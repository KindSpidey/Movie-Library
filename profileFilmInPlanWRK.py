import json, time

from PyQt5.QtWidgets import QWidget
import profileFilmInPlan, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from CreateFilmInPlanWRK import CreateFilmInPlanWorking

class profileFilmInPlanWorking(profileFilmInPlan.Ui_Form, QWidget):
    def __init__(self, parent_main):
        self.data =[]
        self.parent_main = parent_main
        super(profileFilmInPlanWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.editFilmInPlan = CreateFilmInPlanWorking(parent_main,self)
        self.edit.clicked.connect(self.edit_mode)

    def edit_mode(self):
        self.editFilmInPlan.action = 'edit'
        self.editFilmInPlan.set_all()
        self.editFilmInPlan.show()

    def set_all(self):
        self.parent_main.client_server.send((self.parent_main.chosen_film_in_plan) + ']WorkingBD.get_film_in_plan')
        time.sleep(0.2)
        self.data = json.loads(self.parent_main.client_server.answer)[0]
        self.headTitle.setText(str(self.data[0]))
        self.theme.setText('Тема: ' + self.data[1])
        self.idea.setText('Замысел: ' + self.data[2])
        self.budget.setText('Примерный бюджет: ' + str(self.data[3]))
        self.description.setText('Описание: ' + str(self.data[4]))
