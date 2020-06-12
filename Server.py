import socket
from SQL import WorkingBD

class TCPServer():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', 53210))
    serv_sock.listen(1000)

    sqlworker = WorkingBD()

    while True:
        print('Server ONLINE')
        client_sock, client_addr = serv_sock.accept()
        print('Connected by', client_addr)

        while True:
            # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
            data = client_sock.recv(1024)
            if not data:
                print('# Клиент отключился')
                break
            if data == b'Hello, world':
                client_sock.sendall(b'I got')
        client_sock.close()