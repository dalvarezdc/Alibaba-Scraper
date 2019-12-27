from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome
import re #regular expressions, are imported from python directly
import linkGrabber # first install #pip install linkGrabber 


browser = webdriver.Firefox()
#browser.get('http://google.com')
#original: browser.get('https://www.alibaba.com/product-detail/Fancytech-D18-BT-Smart-Watch-Phone_60868480869.html?spm=a27aj.11912869.0.0.52331462WFjEjq')

# test 2: browser.get('https://www.alibaba.com/product-detail/Fancytech-Q18-BT-Sports-Wear-Touch_60868034466.html?spm=a2700.wholesale.deiletai6.6.c2247898qB2PRj')
#Test 3:
browser.get('https://www.alibaba.com/product-detail/Notebook-15-6-i7-8550U-16G_62428654263.html?spm=a27aq.13274681.9336958460.88.64ae30dedOqkkP')



try: 
    ## Variables Extraction 
     
    title = browser.find_element_by_class_name('ma-title').text
    companyname = browser.find_element_by_class_name('company-name-container').text
    suppt = browser.find_element_by_class_name('card-central-logo').text  
    pscore = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div[4]/div[2]/div/a').text
    theprice = browser.find_element_by_class_name('priceVal').text
    
    print('Product Score:', pscore)
    print('Price:', theprice)
    print('Title:', title)
    print('Supplier Company Name:', companyname)
    print('Supplier type:', suppt)
except Exception as ex:
    print("ID Didn't work", format(ex))   

###QUESTION! 
    #FIND: Price 2, price 3, price 4
try:
    #<span class="priceVal" title="$5.27" data-spm-anchor-id="a2700.wholesale.maonnacta.i0.c2247898L3LwGj">$5.27</span>
    #<span class="priceVal" title="$5.07" data-spm-anchor-id="a2700.wholesale.maonnacta.i1.c2247898L3LwGj">$5.07</span>
    theid = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[5]/div[2]/ul/li[2]/div[3]/span').text
    #region = browser.find_elements_by_class_name('field-content-wrrap').__getattribute__('title')
     #   Return getattr(self, title)
    shipping = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div[1]/div/ul/li[2]/span[2]').text

    print('Price 2:', theid)
except Exception as ex:
    print("ID Didn't work", format(ex))   



#browser.close()      
