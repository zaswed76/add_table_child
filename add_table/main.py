# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from add_table import game_manager, game_stat, config, app, \
    pth, style, images_rc

from add_table.games import add_table_game
from add_table.gui import main_widget, success, tool, root_settings, media
from add_table.lib import add_css, config_lib


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
        context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))


QtCore.qInstallMessageHandler(qt_message_handler)


class Process(QObject):
    finished = pyqtSignal()
    process = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

    def start_timer(self):
        pass


class Main(QtCore.QObject):
    num_keys = {
        QtCore.Qt.Key_0: "0", QtCore.Qt.Key_1: "1",
        QtCore.Qt.Key_2: "2",
        QtCore.Qt.Key_3: "3", QtCore.Qt.Key_4: "4",
        QtCore.Qt.Key_5: "5",
        QtCore.Qt.Key_6: "6", QtCore.Qt.Key_7: "7",
        QtCore.Qt.Key_8: "8",
        QtCore.Qt.Key_9: "9"
    }

    def __init__(self):
        super().__init__()
        self.text = []
        self.cfg = config.Config(pth.CONFIG)
        self.app_cfg = app.Config(pth.APPEARANCE)
        self.stat_cfg = config_lib.Config(pth.STAT_CONFIG)

        self.game_stat = game_stat.GameStat(self.cfg)
        self.game_manager = game_manager.GameManager()
        self.add_table_game = add_table_game.TableGame("add_table")

        self.game_manager.add_game(self.add_table_game)

        self.minus_table_game = add_table_game.TableGame("minus_table")
        self.game_manager.add_game(self.minus_table_game)

        self.mul_table_game = add_table_game.TableGame("mul_table")
        self.game_manager.add_game(self.mul_table_game)

        self.game_process = False
        self.__test_mode = False
        self._init_gui()

    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        style = add_css.get_style(pth.CSS_DIR)

        app.setStyleSheet(style)
        self.gui = main_widget.Widget(self.app_cfg)
        self.gui.setWindowTitle(self.cfg.window_title)

        self.player = media.Player()
        # self.player.stateChanged.connect(app.quit)

        self.success_widget = success.SuccessWidget(self.stat_cfg)
        add_success = success.TabSuccess("add_table", self.app_cfg,
                                         self.cfg,
                                         self.game_stat,
                                         icon=os.path.join(pth.ICON,
                                                           "add_tab.png"))
        add_success.home_btn.clicked.connect(self.show_base_window)
        self.success_widget.add_success(add_success)

        minus_success = success.TabSuccess("minus_table",
                                           self.app_cfg,
                                           self.cfg,
                                           self.game_stat,
                                           icon=os.path.join(pth.ICON,
                                                             "minus.png"))
        minus_success.home_btn.clicked.connect(self.show_base_window)
        self.success_widget.add_success(minus_success)

        multi_success = success.TabSuccess("mul_table", self.app_cfg,
                                           self.cfg,
                                           self.game_stat,
                                           icon=os.path.join(pth.ICON,
                                                             "multi.png"))
        multi_success.home_btn.clicked.connect(self.show_base_window)
        self.success_widget.add_success(multi_success)

        self.gui.add_to_stack(self.success_widget)
        self.root = root_settings.RootSettings(self.cfg)
        self.gui.keyPressEvent = self.keyPressEvent
        self.gui.closeEvent = self.closeEvent
        self._init_tool()
        self.gui.show()
        self.gui.resize(*self.app_cfg.size_window)
        self.current_game = self.get_current_game()

        sys.exit(app.exec_())

    def _init_tool(self):

        self.tool = tool.Tool(self.app_cfg)
        self.gui.set_tool(self.tool, direct=tool.Tool.Top)
        size_btn = QtCore.QSize(*self.app_cfg.btn_size)
        icon = os.path.join(pth.ICON, "stop_btn.png")
        icon = r"D:\Serg\project\add_table_child\add_table\resource\icons\stop_btn.png"
        self.stop_btn = main_widget.Btn("stop_btn", size_btn, self)

        self.tool.add_widget(self.stop_btn)

        # region start button
        self.start_btn = main_widget.Btn("start_btn", size_btn, self)
        self.tool.add_widget(self.start_btn)
        self.start_btn.setFocus()
        # endregion


        self.choose_game_btn = main_widget.Combo("chgame",
                                                 QtCore.QSize(45, 32),
                                                 self)

        self.tool.add_widget(self.choose_game_btn)

        self.xtwo_btn = main_widget.Btn("xtwo_btn", size_btn, self)
        self.xtwo_btn.setCheckable(True)
        self.tool.add_widget(self.xtwo_btn)

        ctrls_lst = [2, 3, 4, 5,
                     6, 7, 8, 9]
        _size_btn = QtCore.QSize(28, 28)
        controls = [main_widget.LevelBtn(x, _size_btn, self) for x in
                    ctrls_lst]
        self.level_ctrl = tool.Levels_Controls(self.game_stat)
        self.level_ctrl.set_controls(controls)

        self.tool.add_stretch(1)
        self.tool.add_widget(self.level_ctrl)
        self.tool.add_stretch(1)

        _size = QtCore.QSize(55, 55)
        self.cfg_btn = main_widget.Btn("success_btn", _size, self)
        self.cfg_btn.setIconSize(_size)
        self.tool.add_widget(self.cfg_btn)
        # endregion


        self.choose_game_btn.currentIndexChanged.connect(
            self.choose_game)
        self.start_btn.clicked.connect(self.start_game)
        self.stop_btn.clicked.connect(self.stop_game)
        self.cfg_btn.clicked.connect(self.show_success)

        for gc in self.level_ctrl.controls:
            gc.clicked.connect(self.choose_level)

    def show_base_window(self):
        self.gui.set_stack(self.gui.base_widget)

    def show_success(self):
        self.success_widget.update_tabs()
        self.gui.set_stack(self.success_widget)

    def show_root_settings(self):
        self.root.form.check_test.clicked.connect(self.check_test)
        self.root.form.edit_stat_config.clicked.connect(self.edit_stat_config)
        self.root.show()

    def choose_game(self, i):
        self.current_game = i

    def choose_level(self):
        sender = self.sender()
        self.game_stat.current_level = sender.name
        self.stop_game()

    def start_game(self):
        self.stop_game()
        self.current_game = self.get_current_game()
        self.t1 = time.time()
        self.game_process = True

        self.gui.tasklb.result.setDisabled(False)
        self.gui.tasklb.reset_effect()

        current_level = self.game_stat.current_level

        self.current_game.create_tasks(
            int(current_level), self.current_game.operator,
            mix=self.cfg.mix, test_mode=self.__test_mode,
            double=self.xtwo_btn.isChecked())
        self.current_game.run_new_game()
        self.next_step()
        self.start_task_progress()

        # слайд
        self.start_range_timer()

    def stop_game(self):
        self.game_process = False
        self.player.stop()
        self.gui.tasklb.result.setDisabled(True)
        self.gui.progress.reset()
        self.gui.task_progress.reset()
        try:
            self.progress_timer.stop()
        except AttributeError:
            pass
        self.gui.tasklb.clear_task()
        self.gui.tasklb.clear_result()

    def next_step(self):
        self.text.clear()
        task = self.current_game.next_step
        if task is not None:
            self.gui.tasklb.set_task(task.text)
        else:
            self.stop_game()
            self.gui.tasklb.set_finish_win()
            wow_mp3 = os.path.join(pth.SOUND, "wou.mp3")
            self.player.play_from_local(wow_mp3)

            self.game_stat.game_time = round(time.time() - self.t1)
            self.save_stat()

    def get_current_game(self):
        self.current_index_game = self.choose_game_btn.currentIndex()
        return self.game_manager[self.current_index_game]

    def start_range_timer(self):
        range_timer = self.cfg.timer
        if range_timer:
            self.timer = QTimer()
            self.timer.timeout.connect(self.tick)
            self.timer.start(range_timer * 1000)

    def tick(self):
        self.next_step()

    def accept_answer(self):
        try:
            self.timer.stop()
        except AttributeError:
            pass
        answer = self.gui.tasklb.result.text()
        current_task = self.current_game.current_task
        self.game_stat.current_task = current_task
        self.game_stat.current_user_answer = answer
        if answer == "":  # пустое поле
            return
        result = self.current_game.check_answer(answer)
        if result:
            self.gui.task_progress.increase(1)
            self.gui.tasklb.result.clear()
            self.next_step()
        else:
            self.text.clear()
            self.gui.tasklb.result.clear()
            no_mp3 = os.path.join(pth.SOUND, "no.mp3")
            self.player.play_from_local(no_mp3)
            self.gui.tasklb.lose_effect()
        try:
            self.timer.start()
        except AttributeError:
            pass

    def _update_stat(self, stat_data, current_level,
                     current_rang, current_time):
        stat_data[current_level]["last_rang"] = current_rang
        stat_data[current_level]["last_time"] = current_time
        stat_data[current_level]["count"] = len(self.current_game.tasks)

    def start_task_progress(self):
        self.gui.task_progress.reset()
        self.gui.task_progress.increase(1)
        self.gui.task_progress.setMaximum(
            len(self.current_game.tasks))

    def progress_tick(self):
        self.gui.progress.increase(10)
        value = self.gui.progress.value()
        if (value >= self.gui.progress.maximum() and
                self.game_process):
            self.stop_game()
            self.gui.tasklb.set_lose()

    def check_test(self):
        self.__test_mode = self.root.form.check_test.isChecked()

    def edit_stat_config(self):
        subprocess.Popen('explorer "{}"'.format(pth.ETC))

    def save_stat(self):
        len_tasks = len(self.current_game.tasks)
        current_time = self.game_stat.game_time
        current_level = self.game_stat.current_level
        try:
            stat_data = self.stat_cfg.data[
                self.current_game.name_game]
        except KeyError:
            self.stat_cfg.data[self.current_game.name_game] = {}
            stat_data = self.stat_cfg.data[
                self.current_game.name_game]
        last_time = stat_data.get(self.game_stat.current_level,
                                  {}).get("last_time")

        current_rang = self.game_stat.calc_rang(current_time, len_tasks)
        if last_time is None:
            stat_data[current_level] = {}
            self._update_stat(stat_data, current_level,
                              current_rang, current_time)
            self.stat_cfg.save()
        elif last_time > current_time:
            self._update_stat(stat_data, current_level,
                              current_rang, current_time)
            self.stat_cfg.save()

    def clear_success(self, tab=None):
        if tab is not None:
            self.stat_cfg.data[tab].clear()
            self.stat_cfg.save()
            self.success_widget.update_tabs()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Q and not self.game_process:
            self.start_game()
        if (QKeyEvent.modifiers() == QtCore.Qt.ControlModifier and
                    QKeyEvent.key() == QtCore.Qt.Key_S):
            self.show_root_settings()

        if (QKeyEvent.modifiers() == (QtCore.Qt.ControlModifier |
                                          QtCore.Qt.AltModifier) and
                    QKeyEvent.key() == QtCore.Qt.Key_D and
                self.success_widget.isVisible()):
            name_tab = self.success_widget.current_tab.objectName()
            self.clear_success(name_tab)

        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.accept_answer()
        elif QKeyEvent.key() == QtCore.Qt.Key_Backspace:
            self.text.clear()
            self.gui.tasklb.result.clear()

        # показатьт предыдущий вопрос ответ
        elif QKeyEvent.key() == QtCore.Qt.Key_F1:
            answer = self.game_stat.current_user_answer
            current_task = self.game_stat.current_task.text
            self.gui.tasklb.task.setText(current_task)
            self.gui.tasklb.result.setText(answer)
            self.gui.tasklb.set_attention_effect()
        elif self.gui.tasklb.task.text():
            sign = self.num_keys.get(QKeyEvent.key())
            if sign in self.num_keys.values():
                self.text.append(sign)
                self.gui.tasklb.result.setText("".join(self.text))

    def closeEvent(self, *args, **kwargs):
        self.cfg.progress_timer_checked = False
        self.cfg.save()


if __name__ == '__main__':
    Main()
