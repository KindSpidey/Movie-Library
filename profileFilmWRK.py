from PyQt5.QtWidgets import QWidget
import profileFilm, json, time
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTableWidgetItem
from CreateFilmWRK import CreateFilmWorking
import sys


class profileFilmWorking(profileFilm.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_in_progress):
        self.parent_main = parent_main
        self.parent_in_progress = parent_in_progress
        super(profileFilmWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.data = []
        self.editFilm = CreateFilmWorking(parent_main,parent_in_progress,self, 'edit')
        self.pushButton.clicked.connect(self.edit_mode)

    def edit_mode(self):
        self.editFilm.action= 'edit'
        self.editFilm.set_all()
        self.editFilm.show()
    def set_all(self):
        self.parent_main.client_server.send((self.parent_main.chosen_film) + ']WorkingBD.get_film_by_title')
        time.sleep(0.2)
        self.data = json.loads(self.parent_main.client_server.answer)
        self.data = [list(elem) for elem in self.data]
        self.headTitle.setText(self.data[0][0])
        self.director.setText('Режиссер: '+ str(self.data[0][5]))
        self.screenwriter.setText('Сценарист: ' +str(self.data[0][6]))
        self.composer.setText('Композитор: ' +str(self.data[0][7]))
        self.year.setText('Год выхода: ' +str(self.data[0][3]))
        self.score.setText('Рейтинг: ' +str(self.data[0][2]))
        self.label_9.setText('Сборы: ' +str(self.data[0][1]))
        self.label_8.setText('Бюджет: ' + str(self.data[0][4]))

    def fill_salary_table(self):
        self.actorsTable.setRowCount(0)
        self.parent_main.client_server.send(self.data[0][0]+']WorkingBD.get_salary_by_film')
        time.sleep(0.1)
        films = json.loads(self.parent_main.client_server.answer)

        self.actorsTable.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0,self.actorsTable.columnCount()):
                a = str(films[raw][columns])
                self.actorsTable.setItem(raw, columns, QTableWidgetItem(a))
