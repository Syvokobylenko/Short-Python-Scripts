import socket, time, pyautogui

posold = [0,0]

s = socket.socket()
s.connect(('127.0.0.1', 12345))

while True:
    pos = s.recv(9).decode().split("#")
    pyautogui.moveTo(int(pos[0]), int(pos[1]), 0)