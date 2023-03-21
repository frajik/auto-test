from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

base_url = 'https://demoqa.com/date-picker'
driver = webdriver.Chrome(
    executable_path="/d/Dev/auto_testing/seleniumLessons/chromedriver.exe"
)

driver.get(base_url)
driver.maximize_window()
action = webdriver.ActionChains(driver)

date_form = driver.find_element(
    By.ID,
    'datePickerMonthYearInput'
)
time.sleep(2)

# date_form.clear() баг

# PRINT_date
date_form.send_keys(Keys.BACKSPACE*10)
time.sleep(2)

date_form.send_keys("10/10/1990")
time.sleep(2)

date_form.send_keys(Keys.RETURN)
time.sleep(2)

# CHOICE_date
date_form.click()
time.sleep(2)

date_form.send_keys(Keys.BACKSPACE*10)
time.sleep(2)

selection_field = driver.find_element(
    By.XPATH,
    '//div[@aria-label="Choose Tuesday, January 24th, 2023"]'
).click()

time.sleep(100)
driver.close()
