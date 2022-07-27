from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.recursion.com/careers?gh_jid=4343702"

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(link)
time.sleep(1)

driver.switch_to.frame(driver.find_element(By.ID, "grnhse_iframe"))

why_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/form/div[2]/div[7]/label/textarea')
why_box.send_keys("I hear the tech talks are pretty good :)")

time.sleep(100)

driver.quit()
