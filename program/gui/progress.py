

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



class MyThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True
        self._value = 10

    def run(self):
        self.running = True
        while self.running:
            self.signal.emit(self.value)
            time.sleep(0.5)
            self.value -= 1


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

class Progress(QtGui.QProgressBar):
    def __init__(self):
        super().__init__()
        self.thread = MyThread()
        self.thread.signal.connect(self.setValue)

        #-------------------------------------------------------------

    def start(self):
        self.thread.value = 100
        self.thread.running = True
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
    main = Progress()
    main.setMaximum(100)
    main.start()
    main.show()
    sys.exit(app.exec_())





