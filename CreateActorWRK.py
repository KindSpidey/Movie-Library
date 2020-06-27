
import CreateActor, PyQt5, time, json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from salaryPersonConnectWRK import salaryPersonConnectWorking

class CreateActorWorking(CreateActor.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.action = ''
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        super(CreateActorWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.salary = salaryPersonConnectWorking(self, parent_main)
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
            self.parent_main.client_server.send(self.nameEdit.text() + ', ' + self.phoneEdit.text()+ ', ' +
                self.emailEdit.text()+ ', ' + self.sexEdit.text()+ ', ' + self.birthYearEdit.text()+ ']WorkingBD.update_actor')
            time.sleep(0.2)
            films = self.get_entered_films()
            for elem in films:
                try:
                    self.parent_main.client_server.send(elem +', '+self.nameEdit.text()+']WorkingBD.connect_film_and_actor')
                    time.sleep(0.2)
                except:
                    pass
                try:
                    self.parent_main.client_server.send(self.nameEdit.text()+', ' + elem + ']WorkingBD.add_actor_in_consist_film')
                    time.sleep(0.2)
                except:
                    pass
            self.parent_profile.fill_salary_actor_table()
            self.parent_profile.set_all()
            self.parent_profile.fill_salary_actor_table()
            self.parent_main.setup_tables()
            self.hide()
        if self.action == 'create':
            self.parent_main.client_server.send(self.nameEdit.text() + ', ' + self.phoneEdit.text() + ', '
                + self.emailEdit.text() + ', ' + self.sexEdit.text() + ', ' + self.birthYearEdit.text() + ']WorkingBD.add_actor')
            time.sleep(0.2)
            films = self.get_entered_films()
            for elem in films:
                try:
                    params_of_film = elem + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(None) + ', ' + str(None)
                    self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=[self.nameEdit.text()], command='WorkingBD.add_film')))
                    time.sleep(0.2)
                except:
                    pass
                try:
                    self.parent_main.client_server.send(elem + ', '+self.nameEdit.text() + ']WorkingBD.connect_film_and_actor')
                    time.sleep(0.2)
                except:
                    pass
                try:
                    self.parent_main.client_server.send(self.nameEdit.text() + ', ' + elem + ']WorkingBD.add_actor_in_consist_film')
                    time.sleep(0.2)
                except:
                    pass
            self.parent_main.setup_tables()
            self.hide()
    def get_entered_films(self):
        films = self.textEdit.toPlainText().split(', ')
        return films

    def get_str_films(self):
        self.parent_main.client_server.send(self.parent_main.chosen_actor + ']WorkingBD.get_films_title_by_actor')
        time.sleep(0.1)
        actors = json.loads(self.parent_main.client_server.answer)
        actors_str =''
        for elem in actors:
            if elem!=actors[len(actors)-1]:
                actors_str+=str(elem) + ', '
            else:
                actors_str+=str(elem)
        return actors_str
    def save(self):
        if self.action == 'edit':
            self.parent_main.client_server.send(self.nameEdit.text() + ', ' + self.phoneEdit.text() + ', ' +
             self.emailEdit.text() + ', ' + self.sexEdit.text() + ', ' + self.birthYearEdit.text() + ']WorkingBD.update_actor')
            time.sleep(0.2)
            films = self.get_entered_films()
            for elem in films:
                try:
                    self.parent_main.client_server.send(elem + ', '+self.nameEdit.text() + ']WorkingBD.connect_film_and_actor')
                    time.sleep(0.2)
                except:
                    pass
                try:
                    self.parent_main.client_server.send(
                        self.nameEdit.text() + ', ' + elem + ']WorkingBD.add_actor_in_consist_film')
                    time.sleep(0.2)
                except:
                    pass
    def edit_actor(self):
        self.parent_main.client_server.send(self.parent_main.chosen_actor + ']WorkingBD.get_films_title_by_actor')
        time.sleep(0.1)
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