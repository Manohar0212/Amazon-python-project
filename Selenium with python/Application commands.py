# Application commands:
# get- Opening the url of the application
# title- To capture the title of the page
# current_url-To capture the current url of the page
# page_source_To capture the source code of the page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("http://www.automationpractice.pl/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()

