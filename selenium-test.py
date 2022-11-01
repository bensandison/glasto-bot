from selenium import webdriver
import os
from nordvpn_switcher import initialize_VPN, rotate_VPN

# TODO: optimise selenium browser (no images)
# Stop when reaches ticket page
# Detect and move off slow connections

URL = "https://glastonbury.seetickets.com/content/extras"
isOnTicketPage = False
refreshPerIP = 50
refreshCounter = 0

# Setup VPN rotator:
instructions = initialize_VPN(area_input=['random countries europe 9'])

# Setup Chrome Driver:
PATH = os.environ.get('CHROMEDRIVER')   # get driver location from env variable
if not PATH:
    print("chrome driver env variable not found")
driver = webdriver.Chrome(PATH)


while not isOnTicketPage:
    driver.delete_all_cookies()  # delete cookies
    rotate_VPN(instructions)   # Get new IP

    for x in range(refreshPerIP):
        # Open URL in browser
        driver.get(URL)  # refresh
        refreshCounter += 1     # increment counter
        print("Refresh " + str(refreshCounter))
