# Скролинг и наводка на элемент
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import datetime

base_url = 'https://www.saucedemo.com/'
base_user_name = "standard_user"
base_password = "secret_sauce"
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(base_user_name)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(base_password)
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
time.sleep(2)
# driver.execute_script("window.scrollTo(0, 50)") # скролим на 50 пикселей вниз
action = webdriver.ActionChains(driver)
inv_item = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
action.move_to_element(inv_item).perform()

time.sleep(2)

# current_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
# screenshot_name = "screenshot_" + current_time + ".png"
# driver.save_screenshot(
#     "D:\\Dev\\auto_testing\\seleniumLessons\\screenshots\\" + screenshot_name
# )

time.sleep(100)
driver.close()
