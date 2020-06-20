from PyQt5.QtWidgets import QWidget
import profileFilmInPlan, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from SQL import WorkingBD

class profileFilmInPlanWorking(profileFilmInPlan.Ui_Form, QWidget):
    def __init__(self, parent):
        self.data =[]
        self.parent = parent
        super(profileFilmInPlanWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
    def set_all(self):
        self.data = WorkingBD.get_film_in_plan(self.parent.chosen_film_in_plan)[0]
        self.headTitle.setText(self.data[0])
        self.theme.setText('Тема: ' + self.data[1])
        self.idea.setText('Замысел: ' + self.data[2])
        self.budget.setText('Примерный бюджет: ' + str(self.data[3]))
        self.description.setText('Описание: ' + str(self.data[4]))
