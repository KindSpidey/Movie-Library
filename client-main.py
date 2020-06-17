from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
import sys#, client_server
from TrueMainWRK import TrueMainWorking
from LoginWRK import LoginForm


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    #clientServer = client_server.ClientServer()
    sys.exit(app.exec_())
