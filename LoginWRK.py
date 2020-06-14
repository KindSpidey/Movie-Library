import sys, socket
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from Server import Server
import TrueMainWRK

class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.abd = TrueMainWRK.TrueMainWorking()
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
		sock = socket.socket()
		#sock.connect('localhost', 53210)
		msg = QMessageBox()
		#sock.send(self.lineEdit_username.text())
		#sock.send(self.lineEdit_password.text())
		#data = sock.recv(1024)
		#print(data)
		if self.lineEdit_password.text() == '1':
			self.abd.show()
			self.hide()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()
