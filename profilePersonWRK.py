import json, time

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import profilePerson, PyQt5, CreatePersonWRK
from PyQt5.QtCore import Qt, pyqtSignal



class profilePersonWorking(profilePerson.Ui_Form, QWidget):
    def __init__(self, parent):
        self.dataPerson = []
        self.parent = parent
        self.directorInfo = ''
        self.screenwriterInfo = ''
        self.composerInfo = ''
        super(profilePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.editPerson = CreatePersonWRK.CreatePersonWorking(parent,self)
        self.editButton.clicked.connect(self.edit_mode)
    def edit_mode(self):
        self.editPerson.edit_person()
        self.editPerson.show()
        self.editPerson.action = 'edit'
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
            self.parent.client_server.send(self.parent.chosen_director + ']WorkingBD.get_director_by_name')
            time.sleep(0.1)
            self.dataPerson = json.loads(self.parent.client_server.answer)
            self.directorInfo = self.dataPerson[0]
            self.nameHead.setText(self.directorInfo[0])
            self.averageSalary.setText('Средняя зарплата: '+str(self.directorInfo[1]))
            self.phone.setText('Телефон: '+str(self.directorInfo[2]))
            self.email.setText('email: '+str(self.directorInfo[3]))
        if self.parent.who_is_person == 'screenwriter':
            self.parent.client_server.send(self.parent.chosen_screenwriter + ']WorkingBD.get_screenwriter_by_name')
            time.sleep(0.1)
            self.dataPerson = json.loads(self.parent.client_server.answer)
            self.screenwriterInfo = self.dataPerson[0]
            self.nameHead.setText(self.screenwriterInfo[0])
            self.averageSalary.setText('Средняя зарплата: ' + str(self.screenwriterInfo[1]))
            self.phone.setText('Телефон: ' + str(self.screenwriterInfo[2]))
            self.email.setText('email: ' + str(self.screenwriterInfo[3]))
        if self.parent.who_is_person == 'composer':
            self.parent.client_server.send(self.parent.chosen_composer + ']WorkingBD.get_composer_by_name')
            time.sleep(0.1)
            self.dataPerson = json.loads(self.parent.client_server.answer)
            self.composerInfo = self.dataPerson[0]
            self.nameHead.setText(self.composerInfo[0])
            self.averageSalary.setText('Средняя зарплата: ' + str(self.composerInfo[1]))
            self.phone.setText('Телефон: ' + str(self.composerInfo[2]))
            self.email.setText('email: ' + str(self.composerInfo[3]))