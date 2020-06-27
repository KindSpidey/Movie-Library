from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
import profileActor, PyQt5, CreateActorWRK, json, time


class profileActorWorking(profileActor.Ui_Form, QWidget):
    def __init__(self, parent):
        self.actorInfo = []
        self.dataActor = []
        self.parent = parent
        super(profileActorWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.editActor = CreateActorWRK.CreateActorWorking(parent,self)
        self.edit.clicked.connect(self.edit_actor)
    def edit_actor(self):
        self.editActor.edit_actor()
        self.editActor.action = 'edit'
        self.editActor.show()
    def set_all(self):
        self.parent.client_server.send(self.parent.chosen_actor+']WorkingBD.get_actor_by_name_for_profile')
        time.sleep(0.3)
        self.dataActor = json.loads(self.parent.client_server.answer)
        self.actorInfo = self.dataActor[0]
        self.headWithName.setText(str(self.actorInfo[0]))
        self.email.setText('email: '+ str(self.actorInfo[3]))
        self.averageSalary.setText('Средняя зарплата: '+ str(self.actorInfo[1]))
        self.phone.setText(str(self.actorInfo[2]))
        self.sex.setText('Пол: '+ str(self.actorInfo[4]))
        self.age.setText('Возраст: '+ str(self.actorInfo[5]))

    def fill_salary_actor_table(self):
        self.moviesTable.setRowCount(0)
        length = len(self.dataActor[1])+len(self.dataActor[2])
        self.moviesTable.setRowCount(length)
        if len(self.dataActor[1]) != 0:
            for raw in range(0, len(self.dataActor[1])):
                for columns in range(0, self.moviesTable.columnCount()):
                    a = str(self.dataActor[1][raw][columns])
                    self.moviesTable.setItem(raw, columns, QTableWidgetItem(a))
            for raw in range(len(self.dataActor[1]), len(self.dataActor[1])+len(self.dataActor[2])):
                self.moviesTable.setItem(raw, 0, QTableWidgetItem(self.dataActor[2][raw-len(self.dataActor[1])]))
        else:
            for raw in range(len(self.dataActor[1]), len(self.dataActor[1])+len(self.dataActor[2])):
                self.moviesTable.setItem(raw, 0, QTableWidgetItem(self.dataActor[2][raw]))