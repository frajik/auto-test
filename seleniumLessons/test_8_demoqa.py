from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = 'https://demoqa.com/'
base_user_name = "standard_user"
base_password = "secret_sauce"
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)
action = webdriver.ActionChains(driver)
driver.get(base_url)
driver.maximize_window()
elements = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div/div/div[2]/div/div[1]'
)
elements.click()
time.sleep(2)
buttons = driver.find_element(By.XPATH, "//*[@id='item-4']")
buttons.click()
time.sleep(2)
double_click_button = driver.find_element(
    By.XPATH, "//button[@id='doubleClickBtn']"
)
action.double_click(double_click_button).perform()
time.sleep(2)
right_click_button = driver.find_element(
    By.XPATH,
    "//button[@id='rightClickBtn']"
)
action.context_click(right_click_button).perform()  # "RightLClick"

time.sleep(100)
driver.close()
