import zmq
import time
from threading import Thread


def out(MB,UB,s):
        s=s.decode()
        index = s.rindex('|users|')
        dialog=s[:index]
        users=s[index+7:]
        try:
                MB.SetValue(dialog)
                UB.SetValue(users)
        except:
                print("Error: Can't find the WindowOutPut")
                
                
class Contact(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.done=False
    def run(self):
        while not self.done:
            mes='n '+self.name
            try:
                self.sock.send(mes.encode())
            except:
                print("Error: Can't send message to the server, when reconnect")
            try:
                out(self.MB, self.UB, self.sock.recv())
            except:    
                print("Error: Can't get messege from the server, when reconnect")
            time.sleep(0.5)
    def options(self, name, socket, MB, UB):
        self.name=name
        self.sock=socket        
        self.MB=MB
        self.UB=UB 

class Client():
    def __init__(self):
        self.name = ""
        self.address = ""
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.sendSocket = self.context.socket(zmq.REQ)
        self.contact=Contact()
    def set(self,MB,UB):
        self.MB=MB
        self.UB=UB        
    def start(self,address,port,name):
        self.name=name
        self.contact.done=False
        print("Connecting to hello world server")
        self.socket.connect("tcp://"+address+":"+port)
        self.sendSocket.connect("tcp://"+self.address+":"+port)
        self.contact=Contact()
        self.contact.options(self.name,self.socket,self.MB,self.UB)
        self.contact.start()
    def send(self,s):
        letter="l "+self.name+": "+s
        self.sendSocket.send(str.encode(letter))
        out(self.MB, self.UB, self.sendSocket.recv())
    def done(self):
        self.contact.done=True
    def end(self):
        try:
            self.sendSocket.send(str.encode('e '+self.name))
        except:
            pass   
