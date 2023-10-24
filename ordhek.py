from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
bios=[];
nk=open('dsdw.txt','w',encoding='utf-8')
nk1=open('dsdp.txt','w',encoding='utf-8')
driver.get("https://www.ordhekdeen.com/biodatas/")
time.sleep(10)
driver.find_element_by_css_selector('a.selector').click()
lie=driver.find_elements_by_css_selector('li')
for l in lie:
    if l.text=='পাত্রীর বায়োডাটা':
        l.click()
driver.find_element_by_css_selector(".button.radius").click()
for j in range(1,192):
    driver.get("https://www.ordhekdeen.com/biodatas/?upage={}".format(j))
    b=driver.find_elements_by_tag_name("h4")
    for u in b:
        bio=u.text.split('\n')[1];
        nk1.write(bio)
        bios.append(bio)
nk1.close()
for i in bios:
    driver.get("https://www.ordhekdeen.com/biodatas/{}".format(i))
    #data_no=driver.find_elements_by_css_selector("div#item-header-avatar.twelve.columns.image-hover")
    own1=driver.find_elements_by_class_name("bp-field-name")
    own2=driver.find_elements_by_class_name("bp-field-value")
    own3=driver.find_elements_by_class_name("each-pii")
    nk.write('bio no:{}'.format(i)+'\n')
    for jo,na in zip(own1,own2):
        nk.write(jo.text+'\n'+na.text+'\n');
    for yd in own3:
        nk.write(yd.text+'\n');
nk.close()
driver.quit()
