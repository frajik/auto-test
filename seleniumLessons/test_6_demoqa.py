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
element_checkbox = driver.find_element(By.XPATH, '//li[@id="item-1"]')
element_checkbox.click()
time.sleep(2)
check_box = driver.find_element(
    By.XPATH,
    "//*[@id='tree-node']/ol/li/span/button"
)
check_box.click()

# message = driver.find_element(By.XPATH, '//*[@id="result"]/span[1]').text
# assert message == "You have selected :"
# print("CHECKBOX_PASSED")


time.sleep(100)
driver.close()
