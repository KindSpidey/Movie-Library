import json, time

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import profileFilmInProgress, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from CreateFilmInProgressWRK import CreateFilmInProgressWorking


class profileFilmInProgressWorking(profileFilmInProgress.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_in_plan):
        self.actors =[]
        self.data = []
        self.parent = parent_main
        self.parent_in_plan = parent_in_plan
        super(profileFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.editFilmInProgress = CreateFilmInProgressWorking(parent_main, self, parent_in_plan)
        self.editButton.clicked.connect(self.edit_mode)
    def edit_mode(self):
        self.editFilmInProgress.action = 'edit'
        self.editFilmInProgress.set_all()
        self.editFilmInProgress.show()
    def set_all(self):
        self.parent.client_server.send((self.parent.chosen_film_in_progress) + ']WorkingBD.get_film_in_progress_by_title')
        time.sleep(0.2)
        self.data = json.loads(self.parent.client_server.answer)
        self.data = [list(elem) for elem in self.data]
        self.actors = self.data[1]
        self.data = self.data[0]
        self.titleHead.setText(self.data[0])
        self.budget.setText('Бюджет: '+ str(self.data[1]))
        self.director.setText('Режиссер: '+self.data[2])
        self.screenwriter.setText('Сценарист: '+self.data[3])
        self.composer.setText('Композитор: '+self.data[4])
    def fill_actors_table(self):
        self.actorTab.setRowCount(0)
        self.actorTab.setRowCount(len(self.actors))
        for raw in range(0, len(self.actors)):
            self.actorTab.setItem(raw, 0, QTableWidgetItem(self.actors[raw]))



