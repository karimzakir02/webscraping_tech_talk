from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://goldmansachs.tal.net/vx/lang-en-GB/mobile-0/brand-2/xf-caeaaeb33c61/candidate/register"

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(link)
time.sleep(1)

first_name_box = driver.find_element(By.XPATH, '//*[@id="register_form_firstname"]')
first_name_box.send_keys("Karim")

last_name_box = driver.find_element(By.XPATH, '//*[@id="register_form_lastname"]')
last_name_box.send_keys("Zakir")

email_box = driver.find_element(By.XPATH, '//*[@id="register_form_new_user"]')
email_box.send_keys("zakirkarim02@gmail.com")

time.sleep(100)

driver.quit()
