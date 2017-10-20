from add_table import pth

import sys
from PyQt5 import QtWidgets, QtCore

class GradeBtn(QtWidgets.QPushButton):
    def __init__(self, name, parent, size):
        super().__init__()
        self.setObjectName(str(name))
        # self.setText(str(name))
        self.setParent(parent)
        self.setFixedSize(size)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setCheckable(True)
        self.setAutoExclusive(True)

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
        _names_step = {6: "second", 4: "first", 8: "third"}
        _names_place = {3: "second", 1: "first", 5: "third"}
        n = 0
        for x in range(3):
            for y in range(3):
                name = _names_step.get(n, n)
                self.grid.addWidget(GradeBtn(name, self, self.size_btn), x, y)
                n+=1




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
    main = Grade(45, 45)
    main.show()
    sys.exit(app.exec_())

