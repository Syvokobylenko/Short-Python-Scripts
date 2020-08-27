import pygetwindow, time, pyautogui
def init():
    GF_Client = pygetwindow.getWindowsWithTitle('Gameforge Client')[0]
    GF_Client.restore()
    GF_Client.resizeTo(100, 100)
    GF_Client.moveTo(100, 100)

def login(login,password):
    pyautogui.click(470,399)
    pyautogui.typewrite(str(login))
    pyautogui.press('enter')
    pyautogui.typewrite(str(password))
    pyautogui.press('enter')

def logout():
    pyautogui.click(881,130)
    time.sleep(0.3)
    pyautogui.click(881,230)
    time.sleep(0.3)

def login_wrapper(login_list,password):
    init()
    for login in login_list:
        login(login,password)
        input_temp = input('Any key = next, "0" = repeat last login, "exit" = quit: ')
        while input_temp == "0":
            login(login,password)
            input_temp = input('Any key = next, "0" = repeat last login, "exit" = quit: ')
        if input_temp == "exit":
            return
        logout()
