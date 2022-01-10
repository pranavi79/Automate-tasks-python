from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('ABSOLUTE PATH TO CHROMEDRIVER')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"Friend\'s Name"'

string = "MESSAGE OF YOUR CHOICE"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
for i in range(100):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1)
