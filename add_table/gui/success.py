import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from add_table.gui import success_table




class TabSuccess(QtWidgets.QFrame):
    def __init__(self, name, app_cfg, cfg, game_stat, icon=None):
        super().__init__()
        if icon is not None:
            self.icon = QtGui.QIcon(icon)

        self.labels = {}
        self.setObjectName(name)
        self.game_stat = game_stat
        self.cfg = cfg
        self.app_cfg = app_cfg

        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)

        self.table = success_table.Table()
        self.box.addWidget(self.table)


        rect = QtCore.QRect(0, 0, *app_cfg.size_window)
        tr = rect.topRight()
        self.home_btn = QtWidgets.QPushButton(self)
        self.home_btn.setObjectName("home_btn")
        size_btn = QtCore.QSize(35, 35)
        x = tr.x() - size_btn.width()*2 -14
        self.home_btn.setIconSize(size_btn)
        self.home_btn.move(x, 0)

    def __repr__(self):
        return "{}".format(self.objectName())

    def update_success(self, stat: dict):
        if stat is not  None:
            self.table.update_table(stat)




class SuccessWidget(QtWidgets.QDialog):
    def __init__(self, stat_cfg):
        super().__init__()
        self.tabs = {}
        self.stat_cfg = stat_cfg
        box = QtWidgets.QVBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        self.tab = QtWidgets.QTabWidget(self)
        self.tab.setIconSize(QtCore.QSize(128, 64))
        box.addWidget(self.tab)

    def add_success(self, tab):
        self.tabs[tab.objectName()] = tab
        self.tab.addTab(tab, tab.icon, "")

    def update_tabs(self):

        for name, tab in self.tabs.items():
            data = self.stat_cfg.data.get(name)
            tab.update_success(data)

    @property
    def current_tab(self):
        return self.tab.currentWidget()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = SuccessWidget()
    main.show()
    sys.exit(app.exec_())
