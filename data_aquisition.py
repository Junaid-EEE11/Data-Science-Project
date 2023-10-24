from selenium import webdriver;import time
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
driver=webdriver.Chrome()
id_no=["22090"]
driver.get("http://apps.dpdc.org.bd:7001/apex/f?p=101:46:14656442490954::NO:::")
driver.find_element_by_id("P101_USERNAME").send_keys("gmict")
driver.find_element_by_id("P101_PASSWORD").send_keys("gmict")
driver.find_element_by_id("P101_LOGIN").click()
time.sleep(5)
driver.find_element_by_id("R127787112802140703_search_field").send_keys("{}".format(id_no[0]))
driver.find_element_by_id("R127787112802140703_search_button").click()
time.sleep(7)
driver.find_element_by_css_selector("img").click()
driver.switch_to.window(driver.window_handles[1])

data_empl=pd.read_html(driver.find_element_by_class_name("c25").get_attribute('outerHTML'))
dat=driver.find_elements_by_class_name("c41").get_attribute('outerHTML')
data_job=pd.read_html(dat[0])
data_foren=pd.read_html(dat[2])
#data[0].to_excel("hdjs.xlsx")
