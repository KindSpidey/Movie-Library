from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSignal
import profileActor, PyQt5


class profileActorWorking(profileActor.Ui_Form, QWidget):
    def __init__(self):
        super(profileActorWorking, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.setupUi(self)
