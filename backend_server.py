import socket, threading, sys#, client-handler
from SQL import WorkingBD
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtNetwork import QHostAddress, QTcpServer


class Server:
    def __init__(self):
        self.__isWorking = False
        super().__init__()
        self.startThread = threading.Thread(target=self.listen_clients)
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serv_sock.bind(('', 53210))
        self.serv_sock.listen(10)
        self.client_socket, self.client_addr = self.serv_sock.accept()
        self.startThread.start()


    def listen_clients(self):
        print('SERVER ONLINE')
        while True:
            try:
                client_socket, client_connection = self.serv_sock.accept()
                FUCKINGTHREAD = threading.Thread(target=self.serveClient(client_socket,client_connection))
                FUCKINGTHREAD.start()
            except:
                print('НЕ ВЫШЛО ПОЛУЧИТЬ КЛИЕНТА')
            print('Connected by', self.client_addr)
            while True:
                try:
                    data = self.client_socket.recv(1024)
                    s = data.decode('utf-8')
                    s+='I AM FUCKING DONE'
                    self.client_socket.sendall(s.encode('utf-8'))
                except:
                    pass

                #if data!='':
                #a = WorkingBD.get_password(s)
    def serveClient(self, client, connection):
        ip = connection[0]
        port = connection[1]
        threading._start_new_thread((client, ip))
        while True:
            data = client.recv(1024)
            client.sendall(b'MCCRUSSIAN FUCK YOU!')
    def waitClientConnection(self):
        try:
            clientInfo = self.serv_sock.accept()
            self.parseClietn(clientInfo)
        except OSError:
            if self.__isWorking:
                raise

    def stop(self):
        print("Server has stopped")
        self.client_socket.close()

    def parseClietn(self, clientInfo):
        connection = clientInfo[0]
        rawAddress = clientInfo[1]
        ipAddress = rawAddress[0]
        port = rawAddress[1]
        fullAddress = f"{ipAddress}:{port}"
        print(fullAddress)
if __name__ == '__main__':
    server = Server()
    server.listen_clients()

