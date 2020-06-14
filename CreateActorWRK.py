from PyQt5.QtWidgets import QWidget
import CreateActor, PyQt5
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class CreateActorWorking(CreateActor.Ui_Form, QWidget):
    def __init__(self):
        super(CreateActorWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
