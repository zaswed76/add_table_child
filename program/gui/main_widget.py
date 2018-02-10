import os
import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore

from add_table import pth
from add_table.gui import tool
from jinja2 import Template



class Btn(QtWidgets.QPushButton):
    def __init__(self, name, size,  parent, style=None, icon=None):
        super().__init__()
        self.setObjectName(name)
        print(self.objectName())
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setFixedSize(size)
        self.setIconSize(size)
        # if style is not None:
        #     template = Template(style)
        #     style_sheet = template.render(path=icon)
        #     self.setStyleSheet(style_sheet)
        #     print(style_sheet)

class Combo(QtWidgets.QComboBox):
    def __init__(self, name, size, parent):
        super().__init__()
        self.setObjectName(name)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setFixedSize(size)

        self.addItem(QtGui.QIcon(os.path.join(pth.ICON, "plus.png")), "+")
        self.addItem(QtGui.QIcon(os.path.join(pth.ICON, "minus.png")), "-")
        self.addItem(QtGui.QIcon(os.path.join(pth.ICON, "multi.png")), "*")


class LevelBtn(QtWidgets.QPushButton):
    def __init__(self, name, size, parent, second_name=None):
        super().__init__()
        self.second_name = second_name
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


class Movie(QtGui.QMovie):
    def __init__(self, *__args, **kwargs):
        super().__init__(*__args)
        self.setCacheMode(QtGui.QMovie.CacheAll)
        speed =  kwargs.get("speed", False)
        if speed:
            self.setSpeed(speed)

class TaskLabel(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.form = uic.loadUi(
            os.path.join(pth.UI_DIR, "task_form.ui"), self)
        box = QtWidgets.QHBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        box.addWidget(self.form)
        self.form.task.setFixedSize(500, 100)
        self.form.equal.setFixedSize(100, 100)
        self.form.result.setFixedSize(100, 100)

    def set_finish_win(self):
        image = os.path.join(pth.ICON, "krosh.gif")
        self.movie = Movie(image, QtCore.QByteArray(), self)
        self.form.task.setMovie(self.movie)
        self.movie.start()

    def set_attention_effect(self):
        self.form.task.setStyleSheet("border: 3px solid red;")
        self.form.result.setStyleSheet("border: 3px solid red;")


    def reset_effect(self):
        self.form.task.setStyleSheet("border: none;")
        self.form.result.setStyleSheet("border: none;")
        self.set_color("#555555")

    def lose_effect(self):
        image = os.path.join(pth.ICON, "smile_lose.gif")
        self.movie = Movie(image, QtCore.QByteArray(), self)
        self.form.task.setMovie(self.movie)
        self.movie.start()


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

        self.base_widget = QtWidgets.QFrame()
        self.stack_box = QtWidgets.QStackedLayout(self)
        self.stack_box.setContentsMargins(0, 0, 0, 0)
        self.stack_box.setSpacing(0)
        self.stack_box.addWidget(self.base_widget)


        self.setObjectName("main_widget")
        self.box = QtWidgets.QVBoxLayout(self.base_widget)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.tasklb = TaskLabel()
        self.box.addWidget(self.tasklb)
        self.game_progress = GameProgress()
        self.box.addWidget(self.game_progress)




        self.progress = Progress("timer")
        # self.game_progress.add_progress(self.progress)

        self.task_progress = Progress("task_progress")
        self.game_progress.add_progress(self.task_progress)


    def add_to_stack(self, widget):
        self.stack_box.addWidget(widget)

    def set_tool(self, tool, direct):
        self.box.insertWidget(direct, tool)

    def set_stack(self, widget):
        self.stack_box.setCurrentWidget(widget)


