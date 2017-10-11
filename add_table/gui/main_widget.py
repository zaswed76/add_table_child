import sys
from PyQt5 import QtWidgets


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")
        self.resize(500, 500)
