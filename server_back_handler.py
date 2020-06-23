from threading import Thread
import socket as Socket
from  SQL import WorkingBD
dataPackageSize = 1024
dataPackageEncoding = 'utf-8'
dataClosingSequence = b"\r\n\r\n"


class ServerBackHandler(Thread):
    def __init__(self):
        super().__init__()
        self.socket = Socket.socket()
    def run(self):
        self.listenResponse()


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
        if responseData[1] == 'WorkingBD.add_filminplan':
            WorkingBD.add_filminplan(args[0], args[1], args[2], args[3], args[4])

    def send_data(self, data):
        self.socket.sendall(data)