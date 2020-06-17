from PyQt5.QtWidgets import QWidget
import profileFilm
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys


class profileFilmWorking(profileFilm.Ui_Form, QWidget):
    def __init__(self):
        super(profileFilmWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)