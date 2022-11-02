from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from nordvpn_switcher import initialize_VPN, rotate_VPN
import re

# TODO:
# Detect and move off slow connections

URL = "https://glastonbury.seetickets.com/content/extras"
SEARCH_TERM = "worthy"
isOnTicketPage = False
refreshPerIP = 50
refreshCounter = 0

# Setup VPN rotator:
instructions = initialize_VPN(area_input=['random countries europe 9'])

# Chrome Driver Settings:
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # keep browser open

# Setup Chrome Driver:
PATH = os.environ.get('CHROMEDRIVER')   # get driver location from env variable
if not PATH:
    print("chrome driver env variable not found")
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

while not isOnTicketPage:
    driver.delete_all_cookies()  # delete cookies
    rotate_VPN(instructions)   # Get new IP

    for x in range(refreshPerIP):
        # Open URL in browser
        driver.get(URL)  # refresh

        src = driver.page_source    # get page source
        # search using regex
        text_found = re.search(SEARCH_TERM, src, re.IGNORECASE)

        if text_found != None:
            # if search success:
            isOnTicketPage = True
            print("SUCESS!")
            break
        else:
            # if search failed
            refreshCounter += 1     # increment counter
            print("Refresh " + str(refreshCounter) + ": FAILED")
