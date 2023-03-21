from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

base_url = 'https://demoqa.com/dynamic-properties'
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)

driver.get(base_url)
driver.maximize_window()

try:
    visible_button = driver.find_element(
        By.ID,
        "visibleAfter"
    ).click()
except NoSuchElementException as error:
    print(error)
    time.sleep(5)
    visible_button = driver.find_element(
        By.ID,
        "visibleAfter"
    ).click()


time.sleep(100)
driver.close()
