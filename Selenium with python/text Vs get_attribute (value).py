# text:It always returns inner text of the element
# get_attribute: It always returns values of any attribute of web element


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2Fapple-macbook-pro-13-inch")
# emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
# emailbox.send_keys("manohar0212@gmail.com")
# print("Result of text:",emailbox.text)
# print("Result of get_attribute:",emailbox.get_attribute('value'))
button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text:",button.text)
print("result of get_attribute:",button.get_attribute('value'))
