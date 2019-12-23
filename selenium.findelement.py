from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome
import re #regular expressions, are imported from python directly

browser = webdriver.Firefox()
#browser.get('http://google.com')
browser.get('https://www.alibaba.com/product-detail/Fancytech-D18-BT-Smart-Watch-Phone_60868480869.html?spm=a27aj.11912869.0.0.52331462WFjEjq')

try: 
    ## Extract Price of the variable.
    theid = browser.find_element_by_class_name('priceVal').text 
    title = browser.find_element_by_class_name('ma-title').text
    companyname = browser.find_element_by_class_name('company-name-container').text
    suppt = browser.find_element_by_class_name('card-central-logo').text  

    print('ID:', theid)
    print('Title:', title)
    print('Supplier Company Name:', companyname)
    print('Supplier type:', suppt)
except Exception as ex:
    print("ID Didn't work", format(ex))   

###QUESTION! 
    #FIND: Price2, price 3, price 4
try:
    #<span class="priceVal" title="$5.27" data-spm-anchor-id="a2700.wholesale.maonnacta.i0.c2247898L3LwGj">$5.27</span>
    #<span class="priceVal" title="$5.07" data-spm-anchor-id="a2700.wholesale.maonnacta.i1.c2247898L3LwGj">$5.07</span>
    theid = browser.find_element_by_class_name('priceVal').text 
except Exception as ex:
    print("ID Didn't work", format(ex))   
#browser.close()      
