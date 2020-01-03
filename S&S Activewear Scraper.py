from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome
import re #regular expressions, are imported from python directly

driver = webdriver.Firefox()
driver.get('https://www.ssactivewear.com/')
driver.find_elements_by_class_name('ltkpopup-close')
#driver.find_elements_by_class_name('btn2').click()
#driver.find_elements_by_class_name("dxic").send_keys('predictstore@predictvia.com')

#driver.find_element_by_name('LOGIN').click()

#def ss_login():
 #   driver.get('https://www.ssactivewear.com/')
  #  driver.find_element_by_name('LOGIN').click()
    #driver.find_element_by_id('').send_keys('')
    #driver.find_element_by_id('').click()
