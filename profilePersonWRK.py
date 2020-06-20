from PyQt5.QtWidgets import QWidget
import profilePerson, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal



class profilePersonWorking(profilePerson.Ui_Form, QWidget):
    def __init__(self, parent):
        self.parent = parent
        super(profilePersonWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)