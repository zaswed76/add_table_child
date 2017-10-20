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
        self.size_btn = QtCore.QSize(size.height() / 3,
                                     size.height() / 3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Maximum)
        self.setSizePolicy(sizePolicy)

        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)

        self._names_grid = ["0", "place_1", "2",
                            "place_2", "step_1", "place_3",
                            "step_2", "7", "step_3"]
        self.step_place_link = {"step_1": "place_1",
                                "step_2": "place_2",
                                "step_3": "place_3"}
        self.btns = {}

        self._create_field()

    def _create_field(self):
        n = 0
        for x in range(3):
            for y in range(3):
                name = self._names_grid[n]
                self.btns[name] = GradeBtn(name, self, self.size_btn)
                self.btns[name].clicked.connect(self.change_grade)
                self.grid.addWidget(self.btns[name], x, y)
                n += 1

    def change_grade(self):
        s = self.sender()
        step = s.objectName()
        for s, p in self.step_place_link.items():
            if s == step:
                self.btns[p].setVisible(True)
            else:
                self.btns[p].setVisible(False)

    def init_state_grade(self, grade_name):
        self.btns["place_1"].setVisible(False)
        self.btns["place_2"].setVisible(False)
        self.btns["place_3"].setVisible(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(open(pth.CSS_STYLE, "r").read())
    main = Grade(45, 45)
    main.show()
    sys.exit(app.exec_())
