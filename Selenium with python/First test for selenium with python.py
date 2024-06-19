
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
serv_obj=Service("C:\Mano har\Drivers\geckodriver.exe")
driver= webdriver.Firefox(service=serv_obj)
##driver=webdriver.Firefox()
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1425706449%3A1688193957998118&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AeDOFXjCMEnNeDhxhOP9kxxtyKGLbF1phoss_M72XtpYd_FHQqUHIS2eaE5_WwntNcbTalI4j7E&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
#driver.find_element_by_name("a-input-text a-span12 auth-autofocus auth-required-field").send_keys("manoharnambaru@gmail.com")
#driver.find_element(By.NAME,"a-spacing-small").click()
driver.find_element(By.NAME,"identifierId").send_keys("manoharnambaru@gmail.com")
#driver.find_element_by_id("password").send_keys("gjfdkg ")
driver.find_element(By.ID,"ap_password").send_keys("jgfksdjg")
driver.find_element_by_id("signInSubmit").click()
#driver.find_element(By.ID,"signInSubmit").click()
act_title=driver.title
exp_title="amazon.in"
if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
    driver.close()






from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://accounts.google.com")
driver.maximize_window()
print(driver.title)
driver.close()
