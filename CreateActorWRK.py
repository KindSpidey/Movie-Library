from PyQt5.QtWidgets import QWidget
import CreateActor, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from SQL import WorkingBD
from salaryPersonConnectWRK import salaryPersonConnectWorking

class CreateActorWorking(CreateActor.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.action = ''
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        super(CreateActorWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.salary = salaryPersonConnectWorking(self)
        self.addSalaryButton.clicked.connect(self.go_to_salary)
        self.saveButton.clicked.connect(self.true_save)

    def go_to_salary(self):
        try:
            self.salary.set_all()
            self.save()
            self.salary.show()
        except:
            pass
    def true_save(self):
        if self.action == 'edit':
            WorkingBD.update_actor(self.nameEdit.text(), self.phoneEdit.text(), self.emailEdit.text(), self.sexEdit.text(),
                                   self.birthYearEdit.text())
            films = self.get_entered_films()
            for elem in films:
                try:
                    WorkingBD.connect_film_and_actor(elem,self.nameEdit.text())
                except:
                    pass
                try:
                    WorkingBD.add_actor_in_consist_film(self.nameEdit.text(), elem)
                except:
                    pass
            self.parent_profile.set_all()
            self.parent_profile.fill_salary_actor_table()
            self.parent_main.setup_tables()
            self.hide()
        if self.action == 'create':
            WorkingBD.add_actor(self.nameEdit.text(), self.phoneEdit.text(),self.emailEdit.text(), self.sexEdit.text(), self.birthYearEdit.text())
            films = self.get_entered_films()
            for elem in films:
                try:
                    WorkingBD.add_film(elem, None, None,None, None,None, None,None,[self.nameEdit.text()])
                except:
                    pass
                try:
                    WorkingBD.connect_film_and_actor(elem,self.nameEdit.text())
                except:
                    pass
                try:
                    WorkingBD.add_actor_in_consist_film(self.nameEdit.text(), elem)
                except:
                    pass
            self.parent_main.setup_tables()
            self.hide()
    def get_entered_films(self):
        films = self.textEdit.toPlainText().split(', ')
        return films

    def get_str_films(self):
        actors = WorkingBD.get_films_title_by_actor(self.parent_main.chosen_actor)
        actors_str =''
        for elem in actors:
            if elem!=actors[len(actors)-1]:
                actors_str+=str(elem) + ', '
            else:
                actors_str+=str(elem)
        return actors_str
    def save(self):
        if self.action == 'edit':
            WorkingBD.update_actor(self.nameEdit.text(), self.phoneEdit.text(),self.emailEdit.text(), self.sexEdit.text(), self.birthYearEdit.text())
            films = self.get_entered_films()
            for elem in films:
                try:
                    WorkingBD.connect_film_and_actor(elem,self.nameEdit.text())
                except:
                    pass
                try:
                    WorkingBD.add_actor_in_consist_film(self.nameEdit.text(), elem)
                except:
                    pass
    def edit_actor(self):
        actors = WorkingBD.get_films_title_by_actor(self.parent_main.chosen_actor)
        films = self.get_str_films()
        try:
            self.head.setText('Редактирование актера')
            self.nameEdit.setText(self.parent_profile.actorInfo[0])
            self.phoneEdit.setText(self.parent_profile.actorInfo[2])
            self.emailEdit.setText(self.parent_profile.actorInfo[3])
            self.sexEdit.setText(self.parent_profile.actorInfo[4])
            self.textEdit.setText(films)
            self.birthYearEdit.setText(str(2020 - self.parent_profile.actorInfo[5]))
        except:
            pass