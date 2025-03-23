import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

logging.basicConfig(filename="automation.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Automation script started")

try:
    driver = webdriver.Chrome()
    logging.info("Chrome browser launched")

    driver.get("https://www.saucedemo.com/")
    logging.info("Website opened")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    logging.info("Login successful")

    time.sleep(3)

    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(2)

    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
    logging.info("Logout successful")

    time.sleep(2)
    driver.quit()
    logging.info("Browser closed successfully")

except Exception as e:
    logging.error(f"Error occurred: {e}")
