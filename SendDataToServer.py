import socket

class Sender:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 53210))

    def send(self):
        self.client_sock.send()

