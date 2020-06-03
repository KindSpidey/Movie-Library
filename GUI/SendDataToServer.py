import socket

class Sender:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 53210))

    def send(self):

    print('Received', repr(data.decode('utf-8')))