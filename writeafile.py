import time, pyautogui
from pyautogui import write as writepy
from pyautogui import press as presspy
time.sleep(5)
pyautogui.write("f = open('boot.py', 'w')")
pyautogui.press('enter')
file1 = open('copy.txt', 'r')
f = file1.readlines()
for line in f:
 pyautogui.write("f.write('" + line.rstrip('\n') + "\\n')"),
 pyautogui.press('enter')
