import time, pyautogui
time.sleep(5)
filename = "wifi.ini"
pyautogui.write("import os")
pyautogui.press('enter')
pyautogui.write("os.remove('" + filename + "')")
pyautogui.press('enter')
pyautogui.write("f = open('" + filename + "', 'x')")
pyautogui.press('enter')
pyautogui.write("f.close()")
pyautogui.press('enter')
pyautogui.write("f = open('" + filename + "', 'w')")
pyautogui.press('enter')
file1 = open(filename, 'r')
f = file1.read()
pyautogui.write("f.write(" + repr(f) + ")")
pyautogui.press('enter')
pyautogui.write("f.close()")
pyautogui.press('enter')