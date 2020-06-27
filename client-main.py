
from PyQt5.QtWidgets import QApplication
import sys
from LoginWRK import LoginForm
from client_server import ClientServer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_server = ClientServer()
    form = LoginForm(client_server)
    form.show()
    sys.exit(app.exec_())
