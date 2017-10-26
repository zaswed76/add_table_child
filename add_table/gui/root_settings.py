import os
import sys

from PyQt5 import QtWidgets, uic

from add_table import pth


class RootSettings(QtWidgets.QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.resize(500, 500)


        self.form = uic.loadUi(
            os.path.join(pth.UI_DIR, "root_set.ui"), self)
        self.form.setWindowTitle("Окно настроек администратора")
        box = QtWidgets.QHBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        box.setSpacing(0)
        box.addWidget(self.form)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = RootSettings("cfg")
    main.show()
    sys.exit(app.exec_())
