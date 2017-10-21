import sys
from PyQt5 import QtWidgets, QtGui, QtCore



class TabSuccess(QtWidgets.QFrame):
    def __init__(self, name, app_cfg, cfg, game_stat, icon=None):
        super().__init__()
        if icon is not None:
            self.icon = QtGui.QIcon(icon)
        self.setObjectName(name)
        self.game_stat = game_stat
        self.cfg = cfg
        self.app_cfg = app_cfg



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
        self.tab.setIconSize(QtCore.QSize(40, 40))
        box.addWidget(self.tab)

    def add_success(self, tab):
        self.tab.addTab(tab, tab.icon, "")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = SuccessWidget()
    main.show()
    sys.exit(app.exec_())
