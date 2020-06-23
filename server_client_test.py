import socket as Socket
from server_client_worker import ServerClientWorker
address = 'localhost'
port = 2000
socket = Socket.socket()

class ServerClient:
    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port

    def start(self):
        socket.connect(('localhost', 2000))

    def send_data(data):
        socket.sendall(data)