from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics

dat = []


def gui():
    root = Tk()
    screen_width = 268
    screen_height = 123
    root.geometry(f"{screen_width}x{screen_height}+"
                  f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")
    root.resizable(False, False)
    root.title("IRAS SCHEDULER - By Muyeed")

    ul = ttk.Label(root, text="ID" + " " * 13 + ":")
    ul.place(x=10, y=10)
    ui = ttk.Entry(root)
    ui.place(x=88, y=10)

    pl = ttk.Label(root, text="Password :")
    pl.place(x=10, y=45)
    pi = ttk.Entry(root, show="*")
    pi.place(x=88, y=45)

    def click():
        dat.append(str(ui.get()))
        dat.append(str(pi.get()))
        root.destroy()

    lob = ttk.Button(root, text="Login", command=click)
    lob.place(x=156, y=80)

    root.mainloop()
