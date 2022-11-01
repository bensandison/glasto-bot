from selenium import webdriver
import os
from nordvpn_switcher import initialize_VPN, rotate_VPN


instructions = initialize_VPN(area_input=['random countries europe 8'])

for i in range(3):
    rotate_VPN(instructions)  # refer to the instructions variable here
    print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')


URL = "https://glastonbury.seetickets.com/content/extras"

# Setup Chrome Driver
PATH = os.environ.get('CHROMEDRIVER')
if not PATH:
    print("chrome driver env variable not found")
driver = webdriver.Chrome(PATH)

# Open URL in browser
driver.get(URL)

for x in range(50):
    print(driver.title)
    driver.refresh()

driver.close()
