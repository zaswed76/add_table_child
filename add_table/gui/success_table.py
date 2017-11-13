from PyQt5 import QtWidgets, QtCore

class Table(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Достижения")
        grid_layout = QtWidgets.QGridLayout(self)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(9)

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(
            ["Задача", "Место", "Время", "Примеров\nрешено"])
        self.table.setVerticalHeaderLabels([""]*9)


        # self.table.resizeColumnsToContents()

        grid_layout.addWidget(self.table, 0, 0)

        header = self.table.horizontalHeader()
        header.sectionClicked.connect(self.click)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def click(self, r):
        self.table.sortByColumn(r, QtCore.Qt.AscendingOrder)

    def _convert_to_lst(self, data):
        print(data)
        lst = []
        sort_items = self.sorted(data.items(), 0)
        for k, v in sort_items:
            level_lb = "{} + x".format(k)
            line = [level_lb, str(v["last_rang"]),
                    str(v["last_time"]),
                    str(v.get("count", "none"))
                    ]
            lst.append(line)
        return lst

    def sorted(self, lst, flag=True):
        if flag:
            return sorted(lst, key=lambda x:x[0])
        else:
            return lst

    def update_table(self, data):
        self.table.clearContents()
        lines = self._convert_to_lst(data)
        for row, line in enumerate(lines):
            for column, ln in enumerate(line):
                item = QtWidgets.QTableWidgetItem(ln)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row, column, item)




if __name__ == "__main__":
    import sys
    from add_table import pth
    from add_table.lib import config_lib

    stat_path = pth.STAT_CONFIG
    stat_cfg = config_lib.Config(pth.STAT_CONFIG)




    app = QtWidgets.QApplication(sys.argv)
    mw = Table()
    data = stat_cfg.data["add_table"]


    mw.update_table(data)

    mw.show()
    sys.exit(app.exec())
