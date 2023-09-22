import os
import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
FACEBOOK = os.environ.get("FACEBOOK")

chrome_driver_path = "C:\development\chromedriver-win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://tinder.com/')

time.sleep(10)

accept_cookies = driver.find_element(By.XPATH, '//*[@id="q-881491550"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()

login = driver.find_element(By.XPATH, '//*[@id="q-881491550"]/div/div[1]/div/main/div['
                                      '1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(10)
facebook_login = driver.find_element(By.XPATH, '//*[@id="q1685094670"]/main/div[1]/div/div[1]/div/div/div[2]/div['
                                               '2]/span/div[2]/button/div[2]/div[2]')
facebook_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

fb_email_input = driver.find_element(By.ID, 'email')
fb_email_input.send_keys(EMAIL)

fb_pass_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_pass_input.send_keys(PASSWORD)

time.sleep(10)
submit_fb_credentials = driver.find_element(By.ID, 'loginbutton')
submit_fb_credentials.click()

driver.switch_to.window(base_window)

time.sleep(10)
allow_location = driver.find_element(By.XPATH, '//*[@id="q1685094670"]/main/div/div/div/div[3]/button[1]')
allow_location.click()
notification = driver.find_element(By.XPATH, '//*[@id="q1685094670"]/main/div/div/div/div[3]/button[1]')
notification.click()

# liking people

for n in range(90):
    time.sleep(20)
    print("called")
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys(Keys.RIGHT)

