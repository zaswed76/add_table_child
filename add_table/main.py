import sys

import time
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QTimer

from add_table import pth
from add_table.gui import main_widget, config_widget, tool
from add_table import game_manager, game_stat, config, app
from add_table.games import add_table


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

class Main:
    num_keys = {
        QtCore.Qt.Key_0: "0", QtCore.Qt.Key_1: "1", QtCore.Qt.Key_2: "2",
        QtCore.Qt.Key_3: "3", QtCore.Qt.Key_4: "4", QtCore.Qt.Key_5: "5",
        QtCore.Qt.Key_6: "6", QtCore.Qt.Key_7: "7", QtCore.Qt.Key_8: "8",
        QtCore.Qt.Key_9: "9"
    }
    def __init__(self):
        self.text = []

        self.game_manager = game_manager.GameManager()
        self.game_manager.add_game(add_table.AddTableGame("add_table"))
        self.cfg = config.Config(pth.CONFIG)
        self.app_cfg = app.Config(pth.APPEARANCE)
        self.game_stat = game_stat.GameStat(self.cfg)

        self._init_gui()

    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
        self.gui = main_widget.Widget(self.app_cfg)
        self.gui.keyPressEvent = self.keyPressEvent
        self.gui.show()
        self.gui.resize(*self.app_cfg.size_window)


        self._init_tool()



        sys.exit(app.exec_())

    def _init_tool(self):
        width, height = self.app_cfg.size_window
        self.tool = tool.Tool(self.app_cfg)
        self.gui.set_tool(self.tool, direct=tool.Tool.Top)

        # region start button
        self.start_btn = main_widget.Btn("start_btn", self)
        # self.start_btn.setFixedSize(*self.app_cfg.btn_size)
        self.tool.add_widget(self.start_btn)
        # endregion

        self.level_ctrl = tool.Levels_Controls()
        self.tool.add_stretch(50)
        self.tool.add_widget(self.level_ctrl)
        self.tool.add_stretch(50)

        # region config button
        self.cfg_btn = main_widget.Btn("cfg_btn", self)
        # self.cfg_btn.setFixedSize(*self.app_cfg.btn_size)
        self.tool.add_widget(self.cfg_btn)
        # endregion


        # self.gui.start_btn.clicked.connect(self.start_game)
        # self.gui.cfg_btn.clicked.connect(self.open_config_wiget)
        # self.gui.start_btn.setFocus()

    def start_game(self):
        range_timer = self.cfg.timer
        self.current_game = self.game_manager[self.cfg.current_game]
        self.current_game.create_tasks(2, "add", mix=self.cfg.mix)
        self.next_step()
        self.start_progress()
        if range_timer:
            self.timer = QTimer()
            self.timer.timeout.connect(self.tick)
            self.timer.start(range_timer * 1000)

    def open_config_wiget(self):
        self.config_widget = config_widget.ConfigWidget(self.cfg)
        self.config_widget.show()

    def tick(self):
        self.next_step()

    def keyPressEvent(self, QKeyEvent):
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


    def accept_answer(self):
        try:
            self.timer.stop()
        except AttributeError:
            pass
        answer = self.gui.tasklb.result.text()
        result = self.current_game.check_answer(answer)
        if result:
            self.gui.tasklb.result.clear()
            self.gui.tasklb.result.clear()
            self.next_step()
        else:
            self.text.clear()
            self.gui.tasklb.result.clear()
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
            self.gui.tasklb.set_finish()

    def start_progress(self):
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.progress_tick)
        self.progress_timer.start(3000)

    def progress_tick(self):
        self.gui.progress.increase()


if __name__ == '__main__':
    Main()
