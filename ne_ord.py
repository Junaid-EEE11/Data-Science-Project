from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
options = Options()
#options.headless = True
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\pythone\geckodriver.exe', options=options)
#driver = webdriver.Firefox(options=options)
bios=[];
#nk=open('dsdw.txt','w',encoding='utf-8')
driver.get("https://www.ordhekdeen.com/biodatas/")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,'a.selector').click()
lie=driver.find_elements(By.CSS_SELECTOR,'li')
for l in lie:
	if l.text=='পাত্রের বায়োডাটা':
		l.click()
		break
driver.find_element(By.CSS_SELECTOR,".button.radius").click()
