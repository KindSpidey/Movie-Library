
import CreatePerson, time, json
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from salaryPersonConnectWRK import salaryPersonConnectWorking

class CreatePersonWorking(CreatePerson.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        self.action = ''
        super(CreatePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.salary = salaryPersonConnectWorking(self, parent_main)
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
                self.parent_main.client_server.send(self.nameEdit.text()+ ', '+  self.phoneEdit.text()+ ', '+self.emailEdit.text()+ ']WorkingBD.add_director')
                time.sleep(0.3)
                films = self.get_entered_films()
                for elem in films:
                    try:
                        params_of_film = elem + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + self.nameEdit.text() + ', ' + str(None) + ', ' + str(None)
                        self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=[str(None)], command='WorkingBD.add_film')))
                        time.sleep(0.2)
                    except:
                        pass
            if self.parent_profile.parent.who_is_person == 'composer':
                self.parent_main.client_server.send(self.nameEdit.text()+ ', '+  self.phoneEdit.text()+ ', '+self.emailEdit.text()+ ']WorkingBD.add_composer')
                time.sleep(0.3)
                films = self.get_entered_films()
                for elem in films:
                    try:
                        params_of_film = elem + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(
                            None) + ', ' + str(None) + ', ' + str(None) + ', ' + self.nameEdit.text()
                        self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=[str(None)], command='WorkingBD.add_film')))
                        time.sleep(0.3)
                    except:
                        pass
            if self.parent_profile.parent.who_is_person == 'screenwriter':
                self.parent_main.client_server.send(self.nameEdit.text()+ ', '+  self.phoneEdit.text()+ ', '+self.emailEdit.text()+ ']WorkingBD.add_screenwriter')
                time.sleep(0.3)
                films = self.get_entered_films()
                for elem in films:
                    try:
                        params_of_film = elem + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(
                            None) + ', ' + str(None) + ', ' + self.nameEdit.text()+ str(None)
                        self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=[str(None)], command='WorkingBD.add_film')))
                        time.sleep(0.2)
                    except:
                        pass
        if self.action=='edit':
            self.save()
        self.parent_main.setup_tables()
        self.hide()
    def save(self):
        if self.action == 'edit':
            if self.parent_profile.parent.who_is_person == 'director':
                self.parent_main.client_server.send(self.nameEdit.text()+ ', '+  self.phoneEdit.text()+ ', '+self.emailEdit.text()+ ']WorkingBD.update_director')
                time.sleep(0.3)
            if self.parent_profile.parent.who_is_person == 'composer':
                self.parent_main.client_server.send(self.nameEdit.text()+ ', '+  self.phoneEdit.text()+ ', '+self.emailEdit.text()+ ']WorkingBD.update_composer')
                time.sleep(0.3)
            if self.parent_profile.parent.who_is_person == 'screenwriter':
                self.parent_main.client_server.send(self.nameEdit.text()+ ', '+  self.phoneEdit.text()+ ', '+self.emailEdit.text()+ ']WorkingBD.update_screenwriter')
                time.sleep(0.3)
        self.parent_profile.set_all()
        self.parent_profile.fill_salary_table()
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
            self.parent_main.client_server.send(self.parent_main.who_is_person + ', ' +self.parent_profile.directorInfo[0] + ']WorkingBD.get_films_title_by_person')
            time.sleep(0.4)
            actors = json.loads(self.parent_main.client_server.answer)
        if self.parent_main.who_is_person == 'screenwriter':
            self.parent_main.client_server.send(self.parent_main.who_is_person + ', ' +self.parent_profile.screenwriterInfo[0]+ ']WorkingBD.get_films_title_by_person')
            time.sleep(0.2)
            actors = json.loads(self.parent_main.client_server.answer)
        if self.parent_main.who_is_person == 'composer':
            self.parent_main.client_server.send(self.parent_main.who_is_person + ', ' +self.parent_profile.composerInfo[0]+ ']WorkingBD.get_films_title_by_person')
            time.sleep(0.2)
            actors = json.loads(self.parent_main.client_server.answer)
        actors_str =''
        for elem in actors:
            if elem!=actors[len(actors)-1]:
                actors_str+=str(elem) + ', '
            else:
                actors_str+=str(elem)
        return actors_str