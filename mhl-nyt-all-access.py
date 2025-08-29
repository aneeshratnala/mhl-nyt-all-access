# automate logging into MHL's NYT all-access

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# details
EMAIL = "aneeshratnala@ucla.edu"
PW = "Ucla2024!"
REDEMPTION_URL = "https://nytimes.com/subscription/redeem/all-access?campaignId=8WL9J&gift_code=0f0fdf2e41f43bd1"

# set up, launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("Launching browser...")

try:
    # 1. go to url
    driver.get(REDEMPTION_URL)
    print("Navigating to URL...")

    # 2. hit redeem button
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='btn-redeem']")))
    button.click()
    print("Clicked redeem button.")


except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()
    exit(1)
    
finally:
    # driver.quit()
    print("in finally")
    time.sleep(15) # 15 second wait
    driver.quit()
    print("Browser closed.")