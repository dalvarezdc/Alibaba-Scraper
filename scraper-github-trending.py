import requests
from bs4 import BeautifulSoup
import json
#pasos siguientes a desarrollar
#0. Agregar variables adicionales
#1. Web scraping automatizado
#2. Archivo CSV con variables

page = requests.get('https://www.alibaba.com/product-detail/Portable-Small-USB-Travel-LED-Makeup_60830030133.html?spm=a2700.details.maylikever.2.1fb53cc2uSVPvx')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.get_text())

#v1 = soup.head.title
#print(v1)

v2 = soup.select_one('meta[property="og:price:amount"][content]')['content']
print("v2 is",v2)

v3 = soup.select_one('meta[property="og:price:standard_amount"][content]')['content']
print("v3 is",v3)

v4 = soup.title.string
print(v4)

###
company_name = soup.select_one('[data-aui="company-name"][title]')['title']
print("v5 is", company_name)


raw_content = soup.select_one('meta[name="aplus-exdata"][content]')['content']
#parse raw json
product_and_company_meta = json.loads(raw_content)
print("Product Id: ", product_and_company_meta['productId'])
print("Company Id: ", product_and_company_meta['companyId'])

###

v6 = soup.select_one('meta[name="aplus-exdata"][content]')['content']
print("v6 is",v6)    
    
###

#v5 = soup.a.find(['class="company-name company-name-lite-vb"'])["title"]

#Alibaba
#<meta property="og:price:amount" content="1.89"/>
#<meta property="og:price:standard_amount" content="6.31"/>
#<meta property="og:price:currency" content="USD"/>

#<a class="company-name company-name-lite-vb" href="https://onuliss.en.alibaba.com/" target="_blank"
    #       title="Shenzhen ONULISS Technology Co., Limited" data-aui="company-name" data-domdot="id:3317">
    #        Shenzhen ONULISS Technology Co., Limited</a>

#Product and Company id
# <meta name="aplus-exdata" content='{"productId":"60769168637","companyId":"240628921"}'>
