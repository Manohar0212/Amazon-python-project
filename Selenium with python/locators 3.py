from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.facebook.com/")
driver.maximize_window()
# tag &ID
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag & class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag & attribute
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc")

# tag class & attribute
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("abc")
