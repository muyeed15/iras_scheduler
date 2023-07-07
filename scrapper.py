from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


def scraper(username, password):
    driver = webdriver.Chrome()

    driver.get("http://www.irasv1.iub.edu.bd/")

    driver.find_element(By.XPATH, "//body/div[1]/app-root[1]/div[1]/div[1]/app-login[1]/div[1]/div[1]/div[1]/div["
                                  "2]/div[2]/form[1]/fieldset[1]/div[1]/span[1]/input[1]").send_keys(username)
    driver.find_element(By.CLASS_NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/app-root[1]/div[1]/div[1]/app-login[1]/div[1]/div[1]/div["
                                  "1]/div[2]/div[2]/form[1]/fieldset[1]/div[3]/button[1]").send_keys(Keys.ENTER)

    time.sleep(4)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(3)
    driver.quit()
