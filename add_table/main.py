import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from add_table import pth
from add_table.gui import main_widget
from add_table import task_manager
from add_table.tasks import add_table

# def qt_message_handler(mode, context, message):
#     if mode == QtCore.QtInfoMsg:
#         mode = 'INFO'
#     elif mode == QtCore.QtWarningMsg:
#         mode = 'WARNING'
#     elif mode == QtCore.QtCriticalMsg:
#         mode = 'CRITICAL'
#     elif mode == QtCore.QtFatalMsg:
#         mode = 'FATAL'
#     else:
#         mode = 'DEBUG'
#     print('qt_message_handler: line: %d, func: %s(), file: %s' % (
#         context.line, context.function, context.file))
#     print('  %s: %s\n' % (mode, message))
#
#
# QtCore.qInstallMessageHandler(qt_message_handler)

class Main:
    def __init__(self):
        self._init_gui()
        self.task_manager = task_manager.TaskManager()
        self.task_manager.add_task(add_table.AddTable("add_table"))


    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
        self.gui = main_widget.Widget()
        self.gui.show()
        self.gui.resize(500, 350)
        sys.exit(app.exec_())




if __name__ == '__main__':
    Main()