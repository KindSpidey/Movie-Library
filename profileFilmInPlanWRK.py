from PyQt5.QtWidgets import QWidget
import profileFilmInPlan, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal

class profileFilmInPlanWorking(profileFilmInPlan.Ui_Form, QWidget):
    def __init__(self):
        super(profileFilmInPlanWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
