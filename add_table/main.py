# -*- coding: utf-8 -*-

import os
import sys

import time
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from add_table import game_manager, game_stat, config, app
from add_table.lib import config_lib
from add_table import pth
from add_table.games import add_table
from add_table.gui import main_widget, success, tool, grade, root_settings
from add_table.lib import add_css


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
        self.add_table_game = add_table.TableGame("add_table")

        self.game_manager.add_game(self.add_table_game)

        self.minus_table_game = add_table.TableGame("minus_table")
        self.game_manager.add_game(self.minus_table_game)



        self.game_process = False
        self.__test_mode = False
        self._init_gui()



    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        style = add_css.get_style(pth.CSS_DIR)

        app.setStyleSheet(style)
        self.gui = main_widget.Widget(self.app_cfg)
        self.gui.setWindowTitle(self.cfg.window_title)

        self.success_widget = success.SuccessWidget(self.stat_cfg)
        add_success = success.TabSuccess("add_table", self.app_cfg,
                                         self.cfg,
                                         self.game_stat,
                                         icon=os.path.join(pth.ICON,
                                                           "add_tab.png"))
        add_success.home_btn.clicked.connect(self.show_base_window)
        self.success_widget.add_success(add_success)

        multi_success = success.TabSuccess("multi", self.app_cfg,
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



    def show_base_window(self):
        self.gui.set_stack(self.gui.base_widget)

    def _init_tool(self):
        width, height = self.app_cfg.size_window
        self.tool = tool.Tool(self.app_cfg)
        self.gui.set_tool(self.tool, direct=tool.Tool.Top)
        size_btn = QtCore.QSize(*self.app_cfg.btn_size)
        self.stop_btn = main_widget.Btn("stop_btn", size_btn, self)
        self.tool.add_widget(self.stop_btn)

        # region start button
        self.start_btn = main_widget.Btn("start_btn", size_btn, self)
        self.tool.add_widget(self.start_btn)
        self.start_btn.setFocus()
        # endregion

        self.send_time_btn = main_widget.Btn("send_time_btn",
                                             size_btn, self)
        self.send_time_btn.setCheckable(True)
        self.send_time_btn.setChecked(False)
        self.tool.add_widget(self.send_time_btn)

        self.choose_game_btn = main_widget.Combo("chgame",
                                                 QtCore.QSize(45, 32), self)
        self.tool.add_widget(self.choose_game_btn)

        ctrls_lst = [2, 3, 4, 5,
                     6, 7, 8, 9]
        _size_btn = QtCore.QSize(28, 28)
        controls = [main_widget.LevelBtn(x, _size_btn, self) for x in
                    ctrls_lst]
        self.level_ctrl = tool.Levels_Controls(self.game_stat)
        self.level_ctrl.set_controls(controls)

        # my_ctrl = main_widget.LevelBtn("M", _size_btn, self, "user")
        # self.level_ctrl.add_ctrl(my_ctrl)

        self.tool.add_stretch(1)
        self.tool.add_widget(self.level_ctrl)
        self.tool.add_stretch(1)

        self.grade = grade.Grade(self.cfg, size_btn)
        self.tool.add_widget(self.grade)
        self.grade.set_grade(self.cfg.grade)
        # self.tool.add_stretch(1)

        # region config button
        _size = QtCore.QSize(79, 79)
        self.cfg_btn = main_widget.Btn("success_btn", _size, self)
        self.cfg_btn.setIconSize(_size)
        self.tool.add_widget(self.cfg_btn)
        # endregion


        self.choose_game_btn.currentIndexChanged.connect(self.choose_game)
        self.start_btn.clicked.connect(self.start_game)
        self.stop_btn.clicked.connect(self.stop_game)
        self.cfg_btn.clicked.connect(self.open_success)
        self.send_time_btn.clicked.connect(
            self.checked_progress_timer)
        for gc in self.level_ctrl.controls:
            gc.clicked.connect(self.choose_level)

    def choose_game(self, i):
        self.current_game = i

    def checked_progress_timer(self):
        self.cfg.progress_timer_checked = self.send_time_btn.isChecked()

    def choose_level(self):
        sender = self.sender()
        self.game_stat.current_level = sender.name
        self.stop_game()

    def stop_game(self):
        self.game_process = False
        self.send_time_btn.setDisabled(False)
        self.gui.tasklb.result.setDisabled(True)
        self.grade.setDisabled(False)

        self.gui.progress.reset()
        self.gui.task_progress.reset()
        try:
            self.progress_timer.stop()
        except AttributeError:
            pass
        self.gui.tasklb.clear_task()
        self.gui.tasklb.clear_result()
        self.send_time_btn.setChecked(False)

    def get_current_game(self):
        self.current_index_game = self.choose_game_btn.currentIndex()
        return self.game_manager[self.current_index_game]

    def start_game(self):
        self.current_game = self.get_current_game()
        self.t1 = time.time()
        self.game_process = True
        self.send_time_btn.setDisabled(True)
        self.gui.tasklb.result.setDisabled(False)
        self.gui.tasklb.set_color("#555555")
        current_level = self.game_stat.current_level
        self.game_stat.place = self.grade.current_step


        self.current_game.create_tasks(
            int(current_level), self.current_game.operator,
            mix=self.cfg.mix, test_mode=self.__test_mode)
        self.current_game.run_new_game()
        self.next_step()
        self.start_task_progress()
        if self.cfg.progress_timer_checked:
            self.start_progress()
        # слайд
        self.start_range_timer()

    def start_range_timer(self):
        range_timer = self.cfg.timer
        if range_timer:
            self.timer = QTimer()
            self.timer.timeout.connect(self.tick)
            self.timer.start(range_timer * 1000)

    def open_success(self):

        self.success_widget.update_tabs()
        self.gui.set_stack(self.success_widget)

    def tick(self):
        self.next_step()

    def accept_answer(self):
        try:
            self.timer.stop()
        except AttributeError:
            pass
        answer = self.gui.tasklb.result.text()
        if answer:
            result = self.current_game.check_answer(answer)
        else:
            result = False

        if result:
            self.gui.task_progress.increase(1)
            self.gui.tasklb.result.clear()

            self.next_step()

        else:
            self.text.clear()
            self.gui.tasklb.result.clear()
            self.gui.tasklb.lose_effect()
        try:
            self.timer.start()
        except AttributeError:
            pass

    def next_step(self):
        self.text.clear()
        task = self.current_game.next_step
        if task is not None:
            self.gui.tasklb.set_task(task.text)
        else:
            self.stop_game()
            self.gui.tasklb.set_finish_win()

            self.game_stat.game_time = round(time.time() - self.t1)
            self.save_stat()

    def _update_stat(self, stat_data, current_level,
                     current_rang=None,
                     current_time=None):
        if current_rang is not None:
            stat_data[current_level]["last_rang"] = current_rang
        if current_time is not None:
            stat_data[current_level]["last_time"] = current_time

    def save_stat(self):
        current_time = self.game_stat.game_time
        current_rang = self.grade.current_rang
        current_level = self.game_stat.current_level


        stat_data = self.stat_cfg.data[self.current_game.name_game]
        last_time = stat_data.get(self.game_stat.current_level,
                                  {}).get("last_time")
        last_rang = stat_data.get(self.game_stat.current_level,
                                  {}).get("last_rang")

        if last_rang is None:
            if not self.cfg.progress_timer_checked:
                current_rang = 4
            stat_data[current_level] = {}
            self._update_stat(stat_data, current_level,
                                  current_rang, current_time)
            self.stat_cfg.save()
        elif current_rang < last_rang and current_time < last_time:
            self._update_stat(stat_data, current_level,
                              current_rang, current_time)
            self.stat_cfg.save()
        elif current_rang < last_rang and current_time >= last_time:
            self._update_stat(stat_data, current_level,
                              current_rang, current_time=None)
            self.stat_cfg.save()
        elif current_time < last_time:
            self._update_stat(stat_data, current_level,
                              current_rang=None,
                              current_time=current_time)
            self.stat_cfg.save()



    def start_progress(self):
        if self.send_time_btn.isChecked():
            self.gui.progress.reset()
            self.progress_timer = QTimer()
            self.gui.progress.setMaximum(self.cfg.progress_max)
            self.progress_timer.timeout.connect(self.progress_tick)
            progress_range = self.cfg.grade_to_timer[
                self.grade.current_step]
            self.progress_timer.start(progress_range)
            self.grade.setDisabled(True)

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

    def show_root_settings(self):

        self.root.form.clear_stat_btn.clicked.connect(self.clear_success)
        self.root.form.check_test.clicked.connect(self.check_test)
        self.root.show()

    def check_test(self):
        self.__test_mode = self.root.form.check_test.isChecked()



    def clear_success(self):
        self.stat_cfg.data[self.current_game.name_game].clear()
        self.stat_cfg.save()
        # self.save_stat()
        self.success_widget.update_tabs()


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Q and not self.game_process:
            self.start_game()
        if (QKeyEvent.modifiers() == QtCore.Qt.ControlModifier and
            QKeyEvent.key() == QtCore.Qt.Key_S):
            self.show_root_settings()
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.accept_answer()
        elif QKeyEvent.key() == QtCore.Qt.Key_Backspace:
            self.text.clear()
            self.gui.tasklb.result.clear()
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
