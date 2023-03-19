# Using keyboard and screenshots
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import datetime
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
password.clear()
password.send_keys(Keys.RETURN)

filter = driver.find_element(
    By.XPATH, "//select[@class='product_sort_container']"
)
filter.click()
time.sleep(2)
filter.send_keys(Keys.DOWN)
time.sleep(2)
filter.send_keys(Keys.RETURN)
# time.sleep(5)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# user_name.send_keys("er")
# # password = driver.find_element(By.XPATH, "//input[@id='password']")
# # password.send_keys(base_password)
# # login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
# # login_button.click()
current_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
screenshot_name = "screenshot_" + current_time + ".png"
driver.save_screenshot(
    "D:\\Dev\\auto_testing\\seleniumLessons\\screenshots\\" + screenshot_name
)

time.sleep(100)
driver.close()
