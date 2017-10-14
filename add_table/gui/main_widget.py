import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore

from add_table import pth


class Btn(QtWidgets.QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.setObjectName(name)
        self.setCursor(QtCore.Qt.PointingHandCursor)



class TaskLabel(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.form = uic.loadUi(
            os.path.join(pth.UI_DIR, "task_form.ui"), self)
        box = QtWidgets.QHBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        box.addWidget(self.form)
        self.form.task.setFixedSize(400, 100)
        self.form.equal.setFixedSize(100, 100)
        self.form.result.setFixedSize(100, 100)

    def set_finish(self):
        self.form.task.setText("{}".format("Finish"))

    def set_task(self, task: str):
        self.form.task.setText("{}".format(task))


class GameLabel(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        box = QtWidgets.QHBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(100)
        self.setStyleSheet("background-color: green")


class Widget(QtWidgets.QFrame):


    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")
        self.resize(500, 500)
        box = QtWidgets.QVBoxLayout(self)
        self.tasklb = TaskLabel()
        box.addWidget(self.tasklb)
        self.gamelb = GameLabel()
        box.addWidget(self.gamelb)

        self.start_btn = Btn("start_btn", self)






