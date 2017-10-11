import os
import sys
from PyQt5 import QtWidgets, uic

from add_table import pth




class TaskLabel(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.form = uic.loadUi(os.path.join(pth.UI_DIR, "task_form.ui"), self)
        box = QtWidgets.QHBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        box.addWidget(self.form)

class GameLabel(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")
        self.resize(500, 500)
        box = QtWidgets.QVBoxLayout(self)
        self.tasklb = TaskLabel()
        box.addWidget(self.tasklb)

