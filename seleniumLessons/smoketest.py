from selenium import webdriver
from selenium.webdriver.common.by import By
import time

first_name = "test"
last_name = "test"
zip_code = 297408
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

# first_item_data
name_item_1 = driver.find_element(
    By.XPATH,
    '//*[@id="item_4_title_link"]/div'
).text  # "Sauce Labs Backpack"

price_item_1 = driver.find_element(
    By.XPATH,
    '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div'
).text  # "$29.99"

# add_to_cart
add_item_1 = driver.find_element(
    By.XPATH,
    "//button[@id='add-to-cart-sauce-labs-backpack']"
).click()
time.sleep(2)

# get_cart
shopping_cart = driver.find_element(
    By.XPATH,
    "//div[@id='shopping_cart_container']"
).click()
time.sleep(2)

# inventory_item_1_data
inv_name_item_1 = driver.find_element(
    By.XPATH,
    "//div[@class='inventory_item_name']"
).text
inv_price_item_1 = driver.find_element(
    By.XPATH,
    "//div[@class='inventory_item_price']"
).text
assert name_item_1 == inv_name_item_1
print("Inventory: The product name matches! Test PASSED!")
assert price_item_1 == inv_price_item_1
print("Inventory: The product price matches! Test PASSED!")


# checkout_data_user
get_checkout = driver.find_element(
    By.XPATH,
    "//button[@class='btn btn_action btn_medium checkout_button']"
).click()
time.sleep(2)

checkout_first_name = driver.find_element(
    By.ID,
    "first-name"
).send_keys(first_name)
time.sleep(2)

checkout_last_name = driver.find_element(
    By.ID,
    "last-name"
).send_keys(last_name)
time.sleep(2)

checkout_zip = driver.find_element(
    By.ID,
    "postal-code"
).send_keys(zip_code)
time.sleep(2)

continue_button = driver.find_element(
    By.ID,
    "continue"
).click()
time.sleep(2)


# shopping_cart_item_1_data
sc_name_item_1 = driver.find_element(
    By.XPATH,
    "//div[@class='inventory_item_name']"
).text  # Sauce Labs Backpack
sc_price_item_1 = driver.find_element(
    By.XPATH,
    "//div[@class='inventory_item_price']"
).text  # $29.99
sc_total_price_item_1 = driver.find_element(
    By.XPATH,
    "//div[@class='summary_subtotal_label']"
).text  # Item total: $29.99

assert name_item_1 == sc_name_item_1
print("Shopping_cart: The product name matches! Test PASSED!")
assert price_item_1 == sc_price_item_1
print("Shopping_cart: The product price matches! Test PASSED!")
assert sc_total_price_item_1 == "Item total: " + price_item_1
print("Shopping_cart: The product total price matches! Test PASSED!")


finish_button = driver.find_element(
    By.ID,
    "finish"
).click()
time.sleep(2)

check_for_success_1 = driver.find_element(
    By.XPATH,
    "//h2[@class='complete-header']"
).text
check_for_success_2 = driver.find_element(
    By.XPATH,
    "//span[@class='title']"
).text
assert (
    check_for_success_1 == "Thank you for your order!"
    and check_for_success_2 == "Checkout: Complete!"
)
print("Order accepted! Test PASSED")


time.sleep(100)
driver.close()
