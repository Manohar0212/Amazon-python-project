from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("http://www.automationpractice.pl/")
sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))