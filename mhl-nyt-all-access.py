# automate logging into MHL's NYT all-access

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# details

LIB_CARD_NUM = "21330001217930" # dummy number
EMAIL = "aneeshratnala@ucla.edu"
PW = "Ucla2024!" # dummy pw
LIB_URL = "https://mhl.org/connect/20528"
#REDEMPTION_URL = "https://nytimes.com/subscription/redeem/all-access?campaignId=8WL9J&gift_code=0f0fdf2e41f43bd1"

# set up, launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("Launching browser...")

try:

    # update: when not on MHL network, need to login with LIB CARD NUM first!
    # 1. go to url
    driver.get(LIB_URL)
    print("Navigating to MHL URL...")

    # 2. locate card num input box
    card_input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "card-number")))
    
    card_input_box.send_keys(LIB_CARD_NUM)
    print("Entered library card number.")

    # 3. hit submit button
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "mhl-connector-form-submit")))
    submit_button.click()
    print("Clicked submit button.")

    # 4. wait and check if on nyt page
    time.sleep(5)
    if "nytimes.com" not in driver.current_url:
        print("Failed to reach NYT redemption page")
        driver.quit()
        exit(1)

    # 5. hit redeem button on NYT page
    redeem_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='btn-redeem']")))
    redeem_button.click()
    print("Clicked redeem button.")

    # 6. locate email input box and fill
    email_input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

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