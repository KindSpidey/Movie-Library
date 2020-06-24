import socket, threading
from SQL import WorkingBD
dataClosingSequence = b"\r\n\r\n"
dataClosingSequenceStr = "\r\n\r\n"
encoding = 'utf-8'
dataPackageSize = 1024


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", clientAddress)
        dataParts =[]
        data = ''
        while True:
            try:
                dataBytes = self.csocket.recv(dataPackageSize)
            except:
                break
            if not dataBytes:
                break
            dataParts.append(dataBytes.decode(encoding))
            if not dataBytes.endswith(dataClosingSequence):
                continue
            data = "".join(dataParts)[:-len(dataClosingSequence)]
            self.handle_data(data)
            dataParts.clear()
        print("Client at ", clientAddress, " disconnected...")

    def handle_data(self, data):
        data = data.split(']')
        args = data[0].split(', ')
        if data[1] == 'WorkingBD.add_filminplan':
            WorkingBD.add_filminplan(args[0], args[1], args[2], args[3], args[4])
        if data[1]== 'WorkingBD.get_password':
            answer = WorkingBD.get_password(args[0])
            self.send_data(str(answer))

    def send_data(self, data):
        self.csocket.sendall(data.encode(encoding)+dataClosingSequence)

LOCALHOST = "localhost"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(100)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
