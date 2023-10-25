from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
options = Options()
options.headless = True
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\pythone\geckodriver.exe', options=options)
#driver = webdriver.Firefox(options=options)
bios=[];
nk=open('dsdw.txt','w',encoding='utf-8')
driver.get("https://www.ordhekdeen.com/biodatas/")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,'a.selector').click()
lie=driver.find_elements(By.CSS_SELECTOR,'li')
for l in lie:
	if l.text=='পাত্রের বায়োডাটা':
		l.click()
		break
driver.find_element(By.CSS_SELECTOR,".button.radius").click()
for j in range(1,706):
	driver.get("https://www.ordhekdeen.com/biodatas/?upage={}".format(j))
	b=driver.find_elements(By.TAG_NAME,"h4")
	for u in b:
		bio=u.text.split('\n')[1];
		bios.append(bio)
for i in bios:
	driver.get("https://www.ordhekdeen.com/biodatas/{}".format(i))
	#data_no=driver.find_elements_by_css_selector("div#item-header-avatar.twelve.columns.image-hover")
	own1=driver.find_elements(By.CLASS_NAME,"bp-field-name")
	own2=driver.find_elements(By.CLASS_NAME,"bp-field-value")
	own3=driver.find_elements(By.CLASS_NAME,"each-pii")
	nk.write('bio no:{}'.format(i)+'\n')
	for jo,na in zip(own1,own2):
		nk.write(jo.text+'\n'+na.text+'\n');
	for yd in own3:
		nk.write(yd.text+'\n');
nk.close()
driver.quit()
