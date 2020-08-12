import time, win32clipboard, pywintypes
id_stack = []
values_stack = ""
while True:
    try:
        time.sleep(0.1)
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        item_id = data.split("#")[0]
        if item_id not in id_stack:
            id_stack.append(item_id)
            values_stack += data + "\n"
            print(data)
    except(pywintypes.error):
        print("Clippoard Busy")
    except(KeyboardInterrupt):
        with open("file.txt","x") as txt:
            pass
        with open("file.txt","w") as txt:
            txt.write(values_stack)
        break
