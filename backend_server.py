import socket, threading, json
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
        if data[1]== 'WorkingBD.get_password':
            answer = WorkingBD.get_password(args[0])
            self.send_data(str(answer))
        if data[1] == 'WorkingBD.add_filminplan':
            WorkingBD.add_filminplan(args[0], args[1], args[2], args[3], args[4])
        if data[1] == 'WorkingBD.remove_filminprogress':
            WorkingBD.remove_filminprogress(args[0])
        if data[1]== 'WorkingBD.remove_filminplan':
            WorkingBD.remove_filminplan(args[0])
        if data[1]== 'WorkingBD.remove_film_by_title':
            WorkingBD.remove_film_by_title(args[0])
        if data[1] == 'WorkingBD.remove_screenwriter_by_name':
            WorkingBD.remove_screenwriter_by_name(args[0])
        if data[1] == 'WorkingBD.remove_composer_by_name':
            WorkingBD.remove_composer_by_name(args[0])
        if data[1] == 'WorkingBD.remove_director_by_name':
            WorkingBD.remove_director_by_name(args[0])
        if data[1] == 'WorkingBD.remove_actor_by_name':
            WorkingBD.remove_actor_by_name(args[0])
        if data[1] == 'WorkingBD.get_film_by_title':
            answer = WorkingBD.get_film_by_title(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_film_in_progress_by_title':
            answer = WorkingBD.get_film_in_progress_by_title(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_film_in_plan':
            answer = WorkingBD.get_film_in_plan(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_actor_by_name':
            answer = WorkingBD.get_actor_by_name(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_director_by_name':
            answer = WorkingBD.get_director_by_name(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_composer_by_name':
            answer = WorkingBD.get_composer_by_name(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_screenwriter_by_name':
            answer = WorkingBD.get_screenwriter_by_name(args[0])
            if len(answer)!=0:
                answer = answer[0][0]
                self.send_data(str(answer))
            else:
                self.send_data('')
        if data[1] == 'WorkingBD.get_all_films':
            self.send_data(json.dumps(WorkingBD.get_all_films(WorkingBD)))
        if data[1] == 'WorkingBD.get_all_films_in_progress':
            self.send_data(json.dumps(WorkingBD.get_all_films_in_progress(WorkingBD)))
        if data[1] == 'WorkingBD.get_all_films_in_plan':
            self.send_data(json.dumps(WorkingBD.get_all_films_in_plan(WorkingBD)))
        if data[1] == 'WorkingBD.get_all_actors':
            self.send_data(json.dumps(WorkingBD.get_all_actors(WorkingBD)))
        if data[1] == 'WorkingBD.get_all_persondirector':
            self.send_data(json.dumps(WorkingBD.get_all_person(WorkingBD, 'director')))
        if data[1] == 'WorkingBD.get_all_personcomposer':
            self.send_data(json.dumps(WorkingBD.get_all_person(WorkingBD, 'composer')))
        if data[1] == 'WorkingBD.get_all_personscreenwriter':
            self.send_data(json.dumps(WorkingBD.get_all_person(WorkingBD, 'screenwriter')))
        if data[1] == 'WorkingBD.get_actor_by_name_for_profile':
            self.send_data(json.dumps(WorkingBD.get_actor_by_name_for_profile(data[0])))
        if data[1] == 'WorkingBD.update_actor':
            WorkingBD.update_actor(args[0], args[1], args[2], args[3], args[4])


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
