import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore

from add_table import pth
from add_table.gui import tool


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


class GameProgress(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(100)


    def add_progress(self, progress):

        self.box.addWidget(progress)

class Progress(QtWidgets.QProgressBar):
    def __init__(self):
        super().__init__()
        self._value = 0
        self.setMaximum(10)
        self.setValue(0)
        self.setTextVisible(False)



    def increase(self):

        self.setValue(self.value() + 1)



class Widget(QtWidgets.QFrame):


    def __init__(self, app_cfg):
        super().__init__()
        self.app_cfg = app_cfg
        width, height = self.app_cfg.size_window
        self.setObjectName("main_widget")
        box = QtWidgets.QVBoxLayout(self)
        self.tasklb = TaskLabel()
        box.addWidget(self.tasklb)
        self.game_progress = GameProgress()
        box.addWidget(self.game_progress)

        self.start_btn = Btn("start_btn", self)
        self.start_btn.setFixedSize(*self.app_cfg.btn_size)
        self.start_btn.move(20, 5)
        self.cfg_btn = Btn("cfg_btn", self)
        self.cfg_btn.setFixedSize(*self.app_cfg.btn_size)

        self.cfg_btn.move(width-self.app_cfg.btn_size[0]/2, 5)


        self.progress = Progress()
        self.game_progress.add_progress(self.progress)





