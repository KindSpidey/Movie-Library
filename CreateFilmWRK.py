from PyQt5.QtWidgets import QWidget
import CreateFilm
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from SQL import WorkingBD
#from TrueMainWRK import TrueMainWorking

class CreateFilmWorking(CreateFilm.Ui_Form, QWidget):
    def __init__(self, parent_main, parent_in_progress):
        self.parent = parent_main
        self.parent_in_progress = parent_in_progress
        super(CreateFilmWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.saveButton.clicked.connect(self.submit)

    def submit(self):
        list = []
        actors = []
        list.append(self.textEdit.toPlainText().split(', '))
        for elem in list:
            for s in elem:
                actors.append(s)
        WorkingBD.add_film(self.titleEdit.text(),self.boxOfficeEdit.text(),self.scoreEdit.text(),
                           self.yearEdit.text(),self.budgetEdit.text()
                           ,self.dirEdit.text(),self.scoreEdit.text(),self.compEdit.text(),actors)
        self.parent.setup_tables()
        self.hide()