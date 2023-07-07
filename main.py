from scrapper import scraper
from gui import dat
from gui import gui
from merger import merger
from deleter import deleter
from clear_credentials import clear_credentials

print("IRAS_Scheduler; V.0.0.2.alpha - By Muyeed")
gui()
scraper(dat[0], dat[1])
print("\n\nSchedule:")
merger()
clear_credentials()
deleter()
input("\n\nPress Enter to exit...")
quit()
