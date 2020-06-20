from PyQt5.QtWidgets import QWidget
import CreatePerson, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from SQL import WorkingBD

class CreatePersonWorking(CreatePerson.Ui_Form, QWidget):
    def __init__(self, parent):
        self.parent = parent
        super(CreatePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.saveButton.clicked.connect(self.submit)
    def setHead(self):
        if self.parent.create_who =='director':
            self.head.setText('Добавление режиссера')
        if self.parent.create_who == 'composer':
            self.head.setText('Добавление композитораё')
        if self.parent.create_who == 'screenwriter':
            self.head.setText('Добавление сценариста')
    def submit(self):
        #вызывать несколько методов. Добавлять инфу о человеке. Из поля фильмов добавлять фильм, все остальное заполнить ему nullами
        list = []
        films = []
        list.append(self.moviesEdit.toPlainText().split(', '))
        for elem in list:
            for film in elem:
                films.append(film)
        if self.parent.create_who =='director':
            WorkingBD.add_director(self.nameEdit.text(),self.phoneEdit.text(),self.emailEdit.text())
            for elem in films:
                WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None, None)
        if self.parent.create_who =='composer':
            WorkingBD.add_composer(self.nameEdit.text(),self.phoneEdit.text(),self.emailEdit.text())
            for elem in films:
                WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None, None)
        if self.parent.create_who =='screenwriter':
            WorkingBD.add_screenwriter(self.nameEdit.text(),self.phoneEdit.text(),self.emailEdit.text())
            for elem in films:
                WorkingBD.add_film(elem, None, None, None, None, self.nameEdit.text(), None, None, None)
        self.parent.setup_tables()
        self.hide()