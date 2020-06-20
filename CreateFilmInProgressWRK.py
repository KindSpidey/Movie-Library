from PyQt5.QtWidgets import QWidget
import CreateFilmInProgress, PyQt5, CreateFilmWRK
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from SQL import WorkingBD


class CreateFilmInProgressWorking(CreateFilmInProgress.Ui_Form, QWidget):
    def __init__(self,parent):
        self.parent = parent
        super(CreateFilmInProgressWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
        self.MakeFilmDone = CreateFilmWRK.CreateFilmWorking(parent, self)
        self.makeInProgressFilmButton.clicked.connect(CreateFilmWRK.CreateFilmWorking(parent,self).show) #сделать установку текста текущего фильма в следующем окне

    def submit(self):
        msg = QMessageBox()
        if self.actorsEdit.text() == '' or self.titleEdit.text() == '' or self.budgetEdit.text() == '' or self.dirEdit.text() == '' or self.compEdit.text() == '' or self.scrnEdit.text() == '':
            msg.setText('Заполните все поля')
            msg.exec_()
        else:
            list = []
            actors = []
            list.append(self.textEdit.toPlainText().split(', '))
            for elem in list:
                for s in elem:
                    actors.append(s)
            WorkingBD.add_filmInProgress(self.titleEdit.text(),self.budgetEdit.text(),
                               self.dirEdit.text(),self.compEdit.text(),actors)
            self.parent.setup_tables()
            self.hide()
