import fileinput
import glob
import os
import sys
from PyQt5 import QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.lb = QtWidgets.QPushButton(self)


def open_file(file):
    with open(file, "r") as f:
        return f.read()





if __name__ == '__main__':
    from add_table import pth
    direct_css = os.path.join(pth.ROOT, "example\style")
    css_f = os.path.join(direct_css, "base.css")
    css_2 = os.path.join(direct_css, "second.css")




    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(get_style(direct_css))
    main = Widget()
    main.show()
    sys.exit(app.exec_())