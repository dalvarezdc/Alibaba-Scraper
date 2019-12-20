#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome

browser = webdriver.Chrome('/home/daniel/Documents/chromedriver')
#browser = webdriver.Firefox()
browser.get('https://www.alibaba.com/product-detail/Portable-Small-USB-Travel-LED-Makeup_60830030133.html?spm=a2700.details.maylikever.2.1fb53cc2uSVPvx')
#browser.get('https://selenium.dev/documentation/en/')
browser.maximize_window()
elem = browser.find_element_by_id("a2700.details.tabs.i0.2de37f6d29FMJH")
#elem = browser.find_element_by_id("search-by")
#elem.text
print('this is element', elem)
print('TEXT this is element', elem.text)


#elem = browser.find_element_by_link_text('W3C WebDriver specification')
#elem.click()
#<input data-search-input="" id="search-by" type="search" placeholder="Search..." autocomplete="off">
#<span class="tab-name" title="Company Profile" data-spm-anchor-id="a2700.details.tabs.i0.2de37f6d29FMJH">Company Profile</span>
