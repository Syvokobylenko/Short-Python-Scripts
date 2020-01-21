import socket, time, pyautogui

posold = [0,0]

s = socket.socket()
s.connect(('127.0.0.1', 12345))

while True:
    pos = s.recv(9).decode().split("#")
    pos = [int(i) for i in pos]
    if pos != posold:
        pyautogui.moveTo(pos[0], pos[1], 0)
        posold = pos.copy
    time.sleep(1)