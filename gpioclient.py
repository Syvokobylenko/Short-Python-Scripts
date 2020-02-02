import RPi.GPIO as GPIO
import socket


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

server = socket.socket()
server.bind(('', 2198))

server.listen(5)

switchCreate = switchObject(12)

while True: 
   data, addr = server.accept()
   print ('Got connection from' + str(addr))
   while True:
      try:
        switchCreate.switch(bool(int(data.recv(1).decode())))
      except(ConnectionResetError):
         print("Connection ended")
      except(KeyboardInterrupt):
         exit
   data.close()
