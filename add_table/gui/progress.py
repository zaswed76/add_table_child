

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt5 import QtWidgets as QtGui
from PyQt5 import QtCore


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
        context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))


QtCore.qInstallMessageHandler(qt_message_handler)



class MyThread(QtCore.QThread, QtCore.QObject):
    signal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True
        self.value = 10

    def run(self):
        self.running = True
        while self.running:
            self.signal.emit(self.value)
            time.sleep(0.5)
            self.value -= 1


    def set_start_value(self, v):
        self.value = v


class ControlWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.hbox = QtGui.QHBoxLayout(self)
        self.start_but = QtGui.QPushButton("start")
        self.start_but.clicked.connect(self.start)

        self.stop_but = QtGui.QPushButton("stop")
        self.stop_but.clicked.connect(self.stop)

        self.lab = QtGui.QProgressBar()
        self.lab.setFixedWidth(500)
        self.lab.setRange(0, 10)
        self.lab.setStyleSheet("background-color: lightgrey;")

        self.hbox.addWidget(self.start_but)
        self.hbox.addWidget(self.stop_but)
        self.hbox.addWidget(self.lab)
        self.setLayout(self.hbox)
        #-------------------------------------------------------------

        self.thread = MyThread()
        self.thread.signal.connect(self.on_change)

        #-------------------------------------------------------------

    def start(self):
        self.thread.running = False
        self.thread.running = True
        self.thread.set_start_value(10)
        self.thread.start()

    def stop(self):
        self.lab.setValue(30)

    def on_change(self, s):
        s = int(s)
        if s == 0:
            self.start()
        self.lab.setValue(s)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = ControlWindow()
    main.show()
    sys.exit(app.exec_())





