import time
import zmq
import socket as sock


context = zmq.Context()
socket = context.socket(zmq.REP)
ip=input('IP: ')
port="5555"
socket.bind('tcp://'+ip+':'+port)
print("Start server on "+ip+":"+port)
users=[]
chat=""
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    #  Do some 'work'
    #time.sleep(1)
    mes = message.decode()
    if mes[0]=='n':
        if mes[1:] not in users:
            users.append(mes[1:])
            print(mes[1:],"comes!")
        usersList=''
        for user in users:
            usersList+=user+"\n"
        line=chat+"|users|"+usersList
    elif mes[0]=='l':
        chat+=mes[1:]+"\n"
        usersList=''
        for user in users:
            usersList+=user+"\n"
        line=chat+"|users|"+usersList
    elif mes[0]=='e':
        name=mes[1:]
        if name in users:
            users.pop(users.index(name))
            print(name+" left")
    else:
        print("Strange MES!")
        line="close for you"
    #  Send reply back to client
    socket.send_string(line.rstrip("\n"))
input("Press ENTER...")
