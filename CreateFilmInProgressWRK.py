from PyQt5.QtWidgets import QWidget
import CreateFilmInProgress, PyQt5, CreateFilmWRK
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal


class CreateFilmInProgressWorking(CreateFilmInProgress.Ui_Form, QWidget):
    def __init__(self):
        super(CreateFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmDone = CreateFilmWRK.CreateFilmWorking()
        self.makeInProgressFilmButton.clicked.connect(self.MakeFilmDone.show) #сделать установку текста текущего фильма в следующем окне

