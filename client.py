import socket, time, pyautogui

class connection:
    def __init__(self, IP, port, lenght):
        self.IP = IP
        self.port = port
        self.lenght = lenght
        self.startConnection()

    def startConnection(self):
        self.s = socket.socket()
        try:
            self.s.connect((self.IP, self.port))
        except(ConnectionRefusedError):
            time.sleep(5)
            self.s.close
            self.startConnection()
        except(KeyboardInterrupt):
            exit
        
    def recieveData(self):
        try:
            return self.s.recv(self.lenght).decode()
        except(ConnectionResetError):
            self.s.close
            self.startConnection()
            return self.recieveData()
        except(KeyboardInterrupt):
            exit
            
data = connection("127.0.0.1", 12345, 9)

while True:
    pos = data.recieveData().split("#")
    pyautogui.moveTo(int(pos[0]), int(pos[1]), 0)