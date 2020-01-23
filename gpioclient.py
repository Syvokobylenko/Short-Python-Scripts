import RPi.GPIO as GPIO
import socket, time


class switchObject():
    def __init__(self, channel):
        self.channel = channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)

    def switch(self, state):
        if state:
            GPIO.output(self.channel, GPIO.HIGH)
        else:
            GPIO.output(self.channel, GPIO.LOW)

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
    

data = connection("127.0.0.1", 12345, 1)

switchCreate = switchObject(21)

while True:
    switchCreate.switch(bool(int(data.recieveData())))