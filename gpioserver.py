import socket, time

class connection:
    def __init__(self, IP, port):
        self.IP = IP
        self.port = port
        self.startConnection()

    def startConnection(self):
        self.s = socket.socket()
        try:
            self.s.connect((self.IP, self.port))
        except(ConnectionRefusedError):
            time.sleep(2)
            self.s.close
            self.startConnection()
        except(KeyboardInterrupt):
            exit
        
    def sendData(self, state):
        try:
            self.s.send(state).encode()
        except(ConnectionResetError):
            self.s.close
            self.startConnection()
            self.sendData(state)
        except(KeyboardInterrupt):
            exit
    

data = connection("127.0.0.1", 2198)

while True:
   data.sendData(input("Type 1 or 0 to use switch: "))