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

# products_title = driver.find_element(By.XPATH, "//span[@class='title']")
# value_product_title = products_title.text
# print(value_product_title)
# assert value_product_title == "Products"
# print("PASSED")

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert url == get_url
print("TEST_URL_PASSED")


time.sleep(100)
driver.close()
