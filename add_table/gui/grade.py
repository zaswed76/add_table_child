from add_table import pth

import sys
from PyQt5 import QtWidgets, QtCore

class GradeBtn(QtWidgets.QPushButton):
    def __init__(self, name, parent, size):
        super().__init__()
        self.setObjectName(str(name))
        self.setParent(parent)
        self.setFixedSize(size)

class Grade(QtWidgets.QFrame):
    def __init__(self, size):
        super().__init__()
        self.setFixedSize(size)
        self.size_btn = QtCore.QSize(size.height()/3, size.height()/3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.setSizePolicy(sizePolicy)

        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self._create_field()

    def _create_field(self):
        n = 0
        for x in range(3):
            for y in range(3):
                self.grid.addWidget(GradeBtn(n, self, self.size_btn), x, y)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
    main = Grade(45, 45)
    main.show()
    sys.exit(app.exec_())

