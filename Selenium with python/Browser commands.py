import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
time.sleep(20)
driver.find_element(By.XPATH,"//a[normalize-space()='News']").click()
time.sleep(5)
driver.close()    #Close single browser window which is focused
driver.quit()    #Closing all browser windows and kill the entire process.