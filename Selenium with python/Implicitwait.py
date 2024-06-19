import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()
searchBox=driver.find_element(By.NAME,"q")
searchBox.send_keys("selenium")
searchBox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.close()





