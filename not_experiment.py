from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
bios=[];
nk=open('dsdwc.txt','w',encoding='utf-8')
nk1=open('dsvdp.txt','w',encoding='utf-8')
driver.get("https://www.ordhekdeen.com/biodatas/10002/");
time.sleep(5);
driver.get("https://www.ordhekdeen.com/biodatas/");
time.sleep(10);
driver.find_element_by_css_selector('a.selector').click();
lie=driver.find_elements_by_css_selector('li');
for l in lie:
    if l.text=='পাত্রের বায়োডাটা':
        l.click();
        break
driver.find_element_by_css_selector(".button.radius").click()
for j in range(1,218):
    driver.get("https://www.ordhekdeen.com/biodatas/?upage={}".format(j))
    b=driver.find_elements_by_tag_name("h4")
    for u in b:
        bio=u.text.split('\n')[1];
        nk1.write(bio+'\t')
        bios.append(bio)
ps=nk1.readlines()[0].split("\t")
nk1.close()
bios=ps[:1759]
for i in bios:
    driver.get("https://www.ordhekdeen.com/biodatas/{}".format(i))
    #data_no=driver.find_elements_by_css_selector("div#item-header-avatar.twelve.columns.image-hover")
    own1=driver.find_elements_by_class_name("bp-field-name")
    own2=driver.find_elements_by_class_name("bp-field-value")
    own3=driver.find_elements_by_class_name("each-pii")
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
        if len(k)<3:continue
        mn=k.split('\n')[0]
        gf=k.replace(mn,'')
        gt=gf.replace('\n','')
        if mn in jh:
            lebels[mn]=gt;
    for lk in lebels.keys():
        nk.write("'"+lk+"'"+"\t"+"'"+lebels[lk]+"'"+"\t")
nk.close()
driver.quit()
