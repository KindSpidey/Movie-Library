import socket, threading, sys
from SQL import WorkingBD
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtNetwork import QHostAddress, QTcpServer

class Server():
    def __init__(self):
        super().__init__()
        self.tcpServer = None
    def sessionOpened(self):
        self.tcpServer = QTcpServer(self)
        PORT = 53210
        address = QHostAddress('127.0.0.1')
        if not self.tcpServer.listen(address, PORT):
            print("cant listen!")
            self.close()
            return
        self.tcpServer.newConnection.connect(self.dealCommunication)

    def __init__(self, address="", port=53210):
        self.socket = socket.socket()
        self.socket.bind((address, port))
        self.__isWorking = False
        self.clients = {}


    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', 53210))
    serv_sock.listen(1000)

    sqlworker = WorkingBD()

    while True:
        print('Server ONLINE')
        client_sock, client_addr = serv_sock.accept()
        print('Connected by', client_addr)

        while True:
            # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
            data = client_sock.recv(1024)
            if not data:
                print('# Клиент отключился')
                break
            if data == b'Hello, world':
                client_sock.sendall(b'I got')
        client_sock.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    server = Server()
    server.sessionOpened()
    sys.exit(server.exec_())