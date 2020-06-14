import socket

class Sender:
    def __init__(self):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 53210))
        client_sock.send()

