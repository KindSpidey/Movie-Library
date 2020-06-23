import socket
import threading
SERVER = "localhost"
PORT = 8080
endsequence = b"\r\n\r\n"


class ClientServer:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((SERVER, PORT))


    def getDataPackage(self):
        try:
            recvData = self.client.recv(1024)
            return recvData
        except ConnectionError:
            return 0
    def listen_server(self):
        while in_data := self.getDataPackage():
            print(in_data)

    def stop(self):
        self.client.close()
    def send(self, data):
        self.client.sendall(data)
        data = ''
        self.listen_server()

a = ClientServer()
a.send(b'fuck')
a.listen_server()