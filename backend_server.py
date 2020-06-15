import socket, threading, sys
from SQL import WorkingBD
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtNetwork import QHostAddress, QTcpServer


class Server:
    def __init__(self):
        super().__init__()
        self.startThread = threading.Thread(target=self.listen_clients)
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serv_sock.bind(('', 53210))
        self.serv_sock.listen(10)
        self.client_socket, self.client_addr = self.serv_sock.accept()

    def start(self):
        self.startThread.start()

    def listen_clients(self):
        print('SERVER ONLINE')
        while True:
            print('Connected by', self.client_addr)
            while True:
                data = self.client_socket.recv(1024)
                a = (data.decode('utf-8')).lower()
                print(a)
                if not data:
                    break
                self.client_socket.sendall(a.encode('utf-8'))

    def stop(self):
        print("Server has stopped")
        self.client_socket.close()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    server = Server()
    server.start()
    # server.sessionOpened()
    # sys.exit(server.exec_())
