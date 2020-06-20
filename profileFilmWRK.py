from PyQt5.QtWidgets import QWidget
import profileFilm
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from SQL import WorkingBD
import sys


class profileFilmWorking(profileFilm.Ui_Form, QWidget):
    def __init__(self, parent):
        self.parent = parent
        super(profileFilmWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.data = []

    def set_all(self):
        data = WorkingBD.get_film_by_title(self.parent.chosen_film_in_tab)
        data = [list(elem) for elem in data]
        self.headTitle.setText(data[0][0])
        self.director.setText('Режиссер: '+ data[0][5])
        self.screenwriter.setText('Сценарист: ' +data[0][6])
        self.composer.setText('Композитор: ' +data[0][7])
        self.year.setText('Год выхода: ' +str(data[0][3]))
        self.score.setText('Рейтинг: ' +str(data[0][2]))
        self.label_9.setText('Сборы: ' +str(data[0][1]))
        self.label_8.setText('Бюджет: ' + str(data[0][4]))

    def fill_salary_table(self):
        self.actorsTable.setRowCount(0)
        actors_str =''
        films = WorkingBD.get_actors_by_film(self.data[0][0])
        self.filmTab.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0,self.filmTab.columnCount()):
                if columns!=8:
                    a = str(films[raw][columns+1])
                    self.filmTab.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][9]
                    for u in actors:
                        if u!=actors[len(actors)-1]:
                            actors_str += u + ', '
                        else:
                            actors_str+=u
                    self.filmTab.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''