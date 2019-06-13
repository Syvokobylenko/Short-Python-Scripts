from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import pyautogui
import time
def GetMousePos():
    x, y = pyautogui.position()
    return x, y


class mousegui:
    def __init__(self, master):
        self.master = master
        master.title("Mouse Position")
        self.PosLabel = Label(root, text=GetMousePos())
        self.PosLabel.grid(row=0, column=0)
        self.add_button = Button(master, text="Confirm", command=self.Confirm)
        self.add_button.grid(row=0, column=1)
        self.refresh()
    def refresh(self):
        self.PosLabel.configure(text=GetMousePos())
        self.PosLabel.after(1000, self.refresh)
    def Confirm(self):
        root.destroy()

root = Tk()
my_gui = mousegui(root)
root.mainloop()