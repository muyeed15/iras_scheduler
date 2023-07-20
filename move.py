# modules
import getpass
import shutil

def move():
    user_name = getpass.getuser() # user name

    src_path = fr"schedule.txt" # file location
    dst_path = fr"C:\Users\{user_name}\Desktop\schedule.txt" # moving destination

    try:
        shutil.move(src_path, dst_path) # copy process
    except: pass
