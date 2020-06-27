import time
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
import TrueMainWRK

class LoginForm(QWidget):
	def __init__(self, parent_server):
		super().__init__()
		self.server = parent_server
		self.MainWindow = TrueMainWRK.TrueMainWorking(self.server)
		self.setWindowTitle('Login Form')
		self.resize(500, 120)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Введите ваш логин')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Введите пароль')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		self.button_login = QPushButton('Login')
		self.button_login.clicked.connect(self.check_password)
		layout.addWidget(self.button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()
		self.server.send(self.lineEdit_username.text()+']WorkingBD.get_password')
		time.sleep(0.1)
		if self.lineEdit_password.text() == self.server.answer:
			print(self.server.answer)
			self.MainWindow.show()
			self.hide()
		else:
			msg.setText('Неправильный логин или пароль')
			msg.exec_()
