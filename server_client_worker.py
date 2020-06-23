import server_client_test
import socket as Socket
from server_client_test import address, port, ServerClient


class ServerClientWorker:
    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port
        self.socket = Socket.socket()
    def send_data(self, data):
        server_client_test.ServerClient.send_data(data)