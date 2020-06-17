from SQL import WorkingBD
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import CreateActorWRK
import CreatePersonWRK
import TrueMain
import profileActorWRK
import profileFilmInPlanWRK
import profileFilmInProgressWRK
import profileFilmWRK
import profilePersonWRK
from CreateFilmInPlanWRK import CreateFilmInPlanWorking
from CreateFilmInProgressWRK import CreateFilmInProgressWorking
from CreateFilmWRK import CreateFilmWorking


class TrueMainWorking(TrueMain.Ui_Form, QWidget):
    def __init__(self):
        self.who =''
        super(TrueMainWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.fill_film_table()
        self.createFilm = CreateFilmWorking()
        self.filmCreate.clicked.connect(self.createFilm.show)
        self.createFilmInPlan = CreateFilmInPlanWorking()
        self.planCreate.clicked.connect(self.createFilmInPlan.show)
        self.createFilmInProgress = CreateFilmInProgressWorking()
        self.progressCreate.clicked.connect(self.createFilmInProgress.show)
        self.createActor = CreateActorWRK.CreateActorWorking()
        self.actorCreate.clicked.connect(self.createActor.show)
        self.createPerson = CreatePersonWRK.CreatePersonWorking()
        self.scrnCreate.clicked.connect(self.createPerson.show)
        self.directorCreate.clicked.connect(self.createPerson.show)
        self.compCreate.clicked.connect(self.createPerson.show)
        self.Find.clicked.connect(self.finds)
        self.ProfFilm = profileFilmWRK.profileFilmWorking()
        self.ProfActor = profileActorWRK.profileActorWorking()
        self.ProfPerson = profilePersonWRK.profilePersonWorking()
        self.ProfFilmInProgress = profileFilmInProgressWRK.profileFilmInProgressWorking()
        self.ProfFilmInPlan = profileFilmInPlanWRK.profileFilmInPlanWorking()
        self.pushButton.setDisabled(True)
        self.pushButton.clicked.connect(self.transtition)


    def finds(self):
        search = self.ObjectName.text()
        list =[]
        #делаем запрос на поиск в БД такого-то человека или фильма
        #if search!= None:
            #смотрим, перед нами фильм, актер или кто-то еще. Затем открываем соответстующее окно
        list.append('Spider-Man')
        list.append('film')
        self.found.setText(list[0])#тут ставим найденое, если нашлось и ничего не найдено, если не нашлось
        self.who = list[1]
        self.pushButton.setEnabled(True)

    def transtition(self):
        if self.who == 'actor':
            self.pushButton.clicked.connect(self.ProfActor.show)
        if self.who == 'person':
            self.pushButton.clicked.connect(self.ProfPerson.show)
        if self.who == 'filmInProgress':
            self.pushButton.clicked.connect(self.ProfFilmInProgress.show)
        if self.who == 'filmInPlan':
            self.pushButton.clicked.connect(self.ProfFilmInPlan.show)
        if self.who == 'film':
            self.pushButton.clicked.connect(self.ProfFilm.show)
    def fill_film_table(self):
        actors_str =''
        self.filmTab.setItem(0,0,QTableWidgetItem('72'))
        films = WorkingBD.get_all_films(WorkingBD())
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

    def fill_film_in_plan_table(self):





