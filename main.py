import sys
from random import randint

from PyQt6.QtCore import QUrl, QSize, Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QRadioButton, QPushButton, QLabel, QAbstractButton, \
    QDial, QSlider, QFrame
from PyQt6 import uic

# from testui import Ui_MainWindow


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)

        self.setupUI()

    def setupUI(self):
        self.pushButton.clicked.connect(self.circles)

    def circles(self):
        self.circles_list = []
        for i in range(20):
            radius = randint(0, 40)
            circle = QFrame(self)
            circle.resize(radius * 2, radius * 2)
            circle.move(randint(0, self.width()), randint(0, self.height()))
            circle.setStyleSheet('QFrame{'
                                 f'border-radius: {radius};'
                                 'background-color: yellow;'
                                 '}')
            circle.show()
            self.circles_list.append(circle)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FlagMaker()
    window.show()
    sys.exit(app.exec())
