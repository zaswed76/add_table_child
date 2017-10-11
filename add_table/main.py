import sys
from PyQt5 import QtWidgets
from add_table import pth
from add_table.gui import main_widget


class Main:
    def __init__(self):
        self._init_gui()


    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
        self.gui = main_widget.Widget()
        self.gui.show()
        self.gui.resize(500, 350)
        sys.exit(app.exec_())




if __name__ == '__main__':
    Main()