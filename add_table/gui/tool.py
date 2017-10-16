
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Levels_Controls(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)

class Tool(QtWidgets.QFrame):
    Top = 0
    Bottom = -1
    def __init__(self, app_cfg):
        super().__init__()
        self.app_cfg = app_cfg

        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)

    def add_widget(self, w):
        self.box.addWidget(w, QtCore.Qt.AlignLeft)

    def add_stretch(self, s):
        self.box.addStretch(s)
