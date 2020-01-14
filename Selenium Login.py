from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome
import time
import re #regular expressions, are imported from python directly
import pandas as pd 


#open browser
driver = webdriver.Firefox()
driver.get('https://www.ssactivewear.com/')
time.sleep(3)
#close popup
driver.find_element_by_id("ltkpopup-close-button").click()
time.sleep(2)
#account login
driver.find_element_by_class_name('btn2').click()
time.sleep(3)
driver.find_element_by_id("M_M_zEmailTB").send_keys('predictstore@predictvia.com')
time.sleep(2)
driver.find_element_by_id('M_M_zPasswordTB_CLND').click()
time.sleep(2)
driver.find_element_by_id('M_M_zPasswordTB').send_keys('Isapass321')
time.sleep(2)
driver.find_element_by_id('M_M_zPageLoginBTN_CD').click()

#get brands webpage
listaurl = []
driver.get('https://www.ssactivewear.com/brands')
for element in driver.find_elements_by_class_name('brand'):
  xx = element.find_element_by_tag_name("a").get_attribute("href")
 # print(xx)
  listaurl.append(xx)

#print('Esta es la lista:', listaurl)
print('quinto link:', listaurl[5])

#add new tab (NOT WORKING)
body = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get(listaurl[5])
time.sleep(2)

#Getting article price and name
#driver.get('https://www.ssactivewear.com/ps/alternative?Page=1')
#for element1 in driver.find_elements_by_class_name('i'):
 # print(element1.text)
  #yy = element1.find_element_by_tag_name('ins').text
  #print(yy)

#Getting article price and name at big Scale
clurl = 0
pbn_list=[]
for element in listaurl:
  print(listaurl[clurl])
  driver.get(listaurl[clurl])
  clurl = clurl + 1
  
  for element1 in driver.find_elements_by_class_name('i'):
    #print(type(element1.text))
    #print(element1.text)
    mystr = element1.text
    mytup = tuple(mystr.splitlines())
    pbn_list.append(mytup)
    #print(mytup)
    #exit()
#print(pbn_list)
df_pbn = pd.DataFrame(pbn_list)
df_pbn.columns = ['Price', 'Brand', 'Name', 'None']
print(df_pbn)
exit()


