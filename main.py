# Automate the ordering process of Meesho

from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from xpaths import *

# ======================================================
url = 'https://www.meesho.com/reditor-20000-mah-power-banks/p/4r0xa2'
phoneNumber = "YOUR_PHONE_NUMBER"
# ======================================================

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
browser = webdriver.Chrome(options=opt)

browser.get(url)
print('URL navigated')


time.sleep(2)
browser.save_screenshot('images/1.png')
browser.find_element(By.XPATH, xpath_moreInfo).click()
print("More Information button clicked")

# ======================================================

price = browser.find_element(By.XPATH, xpath_price).text
rating = browser.find_element(By.XPATH, xpath_rating).text
productDetails = browser.find_element(By.XPATH, xpath_productDetails).text

# ======================================================
with open("output.txt", "w", encoding="utf-8") as file:
    # Write data with variable formatting
    file.write("Price of product: {}\n".format(price))
    file.write("\n\nRating of product: {}\n".format(rating))
    file.write("\n\nDetails of product: {}\n".format(productDetails))

# ======================================================
time.sleep(2)
browser.save_screenshot('images/1.png')
browser.find_element(By.XPATH, xpath_buyNow).click()
print("Buy Now button clicked")

time.sleep(2)
browser.save_screenshot('images/2.png')
browser.find_element(By.XPATH, xpath_phoneNumber).send_keys(phoneNumber)
print("Phone number inserted")

time.sleep(2)
browser.save_screenshot('images/3.png')
browser.find_element(By.XPATH, xpath_continueBtnLogin).click()
print("Continue button clicked")

time.sleep(20)
browser.save_screenshot('images/4.png')
browser.find_element(By.XPATH, xpath_selectDeliveryAddress).click()
print("Select Delivery address button in Address tab clicked")


time.sleep(2)
browser.save_screenshot('images/5.png')
browser.find_element(By.XPATH, xpath_deliverToThisAddress_).click()
print("Deliver to this address button in Address tab clicked")

time.sleep(2)
browser.save_screenshot('images/6.png')


browser.find_element(By.XPATH, xpath_continueBtn_payment).click()
print("Continue button in Payment tab clicked")

time.sleep(2)
browser.save_screenshot('images/7.png')
browser.find_element(By.XPATH, xpath_placeOrder).click()
print("Place Order button clicked")

# ======================================================
time.sleep(50)
browser.close()

