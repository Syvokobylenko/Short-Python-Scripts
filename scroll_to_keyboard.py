import keyboard
from pynput import mouse

global key
key = 0

def on_scroll(x, y, dx, dy):
    global key
    key_list = ['7','8','9','0']
    keyboard.send(key_list[key])
    key+=1
    if key == 4:
        key = 0

listener = mouse.Listener(on_scroll=on_scroll)
listener.start()
