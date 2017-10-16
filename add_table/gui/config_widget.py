

import sys
from PyQt5 import QtWidgets

class ConfigWidget(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ConfigWidget()
    main.show()
    sys.exit(app.exec_())

