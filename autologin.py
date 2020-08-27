import pygetwindow, time, pyautogui
def init():
    GF_Client = pygetwindow.getWindowsWithTitle('Gameforge Client')[0]
    GF_Client.resizeTo(100, 100)
    GF_Client.moveTo(100, 100)

def login(login,password):
    init()
    pyautogui.click(470,399)
    pyautogui.typewrite(str(login))
    pyautogui.press('enter')
    pyautogui.typewrite(str(password))
    pyautogui.press('enter')

def logout():
    pyautogui.click(881,130)
    time.sleep(0.3)
    pyautogui.click(881,230)