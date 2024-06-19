import time


from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.select import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alertwindow=driver.switch_to.alert
time.sleep(3)
print(alertwindow.text)
alertwindow.send_keys("Manohar")
# alertwindow.accept()
alertwindow.dismiss()
time.sleep(5)
