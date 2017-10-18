from add_table import pth

import sys
from PyQt5 import QtWidgets, QtCore

class GradeBtn(QtWidgets.QPushButton):
    def __init__(self, name, parent, size):
        super().__init__()
        self.setObjectName(name)
        self.setParent(parent)
        self.setFixedSize(size)

class Grade(QtWidgets.QFrame):
    def __init__(self, width, height):
        super().__init__()
        self.setFixedSize(width+20, height)
        size_btn = QtCore.QSize(height/2, height/2)
        self.first = GradeBtn("first", self, size_btn)
        self.first.move(width/2-size_btn.width()/2, 0)
        self.second = GradeBtn("second",self, size_btn)
        self.second.move(0 -5, size_btn.height())
        self.third = GradeBtn("third", self, size_btn)
        self.third.move(width/2, size_btn.height())




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
    main = Grade(45, 45)
    main.show()
    sys.exit(app.exec_())

