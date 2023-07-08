from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def scraper(username, password):
    try:
        options = webdriver.EdgeOptions()
        options.headless = True
        driver = webdriver.Edge(options=options)
    except:
        try:
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(options=options)
        except:
            try:
                options = webdriver.FirefoxOptions()
                options.headless = True
                driver = webdriver.Firefox(options=options)
            except:
                return "Error: No Supported Driver!"

    driver.get("http://www.irasv1.iub.edu.bd/")

    driver.find_element(By.XPATH, "//body/div[1]/app-root[1]/div[1]/div[1]/app-login[1]/div[1]/div[1]/div[1]/div["
                                  "2]/div[2]/form[1]/fieldset[1]/div[1]/span[1]/input[1]").send_keys(username)
    driver.find_element(By.CLASS_NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/app-root[1]/div[1]/div[1]/app-login[1]/div[1]/div[1]/div["
                                  "1]/div[2]/div[2]/form[1]/fieldset[1]/div[3]/button[1]").send_keys(Keys.ENTER)

    time.sleep(5)
    source_html = driver.page_source
    open(fr"data.ini", "w", encoding="utf-8").write(source_html)

    driver.quit()
