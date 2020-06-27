import CreateFilm, json, time, SQL
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox


class CreateFilmWorking(CreateFilm.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_in_progress, parent_profile, action):
        self.action = action
        self.actors =''
        self.parent = parent_main
        self.parent_profile = parent_profile
        self.parent_in_progress = parent_in_progress
        super(CreateFilmWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.saveButton.clicked.connect(self.save)

    def save(self):
        msg = QMessageBox()
        if self.textEdit.toPlainText() == '' or self.titleEdit.text() == '' or self.boxOfficeEdit.text() == '' or self.scoreEdit.text() == '' or self.yearEdit.text() == '' or self.budgetEdit.text() == '' or self.dirEdit.text() == '' or self.scoreEdit.text() == '' or self.compEdit.text() == '':
            msg.setText('Заполните все поля')
            msg.exec_()
        else:
            list = []
            actors = []
            list.append(self.textEdit.toPlainText().split(', '))
            for elem in list:
                for s in elem:
                    actors.append(s)
            if self.action=='make_done':
                params_of_film = self.titleEdit.text()+ ', ' + self.boxOfficeEdit.text()+ ', '+self.scoreEdit.text()+ ', ' + self.yearEdit.text()+ ', ' +self.budgetEdit.text()+ ', '+self.dirEdit.text()+ ', ' +self.scoreEdit.text()+ ', ' +self.compEdit.text()
                self.parent.client_server.send(self.parent_in_progress.titleEdit.text() + ']WorkingBD.remove_filminprogress')
                time.sleep(0.2)
                self.parent.client_server.send(json.dumps(dict(params = params_of_film, actors = actors, command = 'WorkingBD.add_film')))
                time.sleep(0.2)
                self.parent_in_progress.close()
                self.parent_in_progress.parent_profile.close()
            if self.action=='edit':
                params_of_film = self.titleEdit.text() + ', ' + self.boxOfficeEdit.text() + ', ' + self.scoreEdit.text() + ', ' + self.yearEdit.text() + ', ' + self.budgetEdit.text() + ', '  + self.dirEdit.text() + ', ' + self.scoreEdit.text() + ', ' + self.compEdit.text()
                self.parent.client_server.send(json.dumps(dict(params=params_of_film, actors=actors, command='WorkingBD.update_film')))
                time.sleep(0.2)
                self.parent_profile.set_all()
            if self.action=='create':
                params_of_film = self.titleEdit.text()+ ', ' + self.boxOfficeEdit.text()+ ', '+self.scoreEdit.text()+ ', ' + self.yearEdit.text()+ ', ' +self.budgetEdit.text()+ ', '+self.dirEdit.text()+ ', ' +self.scoreEdit.text()+ ', ' +self.compEdit.text()
                self.parent.client_server.send(json.dumps(dict(params = params_of_film, actors = actors, command = 'WorkingBD.add_film')))
                time.sleep(0.2)
            time.sleep(0.2)
            self.parent.setup_tables()
            self.hide()

    def set_in_progress(self):
        self.action = 'make_done'
        self.head.setText('Перевод снимаемого фильма в снятые')
        self.titleEdit.setText(self.parent_in_progress.titleEdit.text())
        self.scrnEdit.setText(self.parent_in_progress.scrnEdit.text())
        self.dirEdit.setText(self.parent_in_progress.dirEdit.text())
        self.compEdit.setText(self.parent_in_progress.compEdit.text())
        self.budgetEdit.setText(self.parent_in_progress.budgetEdit.text())
        self.textEdit.setText(self.parent_in_progress.actors)
        self.show()

    def set_all(self):
        self.head.setText('Редактирование фильма')
        self.actors = self.get_str_actors()
        self.titleEdit.setText(self.parent_profile.data[0][0])
        self.scrnEdit.setText(self.parent_profile.data[0][6])
        self.dirEdit.setText(self.parent_profile.data[0][5])
        self.compEdit.setText(self.parent_profile.data[0][7])
        self.budgetEdit.setText(self.parent_profile.data[0][0])
        self.textEdit.setText(self.actors)
        self.yearEdit.setText(str(self.parent_profile.data[0][3]))
        self.budgetEdit.setText(str(self.parent_profile.data[0][4]))
        self.scoreEdit.setText(str(self.parent_profile.data[0][2]))
        self.boxOfficeEdit.setText(str(self.parent_profile.data[0][1]))

    def get_entered_actors(self):
        actors = self.textEdit.toPlainText().split(', ')
        return actors

    def get_str_actors(self):
        self.parent.client_server.send((self.parent_profile.data[0][0]) + ']WorkingBD.get_actors_by_film')
        time.sleep(0.2)
        actors = json.loads(self.parent.client_server.answer)
        actors_str =''
        for elem in actors:
            if elem!=actors[len(actors)-1]:
                actors_str+=str(elem) + ', '
            else:
                actors_str+=str(elem)
        return actors_str
