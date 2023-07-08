from scraper import scraper
import getpass
from merger import merger


def main():
    print("IRAS_Scheduler; v0.1.3-alpha; By Muyeed")

    ui = input("Enter your ID: ")
    # pi = str(getpass.getpass("Enter your Password: "))
    pi = input("Enter your Password: ")

    print("Please Wait.... It may take 10~15 seconds")
    scraper(ui, pi)

    merger()

    input("\n\nPress any key to exit...")
    quit()


main()
