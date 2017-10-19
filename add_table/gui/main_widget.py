import os
import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore

from add_table import pth
from add_table.gui import tool


class Btn(QtWidgets.QPushButton):
    def __init__(self, name, parent):
        super().__init__()
        self.setObjectName(name)
        self.setCursor(QtCore.Qt.PointingHandCursor)

class LevelBtn(QtWidgets.QPushButton):
    def __init__(self, name, parent):
        super().__init__()
        size = QtCore.QSize(35, 35)
        self.name = str(name)
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setObjectName("level_btn_" + self.name)
        pth_icon = os.path.join(pth.ICON, self.name +"v" +  ".png")
        self.setIconSize(size)
        self.setFixedSize(size)
        if os.path.isfile(pth_icon):
            self.setIcon(QtGui.QIcon(pth_icon))
        else:
            self.setText(self.name)
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
        self.form.setStyleSheet("color: green")
        self.form.task.setText("{}".format("win!"))

    def lose_effect(self):

        self.form.result.setStyleSheet("border: 6px solid red;")
        QtWidgets.qApp.processEvents()
        QtCore.QThread.msleep(800)
        self.form.result.setStyleSheet("border: none;")


    def set_lose(self):
        self.form.setStyleSheet("color: red")
        self.form.task.setText("{}".format("loss"))

    def set_color(self, color):
        self.form.setStyleSheet("color: {}".format(color))

    def set_task(self, task: str):
        self.form.task.setText("{}".format(task))

    def clear_task(self):
        self.form.task.clear()

    def clear_result(self):
        self.form.result.clear()

class GameProgress(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(100)


    def add_progress(self, progress):
        self.box.addWidget(progress)

class Progress(QtWidgets.QProgressBar):
    def __init__(self, name):
        super().__init__()
        self.setObjectName(name)
        self._value = 0
        self.setValue(0)
        self.setTextVisible(False)

    def increase(self, v):
        self.setValue(self.value() + v)




class Widget(QtWidgets.QFrame):


    def __init__(self, app_cfg):
        super().__init__()
        self.app_cfg = app_cfg

        self.setObjectName("main_widget")
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)

        self.tasklb = TaskLabel()
        self.box.addWidget(self.tasklb)
        self.game_progress = GameProgress()
        self.box.addWidget(self.game_progress)




        self.progress = Progress("timer")
        self.game_progress.add_progress(self.progress)

        self.task_progress = Progress("task_progress")
        self.game_progress.add_progress(self.task_progress)



    def set_tool(self, tool, direct):
        self.box.insertWidget(direct, tool)


