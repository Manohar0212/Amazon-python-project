import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.select import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
alloptions = Select(driver.find_element(By.XPATH, "//select[@id='Skills']"))

# Select option from dropdown
alloptions.select_by_visible_text("APIs")
# alloptions.select_by_value("2")
# alloptions.select_by_index(4)

# To print all options
# option = alloptions
# print("Total options:", len(alloptions))  # lenth of the options(Number)

# print text of the all options
# for opt in alloptions:
#     print(opt.text)
#
# #  select options from dropdown without using built-in method
for opt in alloptions:
   if opt.text=="Book":
       opt.click()
       break


time.sleep(10)
driver.close()
