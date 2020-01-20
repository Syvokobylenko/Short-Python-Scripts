import socket, time, pyautogui

def GetMousePos():
    x, y = pyautogui.position()
    return str(x) + "#" + str(y)

s = socket.socket()
s.bind(('', 12345))

s.listen(5)

while True: 
   c, addr = s.accept()
   print ('Got connection from' + str(addr))
   while True:
      try:
         c.send(str(GetMousePos()).encode())
      except(ConnectionResetError):
         print("Connection ended")
         break
      except(KeyboardInterrupt):
         exit
      time.sleep(1)
   c.close()