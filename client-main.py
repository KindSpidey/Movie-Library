from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
import sys
from TrueMainWRK import TrueMainWorking
from LoginWRK import LoginForm


class Main:
    def __init__(self):
        self.trueMainForm = TrueMainWorking

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = LoginForm()
	form.show()
	sys.exit(app.exec_())
