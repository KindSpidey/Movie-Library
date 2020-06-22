from PyQt5.QtWidgets import QWidget
import CreateFilmInPlan, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import CreateFilmInProgressWRK
from SQL import WorkingBD

class CreateFilmInPlanWorking(CreateFilmInPlan.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.action = ''
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        super(CreateFilmInPlanWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmProgress = CreateFilmInProgressWRK.CreateFilmInProgressWorking(parent_main)
        self.makeInProgressFilmButton.clicked.connect(self.MakeFilmProgress.show)
        self.saveButton.clicked.connect(self.save)
        self.makeInProgressFilmButton.clicked.connect(self.MakeFilmProgress.set_in_plan)

    def set_all(self):
        self.head.setText('Редактирование планируемого фильма')
        self.titleEdit.setText(self.parent_profile.data[0])
        self.planningBudgetEdit.setText(str(self.parent_profile.data[3]))
        self.ideaEdit.setText(self.parent_profile.data[2])
        self.themeEdit.setText(self.parent_profile.data[1])
        self.descriptionEdit.setText(self.parent_profile.data[4])
    def save(self):
        if self.action=='create':
            WorkingBD.add_filminplan(self.titleEdit.text(),self.descriptionEdit.toPlainText(),self.themeEdit.text(),
                                    self.ideaEdit.text(),self.planningBudgetEdit.text())
        else:
            WorkingBD.update_filminplan(self.titleEdit.text(),self.descriptionEdit.toPlainText(),self.themeEdit.text(),
                                    self.ideaEdit.text(),self.planningBudgetEdit.text())
        self.parent_profile.set_all()
        self.parent_main.setup_tables()
        self.hide()
