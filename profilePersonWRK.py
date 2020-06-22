from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import profilePerson, PyQt5, CreatePersonWRK
from PyQt5.QtCore import Qt, pyqtSignal
from SQL import WorkingBD



class profilePersonWorking(profilePerson.Ui_Form, QWidget):
    def __init__(self, parent):
        self.dataPerson = []
        self.parent = parent
        super(profilePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.CreatePerson = CreatePersonWRK.CreatePersonWorking(self)
        self.editButton.clicked.connect(self.edit_mode)
    def edit_mode(self):
        pass
    def fill_salary_table(self):
        self.moviesTable.setRowCount(0)
        length = len(self.dataPerson[1])+len(self.dataPerson[2])
        self.moviesTable.setRowCount(length)
        if len(self.dataPerson[1])!=0:
            for raw in range(0, len(self.dataPerson[1])):
                for columns in range(0, self.moviesTable.columnCount()):
                    a = str(self.dataPerson[1][raw][columns])
                    self.moviesTable.setItem(raw, columns, QTableWidgetItem(a))
            for raw in range(len(self.dataPerson[1]), len(self.dataPerson[1])+len(self.dataPerson[2])):
                self.moviesTable.setItem(raw, 0, QTableWidgetItem(self.dataPerson[2][raw - len(self.dataPerson[1])]))
        else:
            for raw in range(len(self.dataPerson[1]), len(self.dataPerson[1])+len(self.dataPerson[2])):
                self.moviesTable.setItem(raw, 0, QTableWidgetItem(self.dataPerson[2][raw]))

    def set_all(self):
        if self.parent.who_is_person == 'director':
            self.dataPerson = WorkingBD.get_director_by_name(self.parent.chosen_director)
            directorInfo = self.dataPerson[0]
            self.nameHead.setText(directorInfo[0])
            self.averageSalary.setText('Средняя зарплата: '+str(directorInfo[1]))
            self.phone.setText('Телефон: '+str(directorInfo[2]))
            self.email.setText('email: '+str(directorInfo[3]))
        if self.parent.who_is_person == 'screenwriter':
            self.dataPerson = WorkingBD.get_screenwriter_by_name(self.parent.chosen_screenwriter)
            screenwriterInfo = self.dataPerson[0]
            self.nameHead.setText(screenwriterInfo[0])
            self.averageSalary.setText('Средняя зарплата: ' + str(screenwriterInfo[1]))
            self.phone.setText('Телефон: ' + str(screenwriterInfo[2]))
            self.email.setText('email: ' + str(screenwriterInfo[3]))
        if self.parent.who_is_person == 'composer':
            self.dataPerson = WorkingBD.get_composer_by_name(self.parent.chosen_composer)
            composerInfo = self.dataPerson[0]
            self.nameHead.setText(composerInfo[0])
            self.averageSalary.setText('Средняя зарплата: ' + str(composerInfo[1]))
            self.phone.setText('Телефон: ' + str(composerInfo[2]))
            self.email.setText('email: ' + str(composerInfo[3]))