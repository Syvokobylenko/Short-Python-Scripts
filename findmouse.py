import tkinter
import pyautogui

class mousegui:
    def __init__(self):
        self.master = tkinter.Tk()
        self.master.title("Mouse Position")
        self.PosLabel = tkinter.Label(self.master, text=pyautogui.position())
        self.PosLabel.grid(row=0, column=0)
        self.add_button = tkinter.Button(self.master, text="Exit", command=self.exit)
        self.add_button.grid(row=0, column=1)
        self.refresh()
        self.master.mainloop()

    def refresh(self):
        self.PosLabel.configure(text=pyautogui.position())
        self.PosLabel.after(1000, self.refresh)
    def exit(self):
        self.master.destroy()

mousegui()