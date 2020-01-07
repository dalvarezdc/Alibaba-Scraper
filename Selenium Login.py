from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome
import time
import re #regular expressions, are imported from python directly

driver = webdriver.Firefox()
driver.get('https://www.ssactivewear.com/')
time.sleep(5)
driver.find_element_by_id("ltkpopup-close-button").click()
time.sleep(2)
driver.find_element_by_class_name('btn2').click()
time.sleep(3)
driver.find_element_by_id("M_M_zEmailTB").send_keys('predictstore@predictvia.com')
time.sleep(2)
driver.find_element_by_id("M_M_zPasswordTB_CLND").send_keys('Isapass321')
driver.find_element_by_id('M_M_zPageLoginBTN_CD').click()
