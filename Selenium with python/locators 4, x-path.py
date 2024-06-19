import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("http://www.automationpractice.pl/")

 # Relative x-path
# driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-Shirts")
# driver.find_element(By.XPATH,"//*[@name='submit_search']").click()
# time.sleep(5)
# driver.close()

# OR, AND operators in relative x-path
# driver.find_element(By.XPATH,"//*[@id='search_query_top' or @name='search_query']").send_keys("T-Shirts")
# driver.find_element(By.XPATH,"//*[@name='submit_search' and @class='btn btn-default button-search']").click()
# time.sleep(5)
# driver.close()
# contains & satrt_with
# sliders=driver.find_elements(By.XPATH,"//div[contains(@id,'slider_row')]//li[3]//div[1]")
# print(len(sliders))
# text
driver.find_element(By.XPATH,"//a[text()='Popular']")

