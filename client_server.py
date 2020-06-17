import socket, threading


class ClientServer:
    def __init__(self):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sock.connect(('127.0.0.1', 53210))
        self.data = bytes
        self.serv_thread = threading.Thread(target=self.listen_server)
        self.serv_thread.start()
    def listen_server(self):
        while True:
            print('LISTENING')
            while True:
                self.data = self.client_sock.recv(1024)
                print(self.data)

    def receive_data(self):
        self.data = self.client_sock.recv(1024)
        return self.data

    def send_data(self, some_data):
        self.client_sock.sendall(some_data)

    def stop(self):
        self.client_sock.close()

a = ClientServer()
a.send_data(b'URA')