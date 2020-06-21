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
        self.who_is_person =''
        self.chosen_actor = ''
        self.chosen_director =''
        self.chosen_composer =''
        self.chosen_screenwriter =''
        self.chosen_actor =''
        self.chosen_film_in_plan = ''
        self.chosen_film_in_progress = ''
        self.chosen_film = ''
        self.who =''
        self.create_who =''
        super(TrueMainWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.createFilm = CreateFilmWorking(self, None)
        self.filmCreate.clicked.connect(self.createFilm.show)
        self.createFilmInPlan = CreateFilmInPlanWorking(self)
        self.planCreate.clicked.connect(self.createFilmInPlan.show)
        self.createFilmInProgress = CreateFilmInProgressWorking(self)
        self.progressCreate.clicked.connect(self.createFilmInProgress.show)
        self.createActor = CreateActorWRK.CreateActorWorking(self, profileActorWRK)
        self.actorCreate.clicked.connect(self.create_action)
        self.createPerson = CreatePersonWRK.CreatePersonWorking(self)
        self.scrnCreate.clicked.connect(self.create_screenwriter)
        self.directorCreate.clicked.connect(self.create_director)
        self.compCreate.clicked.connect(self.create_composer)
        self.Find.clicked.connect(self.search)
        self.ProfFilm = profileFilmWRK.profileFilmWorking(self)
        self.ProfActor = profileActorWRK.profileActorWorking(self)
        self.ProfPerson = profilePersonWRK.profilePersonWorking(self)
        self.ProfFilmInProgress = profileFilmInProgressWRK.profileFilmInProgressWorking(self)
        self.ProfFilmInPlan = profileFilmInPlanWRK.profileFilmInPlanWorking(self)
        self.pushButton.setDisabled(True)
        self.setup_tables()
        self.filmTab.itemDoubleClicked.connect(self.film_cell_was_clicked)
        self.film_in_progressTab.itemDoubleClicked.connect(self.film_in_progress_cell_was_clicked)
        self.film_in_planTab.itemDoubleClicked.connect(self.film_in_plan_cell_was_clicked)
        self.directorTable.itemDoubleClicked.connect(self.director_cell_was_clicked)
        self.compTable.itemDoubleClicked.connect(self.composer_cell_was_clicked)
        self.scrnTable.itemDoubleClicked.connect(self.screenwriter_cell_was_clicked)
        self.actorTable.itemDoubleClicked.connect(self.actor_cell_was_clicked)

    #def film_cell_edit(self):
    def create_action(self):
        self.createActor.action = 'create'
        self.createActor.show()

    def actor_cell_was_clicked(self):
        #self.who_is_person = 'actor'
        self.chosen_actor = self.actorTable.selectedItems().__getitem__(0).text()
        self.ProfActor.set_all()
        self.ProfActor.fill_salary_actor_table()
        self.ProfActor.show()
    def composer_cell_was_clicked(self):
        self.who_is_person ='composer'
        self.chosen_composer = self.compTable.selectedItems().__getitem__(0).text()
        self.ProfPerson.set_all()
        self.ProfPerson.fill_salary_table()
        self.ProfPerson.show()

    def screenwriter_cell_was_clicked(self):
        self.who_is_person ='screenwriter'
        self.chosen_screenwriter = self.scrnTable.selectedItems().__getitem__(0).text()
        self.ProfPerson.set_all()
        self.ProfPerson.fill_salary_table()
        self.ProfPerson.show()

    def director_cell_was_clicked(self):
        self.who_is_person ='director'
        self.chosen_director = self.directorTable.selectedItems().__getitem__(0).text()
        self.ProfPerson.set_all()
        self.ProfPerson.fill_salary_table()
        self.ProfPerson.show()
    def film_in_plan_cell_was_clicked(self):
        self.chosen_film_in_plan = self.film_in_planTab.selectedItems().__getitem__(0).text()
        self.ProfFilmInPlan.set_all()
        self.ProfFilmInPlan.show()

    def film_cell_was_clicked(self):
        self.chosen_film = self.filmTab.selectedItems().__getitem__(0).text()
        self.ProfFilm.set_all()
        self.ProfFilm.fill_salary_table()
        self.ProfFilm.show()
    def film_in_progress_cell_was_clicked(self):
        self.chosen_film_in_progress = self.film_in_progressTab.selectedItems().__getitem__(0).text()
        self.ProfFilmInProgress.set_all()
        self.ProfFilmInProgress.fill_actors_table()
        self.ProfFilmInProgress.show()

    def create_director(self):
        self.create_who='director'
        self.createPerson.show()
        self.createPerson.setHead()

    def create_screenwriter(self):
        self.create_who = 'screenwriter'
        self.createPerson.show()
        self.createPerson.setHead()

    def create_composer(self):
        self.create_who = 'composer'
        self.createPerson.show()
        self.createPerson.setHead()

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
        list =[]
        result =''
        try:
            film = WorkingBD.get_film_by_title(search)[0][0]
            self.chosen_film = film
            list.append(film)
            list.append('film')
        except:
            pass
        try:
            filminprogress = WorkingBD.get_film_in_progress_by_title(search)[0][0]
            self.chosen_film_in_progress = filminprogress
            list.append(filminprogress)
            list.append('filminprogress')
        except:
            pass
        try:
            filminplan = WorkingBD.get_film_in_plan(search)[0][0]
            self.chosen_film_in_plan = filminplan
            list.append(filminplan)
            list.append('filminplan')
        except:
            pass
        try:
            actor = WorkingBD.get_actor_by_name(search)[0][0]
            self.chosen_actor = actor
            list.append(actor)
            list.append('actor')
        except:
            pass
        try:
            director = WorkingBD.get_director_by_name(search)[0][0]
            self.chosen_director = director
            list.append(director)
            list.append('director')
        except:
            pass
        try:
            screenwriter = WorkingBD.get_screenwriter_by_name(search)[0][0]
            self.chosen_screenwriter = screenwriter
            list.append(screenwriter)
            list.append('screenwriter')
        except:
            pass
        try:
            composer = WorkingBD.get_composer_by_name(search)[0][0]
            self.chosen_composer = composer
            list.append(composer)
            list.append('composer')
        except:
            pass
        if len(list)==0:
            self.found.setText('Не найдено')
            return
        self.found.setText(list[0])
        self.who = list[1]
        self.pushButton.setEnabled(True)
        self.transtition()

    def transtition(self):
        if self.who == 'actor':
            self.pushButton.clicked.connect(self.ProfActor.show)
        if self.who == 'person':
            self.pushButton.clicked.connect(self.ProfPerson.show)
        if self.who == 'filminprogress':
            self.ProfFilmInProgress.set_all()
            self.ProfFilmInProgress.fill_actors_table()
            self.pushButton.clicked.connect(self.ProfFilmInProgress.show)
        if self.who == 'filminplan':
            self.ProfFilmInPlan.set_all()
            self.pushButton.clicked.connect(self.ProfFilmInPlan.show)
        if self.who == 'film':
            self.ProfFilm.set_all()
            self.ProfFilm.fill_salary_table()
            self.pushButton.clicked.connect(self.ProfFilm.show)
    def fill_film_table(self):
        self.filmTab.setRowCount(0)
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
    def fill_film_in_progress(self):
        self.film_in_progressTab.setRowCount(0)
        actors_str = ''
        films = WorkingBD.get_all_films_in_progress(WorkingBD())
        self.film_in_progressTab.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.film_in_progressTab.columnCount()):
                if columns != 5:
                    a = str(films[raw][columns + 1])
                    self.film_in_progressTab.setItem(raw, columns, QTableWidgetItem(a))
                else:
                    actors = films[raw][6]
                    for u in actors:
                        if u != actors[len(actors) - 1]:
                            actors_str += u + ', '
                        else:
                            actors_str += u
                    self.film_in_progressTab.setItem(raw, columns, QTableWidgetItem(actors_str))
                    actors_str = ''
    def fill_film_in_plan_table(self):
        self.film_in_planTab.setRowCount(0)
        films = WorkingBD.get_all_films_in_plan(WorkingBD())
        self.film_in_planTab.setRowCount(len(films))
        for raw in range(0, len(films)):
            for columns in range(0, self.film_in_planTab.columnCount()):
                a = str(films[raw][columns+1])
                self.film_in_planTab.setItem(raw, columns, QTableWidgetItem(a))
    def fill_actors(self):
        self.actorTable.setRowCount(0)
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
        self.directorTable.setRowCount(0)
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
        self.compTable.setRowCount(0)
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
        self.scrnTable.setRowCount(0)
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




