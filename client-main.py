from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
import sys
from TrueMainWRK import TrueMainWorking


class Main:
    def __init__(self):
        self.trueMainForm = TrueMainWorking

if __name__ == '__main__':
	app = QApplication([])
	application = TrueMainWorking()
	application.show()
	sys.exit(app.exec())