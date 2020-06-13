from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from CreateFilmWRK import CreateFilmWorking
from CreateFilmInPlanWRK import CreateFilmInPlanWorking
from CreateFilmInProgressWRK import CreateFilmInProgressWorking
import TrueMain, PyQt5, sys

class TrueMainWorking(TrueMain.Ui_Form, QWidget):
    def __init__(self):
        super(TrueMainWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.createFilm = CreateFilmWorking()
        self.filmCreate.clicked.connect(self.createFilm.show)
        self.createFilmInPlan = CreateFilmInPlanWorking()
        self.planCreate.clicked.connect(self.createFilmInPlan.show)
        self.createFilmInProgress = CreateFilmInProgressWorking()
        self.progressCreate.clicked.connect(self.createFilmInProgress.show)
