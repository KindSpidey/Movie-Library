from PyQt5.QtWidgets import QWidget
import CreatePerson, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class CreatePersonWorking(CreatePerson.Ui_Form, QWidget):
    def __init__(self):
        super(CreatePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)