# Radio-button
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = 'https://demoqa.com/'
base_user_name = "standard_user"
base_password = "secret_sauce"
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)

driver.get(base_url)
driver.maximize_window()
elements = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div/div/div[2]/div/div[1]'
)
elements.click()
time.sleep(2)
element_radio_button = driver.find_element(By.XPATH, '//li[@id="item-2"]')
element_radio_button.click()
time.sleep(2)
activate_r_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
activate_r_button.click()
message = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p'
).text
assert message == "You have selected Yes"
print("TEST_PASSED")

time.sleep(100)
driver.close()
