import socket as Socket
from threading import Thread
from server_back_handler import ServerBackHandler
from SQL import WorkingBD
address = 'localhost'
port = 2000
dataClosingSequence = b"\r\n\r\n"
encoding = "utf-8"
dataPackageSize = 1024


class Server(Thread):
    def __init__(self):
        super().__init__()
        self.socket = Socket.socket()
        self.socket.bind((address, port))

        self.__isWorking = False
        self.clients = {}

    def run(self):
        self.__isWorking = True


    def listenClients(self, connection, clientAddress):
        dataParts = []
        while 1:
            try:
                dataBytes = connection.recv(dataPackageSize)
            except ConnectionError:
                break
            if not dataBytes:
                break
            dataParts.append(dataBytes.decode(encoding))
            if not dataBytes.endswith(dataClosingSequence):
                continue
            data = "".join(dataParts)[:-len(dataClosingSequence)]
            ServerBackHandler.handleResponse(data)
            dataParts.clear()
            print(len(data), data.encode(encoding))
        print(f"{clientAddress} has disconnected")

    def startServer(self):
        socket = Socket.socket()
        socket.bind((address, port))
        socket.listen()

        while True:
            print('sd')
            try:
                connection, clientAddress = socket.accept()
            except OSError:
                break
            print(f"{clientAddress} has connected")
            self.listenClients(connection, clientAddress)

        socket.close()
        print("Server has stopped")

