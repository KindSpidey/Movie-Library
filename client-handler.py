from threading import Thread

str ='as, sa, sas, sasa, as, sa, sq, qs'
list =[]
result = []
list.append(str.split(', '))
for elem in list:
    for s in elem:
        result.append(s)
print(list)
print(result)


#class ClientHandler(Thread):
    #def __init__(self):
        #self.