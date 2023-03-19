from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)
# driver = webdriver.Firefox(
#     executable_path="/d/Dev/auto_testing/seleniumLessons/geckodriver.exe"
# )
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# user_name = driver.find_element(By.ID, "user-name") # ID
# user_name = driver.find_element(By.NAME, "user-name") # NAME
# user_name = driver.find_element(
#   By.XPATH, '//*[@id="user-name"]'
# )  # Full XPATH
# user_name = driver.find_element(
#   By.XPATH, '//input[@id="user-name"]'
# ) # Id XPATH
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
login_button.click()
time.sleep(10)
driver.close()
