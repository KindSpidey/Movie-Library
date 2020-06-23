import socket as Socket
from threading import Thread
from server_client_worker import ServerClientWorker
address = 'localhost'
port = 2000
socket = Socket.socket()

class ServerClient(Thread):
    def __init__(self):
        super().__init__()
        self.address = address
        self.port = port

    def start(self):
        socket.connect(('localhost', 2000))
        ServerClientWorker.run(ServerClientWorker())


ServerClient.start(ServerClient())