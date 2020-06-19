from PyQt5.QtWidgets import QWidget
import CreateFilmInProgress, PyQt5, CreateFilmWRK
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal


class CreateFilmInProgressWorking(CreateFilmInProgress.Ui_Form, QWidget):
    def __init__(self,parent):
        self.parent = parent
        super(CreateFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmDone = CreateFilmWRK.CreateFilmWorking(parent, self)
        self.makeInProgressFilmButton.clicked.connect(CreateFilmWRK.CreateFilmWorking(parent,self).show) #сделать установку текста текущего фильма в следующем окне

