import time, pyautogui
from pyautogui import write as writepy
from pyautogui import press as presspy
time.sleep(5)
pyautogui.write("import os")
pyautogui.press('enter')
pyautogui.write("os.remove('boot.py')")
pyautogui.press('enter')
pyautogui.write("f = open('boot.py', 'x')")
pyautogui.press('enter')
pyautogui.write("f.close()")
pyautogui.press('enter')
pyautogui.write("f = open('boot.py', 'w')")
pyautogui.press('enter')
file1 = open('copy.txt', 'r')
f = file1.readlines()
for line in f:
 pyautogui.write("f.write(r'" + line.rstrip('\n') + r"' + '\n')")
 #for i in range(1,10):
 # pyautogui.press('backspace')
 #pyautogui.write(line.rstrip('\n'))
 pyautogui.press('enter')
pyautogui.write("f.close()")
pyautogui.press('enter')

