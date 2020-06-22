from PyQt5.QtWidgets import QWidget
import CreateFilmInProgress, PyQt5, CreateFilmWRK
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from SQL import WorkingBD


class CreateFilmInProgressWorking(CreateFilmInProgress.Ui_Form, QWidget):
    def __init__(self,parent_main, parent_profile, parent_in_plan):
        self.action = ''
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        self.parent_in_plan = parent_in_plan
        super(CreateFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmDone = CreateFilmWRK.CreateFilmWorking(self.parent_main, self)
        self.saveButton.clicked.connect(self.save)
        self.makeDoneMovieButton.clicked.connect(CreateFilmWRK.CreateFilmWorking(self.parent_main,self).show) #сделать установку текста текущего фильма в следующем окне

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
                WorkingBD.add_filmInProgress(self.titleEdit.text(), self.budgetEdit.text(),
                                   self.dirEdit.text(), self.scrnEdit.text(), self.compEdit.text(), actors)
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
                WorkingBD.add_filmInProgress(self.titleEdit.text(), self.budgetEdit.text(),
                                   self.dirEdit.text(), self.scrnEdit.text(), self.compEdit.text(), actors)
                WorkingBD.remove_filminplan(self.titleEdit.text())
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
                WorkingBD.update_filminprogress(self.titleEdit.text(), self.budgetEdit.text(),
                                   self.dirEdit.text(), self.scrnEdit.text(), self.compEdit.text(), actors)
        self.parent_main.setup_tables()
        self.hide()
    def set_in_plan(self):
        self.action = 'make_in_progress'
        self.head.setText('Перевод планируемого фильма в снимаемые')
        self.makeDoneMovieButton.setDisabled(True)
        self.titleEdit.setText(self.parent_in_plan.titleEdit.text())
        self.budgetEdit.setText(self.parent_in_plan.planningBudgetEdit.text())
