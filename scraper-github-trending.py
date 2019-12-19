import requests
from bs4 import BeautifulSoup
import json
import csv

#pasos siguientes a desarrollar
#0. Agregar variables adicionales
#1. Archivo CSV con variables
#2. Web scraping automatizado


page = requests.get('https://www.alibaba.com/product-detail/Portable-Small-USB-Travel-LED-Makeup_60830030133.html?spm=a2700.details.maylikever.2.1fb53cc2uSVPvx')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')


#v1 = soup.head.title
#print(v1)

v2 = soup.select_one('meta[property="og:price:amount"][content]')['content']
print("Min Price:",v2)

v3 = soup.select_one('meta[property="og:price:standard_amount"][content]')['content']
print("Std Price:",v3)

v4 = soup.title.string
print(v4)

###
company_name = soup.select_one('[data-aui="company-name"][title]')['title']
print("Company Name:", company_name)

### Company Product Id & Company Id
raw_content = soup.select_one('meta[name="aplus-exdata"][content]')['content']
#parse raw json
product_and_company_meta = json.loads(raw_content)
print("Product Id: ", product_and_company_meta['productId'])
print("Company Id: ", product_and_company_meta['companyId'])

###

v6 = soup.select_one('meta[name="aplus-exdata"][content]')['content']
print("v6 is",v6)    
    
###
#v7 = soup.select_one('a[class="score-lite"][content]')['content']
#print("v7 is",v7) 

###CSV
#Open file to write
with open('test1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
# write headers
    thewriter.writerow(['Company Name', 'Company Id', 'Product Id', 'Standard Price'])
#Write rows
    thewriter.writerow([company_name, product_and_company_meta['productId'], product_and_company_meta['companyId'], v3 + '$'])



#Alibaba
#<meta property="og:price:amount" content="1.89"/>
#<meta property="og:price:standard_amount" content="6.31"/>
#<meta property="og:price:currency" content="USD"/>

#<a class="company-name company-name-lite-vb" href="https://onuliss.en.alibaba.com/" target="_blank"
    #       title="Shenzhen ONULISS Technology Co., Limited" data-aui="company-name" data-domdot="id:3317">
    #        Shenzhen ONULISS Technology Co., Limited</a>

#Product and Company id
# <meta name="aplus-exdata" content='{"productId":"60769168637","companyId":"240628921"}'>

# Xpath example: /html/body/table/tbody/tr[123]
