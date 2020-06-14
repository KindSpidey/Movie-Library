import socket, threading, sys
from SQL import WorkingBD
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtNetwork import QHostAddress, QTcpServer

class Server():
    def __init__(self,address="", port=53210):
        super().__init__()
        self.tcpServer = None
        self.socket = socket.socket()
        self.socket.bind((address, port))
        self.socket.listen(100)
        self.__isWorking = False
        self.clients = {}
    def start(self):
        threading.Thread(target=self.listen_clients)
        print('SERVER WORKS')
        return self

    def listen_clients(self):
        self.conn, self.adr = self.socket.accept()
        while True:
            self.socket.listen(1000)
            data = self.conn.recv(1024)
            if not data:
                break
            self.conn.send(data.upper())

    def sessionOpened(self):
        self.tcpServer = QTcpServer(self)
        PORT = 53210
        address = QHostAddress('127.0.0.1')
        if not self.tcpServer.listen(address, PORT):
            print("cant listen!")
            self.close()
            return
        self.tcpServer.newConnection.connect(self.dealCommunication)

    def stop(self):
        self.__isWorking = False
        self.socket.close()
        for client in self.clients.values():
            client.pendedToDisconnect = True
            client.disconnect()
        print("Server has stopped")

if __name__ == '__main__':
    #app = QApplication(sys.argv)
    server = Server()
    server.start()
    #server.sessionOpened()
    #sys.exit(server.exec_())