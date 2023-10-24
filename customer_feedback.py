import random
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://dpdc.org.bd/site/home_gov/customer_feedback/-")
id_no=range(5717889,5718000,1)
for i in id_no:
    f1=random.choice(['01','02','03'])
    f2=random.choice(['01','02','03'])
    driver.find_element(By.ID,"TOKEN_NO").clear()
    driver.find_element(By.ID,"TOKEN_NO").send_keys(i)
    driver.find_element(By.CSS_SELECTOR,"input[type='radio'][name='BEHAVE_FEEDBACK_ID'][value='{}']".format(f1)).click()
    driver.find_element(By.CSS_SELECTOR,"input[type='radio'][name='SERVICE_FEEDBACK_ID'][value='{}']".format(f2)).click()
    driver.find_element(By.ID,"pm-contact-form-btn").click()
driver.close()
