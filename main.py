# data.ini and user.ini creating if they does not exist in the directory
try:
    open(fr"data.ini", "r", encoding="utf-8").read()
except: open(fr"data.ini", "w", encoding="utf-8").write("")

try:
    open(fr"user.ini", "r", encoding="utf-8").read()
except: open(fr"user.ini", "w", encoding="utf-8").write("")

# modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from win32api import GetSystemMetrics
from PIL import ImageTk, Image
from scraper import scraper
from gui import gui

# login interface
def logui():
    root = Tk()
    root.resizable(False, False)
    root.title("IRAS SCHEDULER")
    screen_width = 596
    screen_height = 707
    root.geometry(f"{screen_width}x{screen_height}+"
                f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

    try:
        img = ImageTk.PhotoImage(Image.open("iub.png"))
        panel = Label(root, image = img)
        panel.place(x=122, y=10)
    except:
        panel = Label(root, text="<image>")
        panel.place(x=270, y=150)

    ttk.Label(root, text="IRAS\nSCHEDULER", font="arial, 50", foreground="#190685").place(x=90, y=290)
    ttk.Label(root, text="------------ By Muyeed", font="arial, 20", foreground="#f18019").place(x=250, y=310)
    ttk.Label(root, text="ID             : ", font="arial, 25", foreground="#f18019").place(x=92, y=480)
    ttk.Label(root, text="Password : ", font="arial, 25", foreground="#f18019").place(x=92, y=540)

    id_var = StringVar()
    id = ttk.Entry(root, textvariable = id_var, width=39)
    id.place(x=270, y=493)

    passwd_var = StringVar()
    passwd = ttk.Entry(root, textvariable = passwd_var, width=39, show="*")
    passwd.place(x=270, y=553)

    def login():
        scraper(str(id_var.get()), str(passwd_var.get())) # scrape and create data.ini
        try:
            open(fr"user.ini", "w", encoding="utf-8").write(str(id_var.get())) # user.ini input
            root.destroy()
            gui()
        except:
            open(fr"user.ini", "w", encoding="utf-8").write("") # clear data.ini
            open(fr"data.ini", "w", encoding="utf-8").write("") # clear data.ini
            messagebox.showerror("IRAS SCHEDULER", "Error: Wrong Credentials !") # wrong credentials
            exit()

    lob = ttk.Button(text="Login", width=20, command=login)
    lob.place(x=379, y=600)

    root = mainloop()

# finding data.ini
if str(open(fr"data.ini", "r", encoding="utf-8").read()) == "":
    logui() # login
else:
    try:
        gui() # main gui
    except: 
        open(fr"data.ini", "w", encoding="utf-8").write("") # fixing data.ini
        messagebox.showerror("IRAS SCHEDULER", "Error: data.ini corrupted! Please restart!")
