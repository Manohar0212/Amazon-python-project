from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# driver.get("https://money.rediff.com/mutual-funds ")
# element=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/losers/bse/monthly/groupall']")
# print(element.is_displayed())    #returns true/false based on statement
# print(element.is_enabled())     # returns true/false
# ele=driver.find_element(By.XPATH,"//select[@id='plan']")
# print(ele.is_enabled())
# pwd_element=driver.find_element_by_name("password")
# print(element.is_displayed())    #returns true/false based on statement
# print(element.is_enabled())     # returns true/false
# userName_element.Send_keys("mercury")
# pwd_element.Send_keys("mercury")

# Is selected
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rd_male.is_selected())
print(rd_female.is_selected())
rd_male.click()
print("After selecting male radio button....")
print(rd_male.is_selected())
print(rd_female.is_selected())
rd_female.click()
print("After selecting female radio button")
print(rd_female.is_selected())
print(rd_male.is_selected())
