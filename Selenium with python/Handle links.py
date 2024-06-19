import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Digital downloads').click()

# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find number of links in a page
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))

# print all links with text
for link in links:
    print(link.text)


time.sleep(5)
driver.close()