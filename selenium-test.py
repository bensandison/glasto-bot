from selenium import webdriver
import os

URL = "https://glastonbury.seetickets.com/content/extras"

PATH = os.environ.get('CHROMEDRIVER')
if not PATH:
    print("chrome driver env variable not found")
driver = webdriver.Chrome(PATH)

driver.get(URL)

for x in range(50):
    print(driver.title)
    driver.refresh()

driver.close()
