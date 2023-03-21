from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = 'https://demoqa.com/slider'
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)
action = webdriver.ActionChains(driver)
driver.get(base_url)
driver.maximize_window()

slider = driver.find_element(
    By.XPATH,
    "//input[@class='range-slider range-slider--primary']"
)
time.sleep(2)
action.click_and_hold(slider).move_by_offset(20, 0).release().perform()


time.sleep(100)
driver.close()
