import os
import shutil
from win32_username import win32_username

x_user = win32_username()


def deleter():
    try:
        os.remove(fr"C:/Users/{x_user}/Downloads/Independent University, Bangladesh.html")
    except:
        return "Error: No such file exist!"

    try:
        shutil.rmtree(os.path.join(fr"C:/Users/{x_user}/Downloads/", "Independent University, Bangladesh_files"))
    except:
        return "Error: No such folder exist!"
