from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import profileFilmInProgress, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from SQL import WorkingBD


class profileFilmInProgressWorking(profileFilmInProgress.Ui_Form, QWidget):
    def __init__(self, parent):
        self.actors =[]
        self.data = []
        self.parent = parent
        super(profileFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)

    def set_all(self):
        self.data = WorkingBD.get_film_in_progress_by_title(self.parent.chosen_film_in_progress)
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



