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
        self.Find.clicked.connect(self.search)
        self.ProfFilm = profileFilmWRK.profileFilmWorking()
        self.ProfActor = profileActorWRK.profileActorWorking()
        self.ProfPerson = profilePersonWRK.profilePersonWorking()
        self.ProfFilmInProgress = profileFilmInProgressWRK.profileFilmInProgressWorking()
        self.ProfFilmInPlan = profileFilmInPlanWRK.profileFilmInPlanWorking()
        self.pushButton.setDisabled(True)
        self.pushButton.clicked.connect(self.transtition)
        self.setup_tables()

    def setup_tables(self):
        self.fill_film_table()
        self.fill_film_in_plan_table()
        self.fill_film_in_progress()
        self.fill_actors()
        self.fill_directors()
        self.fill_composers()
        self.fill_screenwriters()
    def search(self):
        search = self.ObjectName.text()
        WorkingBD.get_film_by_title(WorkingBD(), search)
        WorkingBD.get_film_in_progress_by_title(WorkingBD(), search)
        WorkingBD.get_actor_by_name(WorkingBD(), search)
        WorkingBD.get_director_by_name(WorkingBD(), search)
        WorkingBD.get_screenwriter_by_name(WorkingBD(), search)
        WorkingBD.get_composer_by_name(WorkingBD(),search)
        list =[]
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
        films = WorkingBD.get_all_films_in_plan(WorkingBD())
        self.tableWidget_3.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0,self.tableWidget_3.columnCount()):
                a = str(films[raw][columns+1])
                self.tableWidget_3.setItem(raw, columns, QTableWidgetItem(a))
    def fill_film_in_progress(self):
        actors_str = ''
        films = WorkingBD.get_all_films_in_progress(WorkingBD())
        self.tableWidget_2.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.tableWidget_2.columnCount()):
                if columns != 8:
                    a = str(films[raw][columns + 1])
                    self.tableWidget_2.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][9]
                    for u in actors:
                        if u != actors[len(actors) - 1]:
                            actors_str += u + ', '
                        else:
                            actors_str += u
                    self.tableWidget_2.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''
    def fill_actors(self):
        actors_str = ''
        films = WorkingBD.get_all_actors(WorkingBD())
        self.actorTable.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.actorTable.columnCount()):
                if columns != 6:
                    a = str(films[raw][columns + 1])
                    self.actorTable.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][7]
                    for u in actors:
                        if u != actors[len(actors) - 1]:
                            actors_str += u + ', '
                        else:
                            actors_str += u
                    self.actorTable.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''
    def fill_directors(self):
        actors_str = ''
        films = WorkingBD.get_all_person(WorkingBD(),'director')
        self.directorTable.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.directorTable.columnCount()):
                if columns != 4:
                    a = str(films[raw][columns + 1])
                    self.directorTable.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][5]
                    for u in actors:
                        if u != actors[len(actors) - 1]:
                            actors_str += u + ', '
                        else:
                            actors_str += u
                    self.directorTable.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''
    def fill_composers(self):
        actors_str = ''
        films = WorkingBD.get_all_person(WorkingBD(),'composer')
        self.compTable.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.compTable.columnCount()):
                if columns != 4:
                    a = str(films[raw][columns + 1])
                    self.compTable.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][5]
                    for u in actors:
                        if u != actors[len(actors) - 1]:
                            actors_str += u + ', '
                        else:
                            actors_str += u
                    self.compTable.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''
    def fill_screenwriters(self):
        actors_str = ''
        films = WorkingBD.get_all_person(WorkingBD(),'screenwriter')
        self.scrnTable.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.scrnTable.columnCount()):
                if columns != 4:
                    a = str(films[raw][columns + 1])
                    self.scrnTable.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][5]
                    for u in actors:
                        if u != actors[len(actors) - 1]:
                            actors_str += u + ', '
                        else:
                            actors_str += u
                    self.scrnTable.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''




