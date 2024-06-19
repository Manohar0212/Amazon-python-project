import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Mano har\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
driver=webdriver.Chrome()
driver.get("https://intellipaat.com/blog/interview-question/selenium-interview-questions/")

print(driver.title)

driver.get("https://intellipaat.com/academy/")
time.sleep(5)
print(driver.title)
driver.back()

time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)