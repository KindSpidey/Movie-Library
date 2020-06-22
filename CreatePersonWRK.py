from PyQt5.QtWidgets import QWidget
import CreatePerson, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from SQL import WorkingBD
from salaryPersonConnectWRK import salaryPersonConnectWorking

class CreatePersonWorking(CreatePerson.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_profile):
        self.parent_main = parent_main
        self.parent_profile = parent_profile
        self.action = ''
        super(CreatePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.salary = salaryPersonConnectWorking(self)
        self.addSalaryButton.clicked.connect(self.go_to_salary)
        self.saveButton.clicked.connect(self.submit)
    def go_to_salary(self):
        try:
            self.salary.set_all_actors()
            self.save()
            self.salary.show()
        except:
            pass
    def setHead(self):
        if self.parent_main.create_who == 'director':
            self.head.setText('Добавление режиссера')
        if self.parent_main.create_who == 'composer':
            self.head.setText('Добавление композитора')
        if self.parent_main.create_who == 'screenwriter':
            self.head.setText('Добавление сценариста')
    def submit(self):
        list = []
        films = []
        list.append(self.moviesEdit.toPlainText().split(', '))
        for elem in list:
            for film in elem:
                films.append(film)
        if self.parent_main.create_who == 'director':
            WorkingBD.add_director(self.nameEdit.text(),self.phoneEdit.text(),self.emailEdit.text())
            for elem in films:
                WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None, None)
        if self.parent_main.create_who == 'composer':
            WorkingBD.add_composer(self.nameEdit.text(),self.phoneEdit.text(),self.emailEdit.text())
            for elem in films:
                WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None, None)
        if self.parent_main.create_who == 'screenwriter':
            WorkingBD.add_screenwriter(self.nameEdit.text(),self.phoneEdit.text(),self.emailEdit.text())
            for elem in films:
                WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None, None)
        self.parent_main.setup_tables()
        self.hide()

    def edit_person(self):
        try:
            if self.parent_main.who_is_person =='director':
                self.head.setText('Редактирование режиссера')
            if self.parent_main.who_is_person == 'screenwriter':
                self.head.setText('Редактирование сценариста')
            if self.parent_main.who_is_person == 'composer':
                self.head.setText('Редактирование композитора')
        except:
            pass
