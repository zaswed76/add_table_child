from PyQt5 import QtCore, QtMultimedia, QtWidgets
import sys, os
from  add_table import pth


class Player(QtMultimedia.QMediaPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def play_from_local(self, file):
        url = QtCore.QUrl.fromLocalFile(file)
        content = QtMultimedia.QMediaContent(url)
        self.setMedia(content)
        self.play()


if __name__ == '__main__':
    file = os.path.join(pth.SOUND, "wou.mp3")
    app = QtWidgets.QApplication(sys.argv)
    main = Player()
    main.play_from_local(file)

    sys.exit(app.exec_())
