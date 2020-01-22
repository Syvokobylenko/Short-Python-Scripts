import socket

s = socket.socket()
s.bind(('', 12345))

s.listen(5)

while True: 
   c, addr = s.accept()
   print ('Got connection from' + str(addr))
   while True:
      try:
         c.send(input("Type 1 or 0 to use switch: ").encode())
      except(ConnectionResetError):
         print("Connection ended")
      except(KeyboardInterrupt):
         exit
   c.close()