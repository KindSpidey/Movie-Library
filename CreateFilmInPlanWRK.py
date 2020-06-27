import CreateFilmInPlan, time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
import CreateFilmInProgressWRK, profileFilmInPlanWRK

class CreateFilmInPlanWorking(CreateFilmInPlan.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.action = ''
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        super(CreateFilmInPlanWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmProgress = CreateFilmInProgressWRK.CreateFilmInProgressWorking(parent_main, profileFilmInPlanWRK , self)
        self.makeInProgressFilmButton.clicked.connect(self.MakeFilmProgress.show)
        self.saveButton.clicked.connect(self.save)
        self.makeInProgressFilmButton.clicked.connect(self.MakeFilmProgress.set_in_plan)

    def set_all(self):
        if self.action == 'create':
            self.makeInProgressFilmButton.setDisabled(True)
        else:
            self.head.setText('Редактирование планируемого фильма')
            self.titleEdit.setText(str(self.parent_profile.data[0]))
            self.planningBudgetEdit.setText(str(self.parent_profile.data[3]))
            self.ideaEdit.setText(self.parent_profile.data[2])
            self.themeEdit.setText(self.parent_profile.data[1])
            self.descriptionEdit.setText(self.parent_profile.data[4])
    def save(self):
        if self.action=='create':
            self.parent_main.client_server.send(self.titleEdit.text()+ ', ' + self.descriptionEdit.toPlainText()+ ', ' +
                    self.themeEdit.text()+ ', ' +self.ideaEdit.text() + ', '+ self.planningBudgetEdit.text() + ']WorkingBD.add_filminplan')
            time.sleep(0.1)
        else:
            self.parent_main.client_server.send(
                self.titleEdit.text() + ', ' + self.descriptionEdit.toPlainText() + ', ' +
                self.themeEdit.text() + ', ' + self.ideaEdit.text() + ', ' +
                self.planningBudgetEdit.text() + ']WorkingBD.update_filminplan')
            time.sleep(0.1)
        if self.action=='edit':
            self.parent_profile.set_all()
        self.parent_main.setup_tables()
        self.hide()
