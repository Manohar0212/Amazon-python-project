import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://demo.nopcommerce.com/")
#######---find_element()-Returns single web element
# 1)Locator matching with single web element
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Samsung Series 9 NP900X4C Premium Ultrabook")
# time.sleep(20)
# element.click()
# driver.close()
#2) Locator matching with multiple web elements
# element=driver.find_element(By.XPATH,"//a[normalize-space()='Sitemap']")
# print(element.text)
##########----findelements-----######
# 10
# 1)Locator matching with single web element
# element=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(element))
# print(element[0].send_keys("Samsung Series 9 NP900X4C Premium Ultrabook"))
#2)Locator matching with multiple web element
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))#23
# print(elements[3].text)
# for ele in elements:
# print(ele.text)
# 3)No such element exception
# elements=driver.find_elements(By.LINK_TEXT,'ico-log')
# print("elements returned:",len(elements))

