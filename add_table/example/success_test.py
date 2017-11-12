from PyQt5 import QtWidgets


# Наследуемся от QMainWindow
class MainWindow(QtWidgets.QFrame):
    # Переопределяем конструктор класса
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Работа с QTableWidget")  # Устанавливаем заголовок окна
        # Устанавливаем центральный виджет

        grid_layout = QtWidgets.QGridLayout(self)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)


        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(3)

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(
            ["Задача", "Место", "Время"])
        self.table.setVerticalHeaderLabels(["", "", ""])

        # self.table.resizeColumnsToContents()

        grid_layout.addWidget(self.table, 0, 0)

    def update_table(self, lines):
        for row, line in enumerate(lines):
            for column, item in enumerate(line):
                # print(item[0])
                self.table.setItem(row, column,
                                   QtWidgets.QTableWidgetItem(item))


if __name__ == "__main__":
    import sys
    from add_table import pth
    from add_table.lib import config_lib

    stat_path = pth.STAT_CONFIG
    stat_cfg = config_lib.Config(pth.STAT_CONFIG)


    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    lines = [(("2 + x"), "III", "25"),
             (("3 + x"), "II", "15")]

    lines2 = [(("2 + x"), "I", "5"),
              (("3 + x"), "I", "1")]

    mw.update_table(lines)

    mw.show()
    sys.exit(app.exec())
