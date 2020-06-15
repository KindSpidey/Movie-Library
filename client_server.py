import socket


class ClientServer:
    def __init__(self):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sock.connect(('127.0.0.1', 53210))
        self.data = bytes

    def receive_data(self):
        self.data = self.client_sock.recv(1024)
        return self.data

    def send_data(self, some_data):
        self.client_sock.sendall(some_data)

    def stop(self):
        self.client_sock.close()


abc = ClientServer()
abc.send_data(b'FUCK YOU MCcRUSSIAN')

print(abc.receive_data())