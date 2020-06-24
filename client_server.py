import socket
from threading import Thread
SERVER = "localhost"
PORT = 8080
dataClosingSequence = b"\r\n\r\n"
encoding = 'utf-8'
dataPackageSize = 1024


class ClientServer(Thread):
    def __init__(self):
        super().__init__()
        self.answer = 'incorrect password'
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((SERVER, PORT))
        self.client_listen_thread = Thread(target=self.getDataPackage)
        self.client_listen_thread.start()

    def getDataPackage(self):
        dataParts = []
        data =''
        while True:
            try:
                dataBytes = self.client.recv(dataPackageSize)
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

    def handle_data(self, data):
        self.answer = data
    def stop(self):
        self.client.close()
    def send(self, data):
        self.client.sendall(data.encode(encoding)+dataClosingSequence)


#a = ClientServer()
#a.send('Daniil Pugavko]WorkingBD.get_password')
