import time, pyautogui
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
write_string = "f.write(r'"
for line in f:
 write_string += repr(line)
pyautogui.write("f.write(r'" + write_string + "')")
pyautogui.press('enter')
pyautogui.write("f.close()")
pyautogui.press('enter')

