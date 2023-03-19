# Взаимодействие/тест бургера
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = 'https://www.saucedemo.com/'
base_user_name = "standard_user"
base_password = "secret_sauce"
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
time.sleep(2)

burger = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
burger.click()
time.sleep(2)
burger_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
burger_about.click()
about = driver.find_element(By.XPATH, "/html/body/h1").text
assert about == "Error: Forbidden"
print("PASSED")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
print("complete")
driver.back()

time.sleep(100)
driver.close()
