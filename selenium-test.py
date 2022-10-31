from selenium import webdriver
import os

URL = "https://google.com"

PATH = os.environ.get('CHROMEDRIVER')
if not PATH:
    print("chrome driver env variable not found")
driver = webdriver.Chrome(PATH)

driver.get(URL)
print(driver.title)
driver.quit()
