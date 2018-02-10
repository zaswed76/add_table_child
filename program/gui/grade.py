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
    def __init__(self, cfg, size):
        super().__init__()

        self.cfg = cfg
        self.size_btn = QtCore.QSize(size.height() / 3+10,
                                     size.height() / 3+10)
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

        self.step_label_link = {"step_1": {"lb": "I R", "rang": 1},
                                "step_2": {"lb": "II R", "rang": 2},
                                "step_3": {"lb": "III R", "rang": 3}}

        self.btns = {}

        self._create_field()

    def _create_field(self):
        n = 0
        for x in range(3):
            for y in range(3):
                name = self._names_grid[n]

                self.btns[name] = GradeBtn(name, self, self.size_btn)
                if name in self.step_place_link.keys():
                    self.btns[name].clicked.connect(self.change_grade)
                else:
                    self.btns[name].setDisabled(True)
                self.grid.addWidget(self.btns[name], x, y)
                n += 1

    def change_grade(self):
        s = self.sender()
        step = s.objectName()
        self.set_grade(step)
        self.cfg.grade = step

    def set_grade(self, step):
        self._current_step = step
        self._current_lab = self.step_label_link[step]["lb"]

        self._current_rang = self.step_label_link[step]["rang"]
        for s, p in self.step_place_link.items():
            if s == step:
                self.btns[p].setVisible(True)
                self.btns[s].toggle()
            else:
                self.btns[p].setVisible(False)

    @property
    def current_step(self):
        return self._current_step

    @property
    def current_label(self):
        return self._current_lab

    @property
    def current_rang(self):
        return self._current_rang

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
