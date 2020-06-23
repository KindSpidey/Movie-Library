import socket as Socket
from server_back_worker import Server
from SQL import WorkingBD

address = "localhost"
port = 2000
dataPackageSize = 1024
dataClosingSequence = b"\r\n\r\n"
encoding = "utf-8"

if __name__ == '__main__':
    Server.startServer()
