from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options)
bios=[];
nk=open('dgg.txt','w',encoding='utf-8')
nk1=open('dsdgfdf.txt','w',encoding='utf-8')
nk2=open('patro.txt','r',encoding='utf-8')
leb=nk2.readlines()
lbl=[k.replace('\n','') for k in leb]
lebels=dict();
driver.get("https://www.ordhekdeen.com/biodatas/")
time.sleep(10)
driver.find_element_by_css_selector('a.selector').click()
lie=driver.find_elements_by_tag_name('a')
for l in lie:
    if l.text=='পাত্রের বায়োডাটা':
        l.click()
driver.find_element_by_css_selector(".button.radius").click()
for j in range(1,2):
    driver.get("https://www.ordhekdeen.com/biodatas/?upage={}".format(j))
    b=driver.find_elements_by_tag_name("h4")
    for u in b:
        bio=u.text.split('\n')[1];
        nk1.write(bio+'\t');
        bios.append(bio)
nk1.close()
for i in bios:
    driver.get("https://www.ordhekdeen.com/biodatas/{}".format(i));
    #data_no=driver.find_elements_by_css_selector("div#item-header-avatar.twelve.columns.image-hover")
    own1=driver.find_elements_by_class_name("bp-field-name");
    own2=driver.find_elements_by_class_name("bp-field-value");
    own3=[jh.text for jh in driver.find_elements_by_class_name("each-pii")];
    nk.write('bio no:{}\n'.format(i))
    for jo,na in zip(own1,own2):
        nk.write(jo.text+'\n'+na.text+'\n');
    if len(own1)<13:
        nk.write('missing\n'*(26-len(own3)));
    for yd in own3:
        jhk=yd.split("\n")[0];
        kjp=yd.replace(jhk,'')
        kjp=kjp.replace('\n','')
        for lp in lbl:
            if jhk in lp:
                lebels[lp]=kjp;
    for gh in lebels.keys():
        nk.write(gh+'\n'+lebels[gh]+'\n');
nk.close()
driver.quit()
