import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\pythone\geckodriver.exe', options=options)
driver.get("https://cms.dpdc.org.bd/dpdcapp/billing/cpr_cpc_list.php")
id_no="1212121"
##for i in id_no:
driver.find_element(By.ID,"username").clear()
driver.find_element(By.ID,"username").send_keys("DPDC")
driver.find_element(By.ID,"password").clear()
driver.find_element(By.ID,"password").send_keys("DPDC"+Keys.RETURN)
##driver.find_element(By.CSS_SELECTOR,"button[type='submit'][name='BEHAVE_FEEDBACK_ID'][value='{}']".format(f1)).click()
##driver.find_element(By.CSS_SELECTOR,"input[type='radio'][name='SERVICE_FEEDBACK_ID'][value='{}']".format(f2)).click()
##driver.find_element(By.ID,"pm-contact-form-btn").click()
#driver.close()
