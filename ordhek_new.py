from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
options = Options()
options.headless = True
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\pythone\geckodriver.exe', options=options)
bios=[];
nk=open('dsdw111.txt','w',encoding='utf-8')
nk1=open('dsdp.txt','w',encoding='utf-8')
nk2=open('datasa.txt','r',encoding='utf-8')
jh=[gf.replace("\n","") for gf in nk2.readlines()]
if len(bios)<2:
    driver.get("https://www.ordhekdeen.com/biodatas/10002/");
    time.sleep(5);
    driver.get("https://www.ordhekdeen.com/biodatas/");
    time.sleep(10);
    driver.find_element(By.CSS_SELECTOR,'a.selector').click();
    lie=driver.find_elements(By.CSS_SELECTOR,'li');
    for l in lie:
        if l.text=='পাত্রের বায়োডাটা':
            l.click();
            break
    driver.find_element(By.CSS_SELECTOR,".button.radius").click();
    for j in range(1,706):
        driver.get("https://www.ordhekdeen.com/biodatas/?upage={}".format(j))
        b=driver.find_elements(By.TAG_NAME,"h4");
        for u in b:
            bio=u.text.split('\n')[1];
            nk1.write(bio+'\t')
            bios.append(bio)
nk1.close()
nk1=open('dsdp.txt','r',encoding='utf-8')
ps=nk1.readlines()[0].split("\t")
bios=ps[:]
for i in bios:
    driver.get("https://www.ordhekdeen.com/biodatas/{}".format(i))
    #data_no=driver.find_elements_by_css_selector("div#item-header-avatar.twelve.columns.image-hover")
    own1=driver.find_elements(By.CLASS_NAME,"bp-field-name");
    own2=driver.find_elements(By.CLASS_NAME,"bp-field-value");
    own3=driver.find_elements(By.CLASS_NAME,"each-pii");
    nk.write("\n"+'bio no:{}'.format(i)+'\t')
    for jo,na in zip(own1,own2):
        nk.write(jo.text+'\t'+na.text+'\t');
    if len(own1)<13:
        nk.write('mising\t'*2*(13-len(own1)))
    kj=[jh.text for jh in own3];
    lebels=dict();
    for i in jh:
        lebels[i]="missing";
    for k in kj:
        if len(k)<3: continue
        mn=k.split('\n')[0]
        gf=k.replace(mn,'')
        gt=gf.replace('\n','')
        if mn in jh:
            lebels[mn]=gt;
    for lk in lebels.keys():
        nk.write("'"+lk+"'"+"\t"+"'"+lebels[lk]+"'"+"\t")
nk.close()
driver.quit()
