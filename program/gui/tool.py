
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Levels_Controls(QtWidgets.QFrame):
    def __init__(self, game_stat):
        super().__init__()

        self.game_stat = game_stat
        self._controls = []

        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(5)

    @property
    def controls(self):
        return self._controls

    def add_ctrl(self, ctrl):
        self._controls.append(ctrl)
        self.box.addWidget(ctrl)

    def set_controls(self, controls: list):
        for c in controls:
            if c.name == self.game_stat.current_level:
                c.setChecked(True)
            self.add_ctrl(c)




class Tool(QtWidgets.QFrame):

    Top = 0
    Bottom = -1
    def __init__(self, app_cfg):
        super().__init__()
        self.app_cfg = app_cfg
        self.setFixedHeight(self.app_cfg.tool_height)

        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)



    def add_widget(self, w):
        self.box.addWidget(w, QtCore.Qt.AlignLeft)

    def add_stretch(self, s):
        self.box.addStretch(s)
