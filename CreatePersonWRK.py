from PyQt5.QtWidgets import QWidget
import CreatePerson, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from SQL import WorkingBD
from salaryPersonConnectWRK import salaryPersonConnectWorking

class CreatePersonWorking(CreatePerson.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        self.action = ''
        super(CreatePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.salary = salaryPersonConnectWorking(self)
        self.addSalaryButton.clicked.connect(self.go_to_salary)
        self.saveButton.clicked.connect(self.true_save)
    def go_to_salary(self):
        try:
            self.salary.set_all_person()
            self.save()
            self.salary.show()
        except:
            pass
    def setHead(self):
        if self.parent_main.create_who == 'director':
            self.head.setText('Добавление режиссера')
        if self.parent_main.create_who == 'composer':
            self.head.setText('Добавление композитора')
        if self.parent_main.create_who == 'screenwriter':
            self.head.setText('Добавление сценариста')
        self.hide()
    def true_save(self):
        if self.action == 'create':
            if self.parent_profile.parent.who_is_person == 'director':
                WorkingBD.add_director(self.nameEdit.text(), self.phoneEdit.text(),self.emailEdit.text())
                films = self.get_entered_films()
                for elem in films:
                    try:
                        WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None,None)
                    except:
                        pass
            if self.parent_profile.parent.who_is_person == 'composer':
                WorkingBD.add_composer(self.nameEdit.text(), self.phoneEdit.text(), self.emailEdit.text())
                films = self.get_entered_films()
                for elem in films:
                    try:
                        WorkingBD.add_film(elem, None, None, None, None, None, None, self.nameEdit.text(), None)
                    except:
                        pass
            if self.parent_profile.parent.who_is_person == 'screenwriter':
                WorkingBD.add_screenwriter(self.nameEdit.text(), self.phoneEdit.text(), self.emailEdit.text())
                films = self.get_entered_films()
                for elem in films:
                    try:
                        WorkingBD.add_film(elem, None, None, None, None, None, self.nameEdit.text(), None, None)
                    except:
                        pass
        if self.action=='edit':
            self.save()
        self.parent_main.setup_tables()
        self.parent_profile.set_all()
        self.parent_profile.fill_salary_table()
        self.hide()
    def save(self):
        if self.action == 'edit':
            if self.parent_profile.parent.who_is_person == 'director':
                WorkingBD.update_director(self.nameEdit.text(), self.phoneEdit.text(),self.emailEdit.text())
            if self.parent_profile.parent.who_is_person == 'composer':
                WorkingBD.update_composer(self.nameEdit.text(), self.phoneEdit.text(),self.emailEdit.text())
            if self.parent_profile.parent.who_is_person == 'screenwriter':
                WorkingBD.update_screenwriter(self.nameEdit.text(), self.phoneEdit.text(),self.emailEdit.text())
    def edit_person(self):
        films = self.get_str_films()
        try:
            if self.parent_main.who_is_person =='director':
                self.head.setText('Редактирование режиссера')
                self.nameEdit.setText(self.parent_profile.directorInfo[0])
                self.phoneEdit.setText(self.parent_profile.directorInfo[2])
                self.emailEdit.setText(self.parent_profile.directorInfo[3])
            if self.parent_main.who_is_person == 'screenwriter':
                self.head.setText('Редактирование сценариста')
                self.nameEdit.setText(self.parent_profile.screenwriterInfo[0])
                self.phoneEdit.setText(self.parent_profile.screenwriterInfo[2])
                self.emailEdit.setText(self.parent_profile.screenwriterInfo[3])
            if self.parent_main.who_is_person == 'composer':
                self.head.setText('Редактирование композитора')
                self.nameEdit.setText(self.parent_profile.composerInfo[0])
                self.phoneEdit.setText(self.parent_profile.composerInfo[2])
                self.emailEdit.setText(self.parent_profile.composerInfo[3])
            self.moviesEdit.setText(films)
        except:
            pass
    def get_entered_films(self):
        films = self.moviesEdit.toPlainText().split(', ')
        return films
    def get_str_films(self):
        actors = ''
        if self.parent_main.who_is_person == 'director':
            actors = WorkingBD.get_films_title_by_person(self.parent_main.who_is_person,self.parent_profile.directorInfo[0])
        if self.parent_main.who_is_person == 'screenwriter':
            actors = WorkingBD.get_films_title_by_person(self.parent_main.who_is_person,
                                                         self.parent_profile.screenwriterInfo[0])
        if self.parent_main.who_is_person == 'composer':
            actors = WorkingBD.get_films_title_by_person(self.parent_main.who_is_person,
                                                         self.parent_profile.composerInfo[0])
        actors_str =''
        for elem in actors:
            if elem!=actors[len(actors)-1]:
                actors_str+=str(elem) + ', '
            else:
                actors_str+=str(elem)
        return actors_str