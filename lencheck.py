import socket, time, pyautogui

def GetMousePos():
    x, y = pyautogui.position()
    x = str(x).zfill(4)
    y = str(y).zfill(4)
    return x + "#" + y

while True: 
   print(GetMousePos().encode())
   time.sleep(1)