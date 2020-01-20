import socket, time, pyautogui

def GetMousePos():
    x, y = pyautogui.position()
    return x, y

s = socket.socket()
s.bind(('', 8080))

s.listen(5)

while True: 
   c, addr = s.accept()      
   print ('Got connection from' + str(addr))
   while True:
      try:
         c.send(str(GetMousePos()).encode())
      except:
         break
      time.sleep(1)
   c.close()