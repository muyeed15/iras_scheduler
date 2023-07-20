# modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from win32api import GetSystemMetrics
from merger import merger
from date import sch_day
from exporter import exporter
from updater import updater
import webbrowser

# main interface
def gui():
    # week data
    day_x0, day_x1, day_x2, day_x3, day_x4, day_x5, day_x6 = sch_day()

    # routine data
    sat_dat, sun_dat, mon_dat, tue_dat, wed_dat, thu_dat = merger()

    # defining the maximum class
    try:
        sat_sx = len(sat_dat[0])
    except: sat_sx = 0

    try:
        sun_sx = len(sun_dat[0])
    except: sun_sx = 0

    try:
        mon_sx = len(mon_dat[0])
    except: mon_sx = 0

    try:
        tue_sx = len(tue_dat[0])
    except: tue_sx = 0

    try:
        wed_sx = len(wed_dat[0])
    except:
        wed_sx = 0
    
    try:
        thu_sx = len(thu_dat[0])
    except: thu_sx = 0

    clses = [sat_sx, sun_sx, mon_sx, thu_sx, wed_sx, thu_sx]
    xclses = max(clses)

    # gui
    root = Tk()
    root.resizable(False, False)
    root.title("IRAS SCHEDULER")

    # resolution fittings
    if xclses <= 4:
        xsh = 493
    elif xclses == 5:
        xsh = 610
    elif xclses == 6:
        xsh = 727
    
    screen_width = 596
    screen_height = xsh
    root.geometry(f"{screen_width}x{screen_height}+"
                f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

    root.resizable(False, False)

    root.iconbitmap(fr"iras_scheduler.ico")

    # menubar
    menubar = Menu(root)
    
    # menu and commands
    def ex_sch():
        exporter()
        messagebox.showinfo("IRAS SCHEDULER", "Exported Successfully !")

    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Options', menu = file)
    file.add_command(label ='Export Shedule to Text File', command = ex_sch)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)

    def devinfo(): # devloper informations
        root = Tk()
        root.resizable(False, False)
        root.iconbitmap(fr"iras_scheduler.ico")
        root.title("Developer Information")
        screen_width = 300
        screen_height = 150
        root.geometry(f"{screen_width}x{screen_height}+"
                    f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

        ttk.Label(root, text="Developed by", font="arial, 15", foreground="#1b7a34").pack()
        ttk.Label(root, text="Syed Abdullah Al Muyeed", font="arial, 10").pack()
        ttk.Label(root, text="Department of Computer Science & Engineering,", font="arial, 10").pack()
        ttk.Label(root, text="Independent University, Bangladesh", font="arial, 10").pack()
        ttk.Label(root, text="IUB Mail: 2230324@iub.edu.bd", font="arial, 10").pack()
        ttk.Label(root, text="LICENSE: MIT License", font="arial, 10").pack()
        ttk.Label(root, text="@2023", font="arial, 10").pack()

        # gui loop
        root.mainloop()
    
    def up_chk(): # updater
        up_fetch, check, version = updater()
        if up_fetch == True:
            ans = messagebox.askquestion("Updater", f"A newer version available !\nVersion: {version} --> Version: {check}\nDo you want to update?")
            if ans == "yes":
                root.destroy()
                webbrowser.open_new_tab("https://sourceforge.net/projects/iras-scheduler/")
            else:
                pass
        else:
            messagebox.showinfo("Updater", f"You are up to date !\nVersion: {version}")


    about = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='About', menu = about)
    about.add_command(label ='Check Updates', command = up_chk)
    about.add_separator()
    about.add_command(label ='Developer Info', command = devinfo)

    root.config(menu = menubar)

    # canvases
    cf0 = ttk.Frame(root) # options frame
    cf0.place(x=0, y=0)
    cop = Canvas(cf0, background="#0376c8", width=223, height=720) # option canvas
    cop.grid(row=0, column=0)

    # ui tuning
    def sch_can_0():
        # relax
        cfrelax = ttk.Frame(root)
        ttk.Label(cfrelax, text=" Chill dude!", foreground="#bababa",font="arial, 50").pack()

        # saturday
        cfa = ttk.Frame(root) # routine frame
        flags = []
        for i in range(6):
            if i == 0:
                color = "#58bf4e"
            elif i == 1:
                color = "#874abd"
            elif i == 2:
                color = "#4a8dbd"
            elif i == 3:
                color = "#bd924a"
            elif i == 4:
                color = "#bd4a78"
            elif i == 5:
                color = "#bd634a"

            try:
                sub_sec = f"{sat_dat[0][i]}: Sec{sat_dat[2][i]}"
                name = sat_dat[1][i]
                try:
                    time = sat_dat[4][i].replace("R", "")
                except:
                    pass
                room = f"-{sat_dat[3][i]}"
            except:
                name = None
                sub_sec = None
                time = None
                room = None
                color = None
            
            if name != None and sub_sec != None and time != None and room != None and color != None:
                cru = Canvas(cfa, background=color, width=350, height=107) # routine canvas
                cru.grid(row=i, column=0, pady=3)

                ttk.Label(cru, text=sub_sec, font="arial, 25", background=color, foreground="white").place(x=2, y=3)
                ttk.Label(cru, text=name, font="arial, 10", background=color, foreground="white").place(x=9, y=46)
                ttk.Label(cru, text=time, font="arial, 18", background=color, foreground="white").place(x=5, y=70)
                ttk.Label(cru, text=room, font="arial, 15", background=color, foreground="white").place(x=170, y=71)
                flags.append(True)
            else:
                flags.append(False)
            
            if True not in flags:
                cfa = cfrelax

        # sunday
        cfs = ttk.Frame(root) # routine frame
        flags = []
        for i in range(6):
            if i == 0:
                color = "#58bf4e"
            elif i == 1:
                color = "#874abd"
            elif i == 2:
                color = "#4a8dbd"
            elif i == 3:
                color = "#bd924a"
            elif i == 4:
                color = "#bd4a78"
            elif i == 5:
                color = "#bd634a"

            try:
                sub_sec = f"{sun_dat[0][i]}: Sec{sun_dat[2][i]}"
                name = sun_dat[1][i]
                try:
                    time = sun_dat[4][i].replace("T", "")
                except:
                    pass
                room = f"-{sun_dat[3][i]}"
            except:
                name = None
                sub_sec = None
                time = None
                room = None
                color = None
            
            if name != None and sub_sec != None and time != None and room != None and color != None:
                cru = Canvas(cfs, background=color, width=350, height=107) # routine canvas
                cru.grid(row=i, column=0, pady=3)

                ttk.Label(cru, text=sub_sec, font="arial, 25", background=color, foreground="white").place(x=2, y=3)
                ttk.Label(cru, text=name, font="arial, 10", background=color, foreground="white").place(x=9, y=46)
                ttk.Label(cru, text=time, font="arial, 18", background=color, foreground="white").place(x=5, y=70)
                ttk.Label(cru, text=room, font="arial, 15", background=color, foreground="white").place(x=170, y=71)
                flags.append(True)
            else:
                flags.append(False)
            
            if True not in flags:
                cfs = cfrelax
            
        # Monday
        cfm = ttk.Frame(root) # routine frame
        flags = []
        for i in range(6):
            if i == 0:
                color = "#58bf4e"
            elif i == 1:
                color = "#874abd"
            elif i == 2:
                color = "#4a8dbd"
            elif i == 3:
                color = "#bd924a"
            elif i == 4:
                color = "#bd4a78"
            elif i == 5:
                color = "#bd634a"
        
            try:
                sub_sec = f"{mon_dat[0][i]}: Sec{mon_dat[2][i]}"
                name = mon_dat[1][i]
                try:
                    time = mon_dat[4][i].replace("W", "")
                except:
                    pass
                room = f"-{mon_dat[3][i]}"
            except:
                name = None
                sub_sec = None
                time = None
                room = None
                color = None
            
            if name != None and sub_sec != None and time != None and room != None and color != None:
                cru = Canvas(cfm, background=color, width=350, height=107) # routine canvas
                cru.grid(row=i, column=0, pady=3)

                ttk.Label(cru, text=sub_sec, font="arial, 25", background=color, foreground="white").place(x=2, y=3)
                ttk.Label(cru, text=name, font="arial, 10", background=color, foreground="white").place(x=9, y=46)
                ttk.Label(cru, text=time, font="arial, 18", background=color, foreground="white").place(x=5, y=70)
                ttk.Label(cru, text=room, font="arial, 15", background=color, foreground="white").place(x=170, y=71)
                flags.append(True)
            else:
                flags.append(False)
            
            if True not in flags:
                cfm = cfrelax
            

        # tuesday
        cft = ttk.Frame(root) # routine frame
        flags = []
        for i in range(6):
            if i == 0:
                color = "#58bf4e"
            elif i == 1:
                color = "#874abd"
            elif i == 2:
                color = "#4a8dbd"
            elif i == 3:
                color = "#bd924a"
            elif i == 4:
                color = "#bd4a78"
            elif i == 5:
                color = "#bd634a"
        
            try:
                sub_sec = f"{tue_dat[0][i]}: Sec{tue_dat[2][i]}"
                name = tue_dat[1][i]
                try:
                    time = tue_dat[4][i].replace("S", "")
                except:
                    pass
                room = f"-{tue_dat[3][i]}"
            except:
                name = None
                sub_sec = None
                time = None
                room = None
                color = None
            
            if name != None and sub_sec != None and time != None and room != None and color != None:
                cru = Canvas(cft, background=color, width=350, height=107) # routine canvas
                cru.grid(row=i, column=0, pady=3)

                ttk.Label(cru, text=sub_sec, font="arial, 25", background=color, foreground="white").place(x=2, y=3)
                ttk.Label(cru, text=name, font="arial, 10", background=color, foreground="white").place(x=9, y=46)
                ttk.Label(cru, text=time, font="arial, 18", background=color, foreground="white").place(x=5, y=70)
                ttk.Label(cru, text=room, font="arial, 15", background=color, foreground="white").place(x=170, y=71)
                flags.append(True)
            else:
                flags.append(False)
            
            if True not in flags:
                cft = cfrelax

        # wednesday
        cfw = ttk.Frame(root) # routine frame
        flags = []
        for i in range(6):
            if i == 0:
                color = "#58bf4e"
            elif i == 1:
                color = "#874abd"
            elif i == 2:
                color = "#4a8dbd"
            elif i == 3:
                color = "#bd924a"
            elif i == 4:
                color = "#bd4a78"
            elif i == 5:
                color = "#bd634a"
        
            try:
                sub_sec = f"{wed_dat[0][i]}: Sec{wed_dat[2][i]}"
                name = wed_dat[1][i]
                try:
                    time = wed_dat[4][i].replace("M", "")
                except:
                    pass
                room = f"-{wed_dat[3][i]}"
            except:
                name = None
                sub_sec = None
                time = None
                room = None
                color = None

            if name != None and sub_sec != None and time != None and room != None and color != None:
                cru = Canvas(cfw, background=color, width=350, height=107) # routine canvas
                cru.grid(row=i, column=0, pady=3)

                ttk.Label(cru, text=sub_sec, font="arial, 25", background=color, foreground="white").place(x=2, y=3)
                ttk.Label(cru, text=name, font="arial, 10", background=color, foreground="white").place(x=9, y=46)
                ttk.Label(cru, text=time, font="arial, 18", background=color, foreground="white").place(x=5, y=70)
                ttk.Label(cru, text=room, font="arial, 15", background=color, foreground="white").place(x=170, y=71)
                flags.append(True)
            else:
                flags.append(False)
            
            if True not in flags:
                cfw = cfrelax

        # thursday
        cfr = ttk.Frame(root) # routine frame
        flags = []
        for i in range(6):
            if i == 0:
                color = "#58bf4e"
            elif i == 1:
                color = "#874abd"
            elif i == 2:
                color = "#4a8dbd"
            elif i == 3:
                color = "#bd924a"
            elif i == 4:
                color = "#bd4a78"
            elif i == 5:
                color = "#bd634a"
        
            try:
                sub_sec = f"{thu_dat[0][i]}: Sec{thu_dat[2][i]}"
                name = thu_dat[1][i]
                try:
                    time = thu_dat[4][i].replace("A", "")
                except:
                    pass
                room = f"-{thu_dat[3][i]}"
            except:
                name = None
                sub_sec = None
                time = None
                room = None
                color = None

            if name != None and sub_sec != None and time != None and room != None and color != None:
                cru = Canvas(cfr, background=color, width=350, height=107) # routine canvas
                cru.grid(row=i, column=0, pady=3)

                ttk.Label(cru, text=sub_sec, font="arial, 25", background=color, foreground="white").place(x=2, y=3)
                ttk.Label(cru, text=name, font="arial, 10", background=color, foreground="white").place(x=9, y=46)
                ttk.Label(cru, text=time, font="arial, 18", background=color, foreground="white").place(x=5, y=70)
                ttk.Label(cru, text=room, font="arial, 15", background=color, foreground="white").place(x=170, y=71)
                flags.append(True)
            else:
                flags.append(False)
            
            if True not in flags:
                cfr = cfrelax

        # remove frame
        def removeframe():
            try:
                cfa.place_forget()
            except: pass

            try:
                cfs.place_forget()
            except: pass

            try:
                cfm.place_forget()
            except: pass

            try:
                cft.place_forget()
            except: pass

            try:
                cfw.place_forget()
            except: pass

            try:
                cfr.place_forget()
            except: pass

            try:
                cfrelax.place_forget()
            except: pass
                
        # button commands
        if day_x0 == "Sat":
            def tod():
                removeframe()
                cfa.place(x=233, y=0)
            def tom():
                removeframe()
                cfs.place(x=233, y=0)
            def x0():
                removeframe()
                cfm.place(x=233, y=0)
            def x1():
                removeframe()
                cft.place(x=233, y=0)
            def x2():
                removeframe()
                cfw.place(x=233, y=0)
            def x3():
                removeframe()
                cfr.place(x=233, y=0)
            def x4():
                removeframe()
                cfrelax.place(x=233, y=0)
            
        elif day_x0 == "Sun":
            def tod():
                removeframe()
                cfs.place(x=233, y=0)
            def tom():
                removeframe()
                cfm.place(x=233, y=0)
            def x0():
                removeframe()
                cft.place(x=233, y=0)
            def x1():
                removeframe()
                cfw.place(x=233, y=0)
            def x2():
                removeframe()
                cfr.place(x=233, y=0)
            def x3():
                removeframe()
                cfrelax.place(x=233, y=0)
            def x4():
                removeframe()
                cfa.place(x=233, y=0)
        
        elif day_x0 == "Mon":
            def tod():
                removeframe()
                cfm.place(x=233, y=0)
            def tom():
                removeframe()
                cft.place(x=233, y=0)
            def x0():
                removeframe()
                cfw.place(x=233, y=0)
            def x1():
                removeframe()
                cfr.place(x=233, y=0)
            def x2():
                removeframe()
                cfrelax.place(x=233, y=0)
            def x3():
                removeframe()
                cfa.place(x=233, y=0)
            def x4():
                removeframe()
                cfs.place(x=233, y=0)

        elif day_x0 == "Tue":
            def tod():
                removeframe()
                cft.place(x=233, y=0)
            def tom():
                removeframe()
                cfw.place(x=233, y=0)
            def x0():
                removeframe()
                cfr.place(x=233, y=0)
            def x1():
                removeframe()
                cfrelax.place(x=233, y=0)
            def x2():
                removeframe()
                cfa.place(x=233, y=0)
            def x3():
                removeframe()
                cfs.place(x=233, y=0)
            def x4():
                removeframe()
                cfm.place(x=233, y=0)

        elif day_x0 == "Wed":
            def tod():
                removeframe()
                cfw.place(x=233, y=0)
            def tom():
                removeframe()
                cfr.place(x=233, y=0)
            def x0():
                removeframe()
                cfrelax.place(x=233, y=0)
            def x1():
                removeframe()
                cfa.place(x=233, y=0)
            def x2():
                removeframe()
                cfs.place(x=233, y=0)
            def x3():
                removeframe()
                cfm.place(x=233, y=0)
            def x4():
                removeframe()
                cft.place(x=233, y=0)

        elif day_x0 == "Thu":
            def tod():
                removeframe()
                cfr.place(x=233, y=0)
            def tom():
                removeframe()
                cfrelax.place(x=233, y=0)
            def x0():
                removeframe()
                cfa.place(x=233, y=0)
            def x1():
                removeframe()
                cfs.place(x=233, y=0)
            def x2():
                removeframe()
                cfm.place(x=233, y=0)
            def x3():
                removeframe()
                cft.place(x=233, y=0)
            def x4():
                removeframe()
                cfw.place(x=233, y=0)

        elif day_x0 == "Fri":
            def tod():
                removeframe()
                cfrelax.place(x=233, y=0)
            def tom():
                removeframe()
                cfa.place(x=233, y=0)
            def x0():
                removeframe()
                cfs.place(x=233, y=0)
            def x1():
                removeframe()
                cfm.place(x=233, y=0)
            def x2():
                removeframe()
                cft.place(x=233, y=0)
            def x3():
                removeframe()
                cfw.place(x=233, y=0)
            def x4():
                removeframe()
                cfr.place(x=233, y=0)
        
        # toadys
        tod()

        # button frame
        bf0 = ttk.Frame(root)
        bf0.place(x=10, y=10)

        # button size
        sbx = 65
        sby = 10

        # title frame
        ttk.Label(bf0, text="Schedule").grid(row=0, column=0)

        # buttons
        butt_0 = ttk.Button(bf0, text="Today", command=tod)
        butt_0.grid(row=1, column=0, ipadx=sbx, ipady=sby)
        butt_1 = ttk.Button(bf0, text="Tomorrow", command=tom)
        butt_1.grid(row=2, column=0, ipadx=sbx, ipady=sby)
        butt_2 = ttk.Button(bf0, text=day_x2, command=x0)
        butt_2.grid(row=3, column=0, ipadx=sbx, ipady=sby)
        butt_3 = ttk.Button(bf0, text=day_x3, command=x1)
        butt_3.grid(row=4, column=0, ipadx=sbx, ipady=sby)
        butt_4 = ttk.Button(bf0, text=day_x4, command=x2)
        butt_4.grid(row=5, column=0, ipadx=sbx, ipady=sby)
        butt_5 = ttk.Button(bf0, text=day_x5, command=x3)
        butt_5.grid(row=6, column=0, ipadx=sbx, ipady=sby)
        butt_6 = ttk.Button(bf0, text=day_x6, command=x4)
        butt_6.grid(row=7, column=0, ipadx=sbx, ipady=sby)

    sch_can_0()

    # id lnfo and logout
    def sch_acc():
        af0 = ttk.Frame(root)
        af0.place(x=10, y=352)

        ttk.Label(af0, text="Account Info:", font="arial, 12").pack(pady=10)

        # ID
        id_dat = open(fr"user.ini", "r", encoding="utf-8").read()
        ttk.Label(af0, text=f"ID: {id_dat}", font="arial, 16").pack()

        def logout():
            # clear
            open(fr"user.ini", "w", encoding="utf-8").write("")
            open(fr"data.ini", "w", encoding="utf-8").write("")
            # destroy
            root.destroy()

        # log out
        lob = ttk.Button(af0, text="Log Out", command=logout)
        lob.pack(padx=65, pady=8)

    sch_acc()

    # gui loop
    root.mainloop()
