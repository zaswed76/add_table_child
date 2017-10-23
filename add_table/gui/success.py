import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class SuccessLabel(QtWidgets.QLabel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setFixedHeight(33)
        self.setFixedWidth(25*12)
        self.setText(name)


class TabSuccess(QtWidgets.QFrame):
    def __init__(self, name, app_cfg, cfg, game_stat, icon=None):
        super().__init__()
        if icon is not None:
            self.icon = QtGui.QIcon(icon)
        self.setObjectName(name)
        self.game_stat = game_stat
        self.cfg = cfg
        self.app_cfg = app_cfg

        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)


        for name in self.game_stat.levels.keys():

            lb = SuccessLabel(name)
            self.box.addWidget(lb)

        rect = QtCore.QRect(0, 0, *app_cfg.size_window)
        tr = rect.topRight()
        self.home_btn = QtWidgets.QPushButton(self)
        self.home_btn.setObjectName("home_btn")
        size_btn = QtCore.QSize(35, 35)
        x = tr.x() - size_btn.width()*2
        self.home_btn.setIconSize(size_btn)
        self.home_btn.move(x, 0)




class AddTabSuccess(TabSuccess):
    def __init__(self, name, app_cfg, cfg, game_stat, icon=None):
        super().__init__(name, app_cfg, cfg, game_stat, icon=None)

        if icon is not None:
            self.icon = QtGui.QIcon(icon)


class SuccessWidget(QtWidgets.QDialog):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        box = QtWidgets.QVBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        self.tab = QtWidgets.QTabWidget(self)
        self.tab.setIconSize(QtCore.QSize(128, 64))
        box.addWidget(self.tab)

    def add_success(self, tab):
        self.tab.addTab(tab, tab.icon, "")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = SuccessWidget()
    main.show()
    sys.exit(app.exec_())
