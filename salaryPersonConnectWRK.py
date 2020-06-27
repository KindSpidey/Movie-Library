import salaryPersonConnect, time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class salaryPersonConnectWorking(salaryPersonConnect.Ui_Form, QWidget):
    def __init__(self, parent, parent_main):
        self.parent_main = parent_main
        self.parent = parent
        super(salaryPersonConnectWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.make_connection)

    def make_connection(self):
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.tableWidget.item(row, col).text())
                except:
                    tmp.append('No data')
            data.append(tmp)
        self.whos = self.parent.head.text().split(' ')
        self.whos = self.whos[1][0:len(self.whos[1]) - 1]
        if self.whos == 'актер':
            self.whos = 'actor'
        if self.whos == 'режиссер':
            self.whos = 'director'
        if self.whos == 'композитор':
            self.whos = 'composer'
        if self.whos == 'сценарист':
            self.whos = 'screenwriter'
        for lst in data:
            try:
                self.parent_main.client_server.send(lst[0] + ', ' + self.whos + ', '
            + self.parent.nameEdit.text() + ', ' + lst[1] + ']WorkingBD.connect_salary_and_person')
                time.sleep(0.3)
            except:
                pass
            try:
                self.parent_main.client_server.send(lst[0] + ', ' + self.whos + ', '
                 + self.parent.nameEdit.text() + ', ' + lst[1] + ']WorkingBD.update_salary_when_created')
                time.sleep(0.3)
            except:
                pass
        self.hide()

    def set_all(self):
        self.personName.setText(self.parent.parent_profile.actorInfo[0])

        self.tableWidget.setRowCount(0)
        length = len(self.parent.parent_profile.dataActor[1]) + len(self.parent.parent_profile.dataActor[2])
        self.tableWidget.setRowCount(length)
        if len(self.parent.parent_profile.dataActor[1]) != 0:
            for raw in range(0, len(self.parent.parent_profile.dataActor[1])):
                for columns in range(0, self.tableWidget.columnCount()):
                    a = str(self.parent.parent_profile.dataActor[1][raw][columns])
                    self.tableWidget.setItem(raw, columns, QTableWidgetItem(a))
            for raw in range(len(self.parent.parent_profile.dataActor[1]),
                             len(self.parent.parent_profile.dataActor[1]) + len(
                                     self.parent.parent_profile.dataActor[2])):
                self.tableWidget.setItem(raw, 0, QTableWidgetItem(
                    self.parent.parent_profile.dataActor[2][raw - len(self.parent.parent_profile.dataActor[1])]))
        else:
            for raw in range(len(self.parent.parent_profile.dataActor[1]),
                             len(self.parent.parent_profile.dataActor[1]) + len(
                                     self.parent.parent_profile.dataActor[2])):
                self.tableWidget.setItem(raw, 0, QTableWidgetItem(self.parent.parent_profile.dataActor[2][raw]))
    def set_all_person(self):
        self.tableWidget.setRowCount(0)
        if self.parent.parent_main.who_is_person == 'director':
            self.personName.setText(self.parent.parent_profile.directorInfo[0])
        if self.parent.parent_main.who_is_person == 'composer':
            self.personName.setText(self.parent.parent_profile.composerInfo[0])
        if self.parent.parent_main.who_is_person == 'screenwriter':
            self.personName.setText(self.parent.parent_profile.screenwriterInfo[0])
        length = len(self.parent.parent_profile.dataPerson[1]) + len(self.parent.parent_profile.dataPerson[2])
        self.tableWidget.setRowCount(length)
        if len(self.parent.parent_profile.dataPerson[1]) != 0:
            for raw in range(0, len(self.parent.parent_profile.dataPerson[1])):
                for columns in range(0, self.tableWidget.columnCount()):
                    a = str(self.parent.parent_profile.dataPerson[1][raw][columns])
                    self.tableWidget.setItem(raw, columns, QTableWidgetItem(a))
            for raw in range(len(self.parent.parent_profile.dataPerson[1]),
                             len(self.parent.parent_profile.dataPerson[1]) + len(
                                 self.parent.parent_profile.dataPerson[2])):
                self.tableWidget.setItem(raw, 0, QTableWidgetItem(
                    self.parent.parent_profile.dataPerson[2][raw - len(self.parent.parent_profile.dataPerson[1])]))
        else:
            for raw in range(len(self.parent.parent_profile.dataPerson[1]),
                             len(self.parent.parent_profile.dataPerson[1]) + len(
                                 self.parent.parent_profile.dataPerson[2])):
                self.tableWidget.setItem(raw, 0, QTableWidgetItem(self.parent.parent_profile.dataPerson[2][raw]))


