from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Работа с QTableWidget")    # Устанавливаем заголовок окна
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет

        grid_layout = QGridLayout()             # Создаём QGridLayout
        central_widget.setLayout(grid_layout)   # Устанавливаем данное размещение в центральный виджет

        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setColumnCount(3)     # Устанавливаем три колонки
        self.table.setRowCount(3)        # и одну строку в таблице

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["Задача", "Место", "Время"])
        self.table.setVerticalHeaderLabels(["", "", ""])

        self.table.resizeColumnsToContents()

        grid_layout.addWidget(self.table, 0, 0)

    def update_table(self, lines):
        for row, line in enumerate(lines):
            for column, item in enumerate(line):
                print(item[0])
                self.table.setItem(row, column, QTableWidgetItem(item))



if __name__ == "__main__":
    import sys
    from add_table import pth

    stat = pth.STAT_CONFIG

    app = QApplication(sys.argv)
    mw = MainWindow()
    lines = [(("2 + x"), "III", "25"),
                 (("3 + x"), "II", "15")]

    lines2 = [(("2 + x"), "I", "5"),
                 (("3 + x"), "I", "1")]



    mw.update_table(lines)

    mw.show()
    sys.exit(app.exec())