import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from add_table import pth
from add_table.gui import main_widget
from add_table import game_manager, game_stat, config
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

class Main:
    def __init__(self):

        self.game_manager = game_manager.GameManager()
        self.game_manager.add_game(add_table.AddTableGame("add_table"))
        self.cfg = config.Config(pth.CONFIG)
        self.game_stat = game_stat.GameStat(self.cfg)
        self.start_game()
        self._init_gui()

    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
        self.gui = main_widget.Widget()
        self.gui.show()
        self.gui.resize(500, 350)
        sys.exit(app.exec_())

    def start_game(self):

        self.current_game = self.game_manager[self.cfg.current_game]
        task = self.current_game.next_step

    def next_step(self):
        pass


if __name__ == '__main__':
    Main()
