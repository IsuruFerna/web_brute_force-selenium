from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ! use env variables or pass them directly to your program
# getting varibles from .env or setting default values
URL = os.environ.get('URL', "google.com")
PARTIAL_LINK_TEXT = os.environ.get('PARTIAL_LINK_TEXT', "google")

# service = Service(executable_path="")
# driver = webdriver.Chrome(service=service)
# tutorial: https://youtu.be/NB8OceGZGjA
# code: https://github.com/techwithtim/SeleniumTutorial

driver = webdriver.Chrome()

driver.get("https://google.com")

reject_all_btn = driver.find_element(By.ID, "W0wltc")
reject_all_btn.click()

#  Like an exception
# crash the program in 5 seconds if we did not get what we expected
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # clean input field
input_element.send_keys(URL + Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, PARTIAL_LINK_TEXT))
)


# LINK_TEXT finds the exact text while PARTIAL_LINK_TEXT finds similar text
#this finds the first one
link = driver.find_element(By.PARTIAL_LINK_TEXT, PARTIAL_LINK_TEXT)
link.click()

# finds multiplse as a list
# links = driver.find_elements(By.PARTIAL_LINK_TEXT, PARTIAL_LINK_TEXT)

time.sleep(100)

driver.quit()