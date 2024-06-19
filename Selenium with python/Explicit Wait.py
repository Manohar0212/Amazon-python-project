from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# mywait=WebDriverWait(driver,10)# explicit wait condition
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
driver.get("https://www.google.com/")
driver.maximize_window()
searchBox=driver.find_element(By.NAME,"q")
searchBox.send_keys("selenium")
searchBox.submit()
searchlink=mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[normalize-space()='Selenium']"))
searchlink.click()







