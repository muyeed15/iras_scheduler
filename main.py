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
    screen_width = 592
    screen_height = 493
    root.geometry(f"{screen_width}x{screen_height}+"
                f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

    root.iconbitmap(fr"iras_scheduler.ico")

    try:
        img = ImageTk.PhotoImage(Image.open("iras_scheduler.png"))
        panel = Label(root, image = img)
        panel.place(x=30, y=10)
    except:
        panel = Label(root, text="<image>", foreground="#bababa")
        panel.place(x=120, y=150)

    ttk.Label(root, text="IRAS", font="arial, 80", foreground="#7fb6e0").place(x=300, y=40)
    ttk.Label(root, text="SCHEDULER", font="arial, 29", foreground="#0376c8").place(x=305, y=150)
    ttk.Label(root, text="---------- By Muyeed", font="arial, 20", foreground="#7fb6e0").place(x=308, y=200)
    ttk.Label(root, text="ID             : ", font="arial, 25", foreground="#0376c8").place(x=44, y=289)
    ttk.Label(root, text="Password : ", font="arial, 25", foreground="#0376c8").place(x=44, y=349)

    id_var = StringVar()
    id = ttk.Entry(root, textvariable = id_var, width=50)
    id.place(x=240, y=300)

    passwd_var = StringVar()
    passwd = ttk.Entry(root, textvariable = passwd_var, width=50, show="*")
    passwd.place(x=240, y=360)

    def login():
        root.destroy()
        scraper(str(id_var.get()), str(passwd_var.get())) # scrape and create data.ini
        try:
            open(fr"user.ini", "w", encoding="utf-8").write(str(id_var.get())) # user.ini input
            gui()
        except:
            open(fr"user.ini", "w", encoding="utf-8").write("") # clear data.ini
            open(fr"data.ini", "w", encoding="utf-8").write("") # clear data.ini
            messagebox.showerror("IRAS SCHEDULER", "Error: Wrong Credentials !") # wrong credentials
            exit()

    flob = ttk.Frame(root)
    flob.place(x=450, y=410)
    lob = ttk.Button(flob, text="Login", command=login)
    lob.pack(ipadx=10, ipady=10)

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
