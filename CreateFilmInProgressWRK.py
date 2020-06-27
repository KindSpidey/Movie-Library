from PyQt5.QtWidgets import QWidget
import CreateFilmInProgress, PyQt5, CreateFilmWRK, json, time
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal


class CreateFilmInProgressWorking(CreateFilmInProgress.Ui_Form, QWidget):
    def __init__(self,parent_main, parent_profile, parent_in_plan):
        self.action = ''
        self.actors = ''
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        self.parent_in_plan = parent_in_plan
        super(CreateFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmDone = CreateFilmWRK.CreateFilmWorking(parent_main, self, None, 'make_done')
        self.saveButton.clicked.connect(self.save)
        self.makeDoneMovieButton.clicked.connect(self.MakeFilmDone.set_in_progress)

    def save(self):
        msg = QMessageBox()
        if self.action== 'create':
            if self.actorsEdit.toPlainText() == '' or self.titleEdit.text() == '' or self.budgetEdit.text() == '' or self.dirEdit.text() == '' or self.compEdit.text() == '' or self.scrnEdit.text() == '':
                msg.setText('Заполните все поля')
                msg.exec_()
            else:
                list = []
                actors = []
                list.append(self.actorsEdit.toPlainText().split(', '))
                for elem in list:
                    for s in elem:
                        actors.append(s)
                params_of_film = self.titleEdit.text() + ', ' + self.budgetEdit.text()+ ', ' +self.dirEdit.text()+ ', ' + self.scrnEdit.text()+ ', ' + self.compEdit.text()
                self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=actors, command='WorkingBD.add_filmInProgress')))
                time.sleep(0.2)
        if self.action=='make_in_progress':
            if self.actorsEdit.toPlainText() == '' or self.titleEdit.text() == '' or self.budgetEdit.text() == '' or self.dirEdit.text() == '' or self.compEdit.text() == '' or self.scrnEdit.text() == '':
                msg.setText('Заполните все поля')
                msg.exec_()
            else:
                list = []
                actors = []
                list.append(self.actorsEdit.toPlainText().split(', '))
                for elem in list:
                    for s in elem:
                        actors.append(s)
                self.parent_main.client_server.send(self.titleEdit.text() + ']WorkingBD.remove_filminplan')
                time.sleep(0.2)
                params_of_film = self.titleEdit.text() + ', ' + self.budgetEdit.text() + ', ' + self.dirEdit.text() + ', ' + self.scrnEdit.text() + ', ' + self.compEdit.text()
                self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=actors, command='WorkingBD.add_filmInProgress')))
                time.sleep(0.2)
                self.parent_in_plan.close()
                self.parent_in_plan.parent_profile.close()
        if self.action=='edit':
            if self.actorsEdit.toPlainText() == '' or self.titleEdit.text() == '' or self.budgetEdit.text() == '' or self.dirEdit.text() == '' or self.compEdit.text() == '' or self.scrnEdit.text() == '':
                msg.setText('Заполните все поля')
                msg.exec_()
            else:
                list = []
                actors = []
                list.append(self.actorsEdit.toPlainText().split(', '))
                for elem in list:
                    for s in elem:
                        actors.append(s)
                params_of_film = self.titleEdit.text() + ', ' + self.budgetEdit.text() + ', ' + self.dirEdit.text() + ', ' + self.scrnEdit.text() + ', ' + self.compEdit.text()
                self.parent_main.client_server.send(json.dumps(dict(params=params_of_film, actors=actors, command='WorkingBD.update_filminprogress')))
                time.sleep(0.2)
                self.parent_profile.set_all()
        time.sleep(0.2)
        self.parent_main.setup_tables()
        self.hide()
    def set_in_plan(self):
        self.action = 'make_in_progress'
        self.head.setText('Перевод планируемого фильма в снимаемые')
        self.makeDoneMovieButton.setDisabled(True)
        self.titleEdit.setText(self.parent_in_plan.titleEdit.text())
        self.budgetEdit.setText(self.parent_in_plan.planningBudgetEdit.text())

    def set_all(self):
        if self.action == 'edit':
            self.titleEdit.setText(self.parent_profile.data[0])
            self.budgetEdit.setText(str(self.parent_profile.data[1]))
            self.dirEdit.setText(self.parent_profile.data[2])
            self.scrnEdit.setText(self.parent_profile.data[3])
            self.compEdit.setText(self.parent_profile.data[4])
            self.actors = self.get_str_actors()
            self.actorsEdit.setText(self.actors)
        if self.action == 'create':
            self.makeDoneMovieButton.setDisabled(True)

    def get_entered_actors(self):
        actors = self.textEdit.toPlainText().split(', ')
        return actors

    def get_str_actors(self):
        self.parent_main.client_server.send((self.parent_profile.data[0])+']WorkingBD.get_actors_by_filminprogress')
        time.sleep(0.2)
        actors = json.loads(self.parent_main.client_server.answer)
        actors_str =''
        for elem in actors:
            if elem!=actors[len(actors)-1]:
                actors_str+=str(elem) + ', '
            else:
                actors_str+=str(elem)
        return actors_str