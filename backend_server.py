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
        try:
            data = json.loads(data)
            self.special_handle(data)
            return
        except:
            pass
        data = data.split(']')
        args = data[0].split(', ')
        if data[1]== 'WorkingBD.get_password':
            answer = WorkingBD.get_password(args[0])
            self.send_data(str(answer))
            return
        if data[1] == 'WorkingBD.add_filminplan':
            WorkingBD.add_filminplan(args[0], args[1], args[2], args[3], args[4])
            return
        if data[1] == 'WorkingBD.remove_filminprogress':
            WorkingBD.remove_filminprogress(args[0])
            return
        if data[1]== 'WorkingBD.remove_filminplan':
            WorkingBD.remove_filminplan(args[0])
            return
        if data[1]== 'WorkingBD.remove_film_by_title':
            WorkingBD.remove_film_by_title(args[0])
            return
        if data[1] == 'WorkingBD.remove_screenwriter_by_name':
            WorkingBD.remove_screenwriter_by_name(args[0])
            return
        if data[1] == 'WorkingBD.remove_composer_by_name':
            WorkingBD.remove_composer_by_name(args[0])
            return
        if data[1] == 'WorkingBD.remove_director_by_name':
            WorkingBD.remove_director_by_name(args[0])
            return
        if data[1] == 'WorkingBD.remove_actor_by_name':
            WorkingBD.remove_actor_by_name(args[0])
            return
        if data[1] == 'WorkingBD.get_film_by_title':
            answer = WorkingBD.get_film_by_title(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_film_in_progress_by_title':
            answer = WorkingBD.get_film_in_progress_by_title(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_film_in_plan':
            answer = WorkingBD.get_film_in_plan(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_actor_by_name':
            answer = WorkingBD.get_actor_by_name(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_director_by_name':
            answer = WorkingBD.get_director_by_name(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_composer_by_name':
            answer = WorkingBD.get_composer_by_name(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_screenwriter_by_name':
            answer = WorkingBD.get_screenwriter_by_name(args[0])
            if len(answer)!=0:
                self.send_data(json.dumps(answer))
            else:
                self.send_data('')
            return
        if data[1] == 'WorkingBD.get_all_films':
            self.send_data(json.dumps(WorkingBD.get_all_films(WorkingBD)))
            return
        if data[1] == 'WorkingBD.get_all_films_in_progress':
            self.send_data(json.dumps(WorkingBD.get_all_films_in_progress(WorkingBD)))
            return
        if data[1] == 'WorkingBD.get_all_films_in_plan':
            self.send_data(json.dumps(WorkingBD.get_all_films_in_plan(WorkingBD)))
            return
        if data[1] == 'WorkingBD.get_all_actors':
            self.send_data(json.dumps(WorkingBD.get_all_actors(WorkingBD)))
            return
        if data[1] == 'WorkingBD.get_all_persondirector':
            self.send_data(json.dumps(WorkingBD.get_all_person(WorkingBD, 'director')))
            return
        if data[1] == 'WorkingBD.get_all_personcomposer':
            self.send_data(json.dumps(WorkingBD.get_all_person(WorkingBD, 'composer')))
            return
        if data[1] == 'WorkingBD.get_all_personscreenwriter':
            self.send_data(json.dumps(WorkingBD.get_all_person(WorkingBD, 'screenwriter')))
            return
        if data[1] == 'WorkingBD.get_actor_by_name_for_profile':
            self.send_data(json.dumps(WorkingBD.get_actor_by_name_for_profile(data[0])))
            return
        if data[1] == 'WorkingBD.update_actor':
            WorkingBD.update_actor(args[0], args[1], args[2], args[3], args[4])
            return
        if data[1] == 'WorkingBD.connect_film_and_actor':
            try:
                WorkingBD.connect_film_and_actor(args[0], args[1])
            except:
                pass
            return
        if data[1] == 'WorkingBD.add_actor_in_consist_film':
            try:
                WorkingBD.add_actor_in_consist_film(args[0], args[1])
            except:
                pass
            return
        if data[1] == 'WorkingBD.add_actor':
            WorkingBD.add_actor(args[0], args[1], args[2], args[3], args[4])
            return
        if data[1] == 'WorkingBD.get_films_title_by_actor':
            self.send_data(json.dumps(WorkingBD.get_films_title_by_actor(args[0])))
            return
        if data[1] == 'WorkingBD.update_filminplan':
            WorkingBD.update_filminplan(args[0], args[1], args[2], args[3], args[4])
            return
        if data[1] == 'WorkingBD.add_filminplan':
            WorkingBD.add_filminplan(args[0], args[1], args[2], args[3], args[4])
            return
        if data[1] == 'WorkingBD.get_actors_by_filminprogress':
            self.send_data(json.dumps(WorkingBD.get_actors_by_filminprogress(args[0])))
            return
        if data[1] == 'WorkingBD.get_actors_by_film':
            self.send_data(json.dumps(WorkingBD.get_actors_by_film(args[0])))
            return
        if data[1] == 'WorkingBD.get_salary_by_film':
            self.send_data(json.dumps(WorkingBD.get_salary_by_film(args[0])))
            return
        if data[1] == 'WorkingBD.connect_salary_and_person':
            WorkingBD.connect_salary_and_person(args[0], args[1], args[2], args[3])
            return
        if data[1] == 'WorkingBD.update_salary_when_created':
            WorkingBD.update_salary_when_created(args[0], args[1], args[2], args[3])
            return
        if data[1] == 'WorkingBD.add_director':
            WorkingBD.add_director(args[0], args[1], args[2])
            return
        if data[1] == 'WorkingBD.add_composer':
            WorkingBD.add_composer(args[0], args[1], args[2])
            return
        if data[1] == 'WorkingBD.add_screenwriter':
            WorkingBD.add_screenwriter(args[0], args[1], args[2])
            return
        if data[1] == 'WorkingBD.update_director':
            WorkingBD.update_director(args[0], args[1], args[2])
            return
        if data[1] == 'WorkingBD.update_composer':
            WorkingBD.update_composer(args[0], args[1], args[2])
            return
        if data[1] == 'WorkingBD.update_screenwriter':
            WorkingBD.update_screenwriter(args[0], args[1], args[2])
            return
        if data[1] == 'WorkingBD.get_films_title_by_person':
            self.send_data(json.dumps(WorkingBD.get_films_title_by_person(args[0], args[1])))

    def special_handle(self, data):
        params_of_film = data['params']
        args = params_of_film.split(', ')
        actors = data['actors']
        command = data['command']
        if command == 'WorkingBD.add_film':
            WorkingBD.add_film(args[0], args[1], args[2], args[3], args[4], args[5], args[6],args[7], actors)
            return
        if command == 'WorkingBD.update_film':
            WorkingBD.update_film(args[0], args[1], args[2], args[4], args[3], args[5], args[6], args[7],actors)
            return
        if command == 'WorkingBD.add_filmInProgress':
            WorkingBD.add_filmInProgress(args[0], args[1], args[2], args[3], args[4], actors)
            return
        if command == 'WorkingBD.update_filminprogress':
            WorkingBD.update_filminprogress(args[0], args[1], args[2], args[3], args[4], actors)
            return


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
