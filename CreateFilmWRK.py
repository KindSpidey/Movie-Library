from PyQt5.QtWidgets import QWidget
import CreateFilm
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys

class CreateFilmWorking(CreateFilm.Ui_Form, QWidget):
    def __init__(self):
        super(CreateFilmWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
