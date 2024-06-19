import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# 1)Select specific checkbox
# checkbox=driver.find_element(By.XPATH,"//input[@id='checkbox1']").click()

#2)Select all checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkbox')]")
print(len(checkboxes)) #3

# Approach 1
# for i in range(len(checkboxes)):
#        checkboxes[i].click()

# Approah 2
for checkbox in checkboxes:
    checkbox.click()


# 3)Select multiple checkboxes by choice

# for checkbox in checkboxes:
#     hobbies=checkbox.get_attribute('id')
#        if  hobbies=='Cricket' or hobbies=='Movies':
#     checkbox.click()

# Approach 3
# 4)Select last 2 checkboxes
#   range(1,3)   ---->2,3
# total number of elements-2=starting index
# for i in range(len(checkboxes)-2,len(checkboxes)) :
#      checkboxes[i].click()

# 5)select first two checkboxes
# for i in range (len(checkboxes)):
#      if i<2:
#          checkboxes[i].click()

# 6)Clearing all check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()



time.sleep(5)
driver.close()