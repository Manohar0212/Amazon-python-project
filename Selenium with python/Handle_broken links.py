import time

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver  = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("http://www.deadlinkcity.com/")
alllinks=driver.find_elements(By.TAG_NAME,'a')
print(len(alllinks))

# finding broken links
count=0
for link in alllinks:
   url=link.get_attribute('href')
   try:
       res=requests.head(url)
   except:
       None
   if res.status_code>=400:
    count+=1
    print(url, "is broken link")
   else:
    print(url, "is valid link")
    print("total number of broken links:", count)
