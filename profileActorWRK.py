from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
import profileActor, PyQt5
from SQL import WorkingBD

class profileActorWorking(profileActor.Ui_Form, QWidget):
    def __init__(self, parent):
        self.dataActor = []
        self.parent = parent
        super(profileActorWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)

    def set_all(self):
        self.dataActor = WorkingBD.get_actor_by_name_for_profile(self.parent.chosen_actor)
        actorInfo = self.dataActor[0]
        self.headWithName.setText(actorInfo[0])
        self.email.setText('email'+ actorInfo[3])
        self.averageSalary.setText('Средняя зарплата: '+ str(actorInfo[1]))
        self.phone.setText(actorInfo[2])
        if actorInfo[4]=='male' or actorInfo[4]=='М':
            self.sex.setText('Пол: М')
        else:
            self.sex.setText('Пол: Ж')
        self.age.setText('Возраст: '+ str(actorInfo[5]))

    def fill_salary_actor_table(self):
        self.moviesTable.setRowCount(0)
        length = len(self.dataActor[1])+len(self.dataActor[2])
        self.moviesTable.setRowCount(length)
        if len(self.dataPerson[1])!=0:
            for raw in range(0, len(self.dataActor[1])):
                for columns in range(0, self.moviesTable.columnCount()):
                    a = str(self.dataActor[1][raw][columns])
                    self.moviesTable.setItem(raw, columns, QTableWidgetItem(a))
        for raw in range(len(self.dataActor[1]), len(self.dataActor[1])+len(self.dataActor[2])):
            for elem in self.dataActor[2]:
                self.moviesTable.setItem(raw, 0, QTableWidgetItem(elem))
