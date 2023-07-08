from scrapper import scraper
import getpass
from merger import merger


def main():
    print("IRAS_Scheduler; v0.1.2.alpha - By Muyeed")

    ui = input("Enter your username: ")
    # pi = str(getpass.getpass("Enter your password: "))
    pi = input("Enter your password: ")

    print("Please Wait.... It may take 10~15 seconds")
    scraper(ui, pi)

    merger()

    input("\n\nPress any key to exit...")
    quit()


main()
