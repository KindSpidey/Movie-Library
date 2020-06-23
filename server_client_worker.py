from threading import Thread

import socket as Socket
address = 'localhost'
port = 2000

dataPackageSize = 1024
dataClosingSequence = b"\r\n\r\n"
dataPackageEncoding = 'utf-8'

class ServerClientWorker(Thread):
    def __init__(self):
        super().__init__()
        self.address = address
        self.port = port
        self.socket = Socket.socket()

    def run(self):
        self.listenResponse()

    def send_data(self, data):
        self.socket.sendall(data)

    def listenResponse(self):
        responseParts = []
        while receivedData := self.getDataPackage():
            responseParts.append(receivedData.decode(dataPackageEncoding))
            if receivedData.endswith(dataClosingSequence):
                responseData = ''.join(responseParts)[:-len(dataClosingSequence)]
                self.handleResponse(responseData)
                responseParts = []

    def getDataPackage(self):
        try:
            return self.socket.recv(dataPackageSize)
        except ConnectionError:
            return 0

    def handleResponse(self, responseData: str):
        responseData = responseData.split(']')
        args = responseData[0].split(', ')
