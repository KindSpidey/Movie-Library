from PyQt5.QtWidgets import QWidget
import profileFilmInProgress, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal


class profileFilmInProgressWorking(profileFilmInProgress.Ui_Form, QWidget):
    def __init__(self):
        super(profileFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
