# Negative_testing: LOGIN_FAILED
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = 'https://www.saucedemo.com/'
base_user_name = "standard_user"
base_password = "secret_sauc"
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(base_user_name)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(base_password)
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()

warning = driver.find_element(By.XPATH, "//h3[@data-test='error']")
text_error = warning.text
assert text_error == (
    "Epic sadface: Username and password do not match any user in this service"
)
print("Test_passed")

driver.refresh()  # обновить страницу

time.sleep(100)
driver.close()
