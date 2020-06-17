from PyQt5.QtWidgets import QWidget
import CreateFilmInPlan, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import CreateFilmInProgressWRK


class CreateFilmInPlanWorking(CreateFilmInPlan.Ui_Form, QWidget):
    def __init__(self):
        super(CreateFilmInPlanWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmProgress = CreateFilmInProgressWRK.CreateFilmInProgressWorking()
        self.makeInProgressFilmButton.clicked.connect(self.MakeFilmProgress.show)
