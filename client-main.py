
from PyQt5.QtWidgets import QWidget, QApplication
import sys, client_server
from LoginWRK import LoginForm
from client_server import ClientServer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_server = ClientServer()
    form = LoginForm(client_server)
    form.show()
    sys.exit(app.exec_())
