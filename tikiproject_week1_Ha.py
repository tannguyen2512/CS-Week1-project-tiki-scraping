#!/usr/bin/env python
# coding: utf-8

# In[66]:


import requests
import re


# In[68]:


# request page may pha ca phe
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

r = requests.get('https://tiki.vn/may-pha-ca-phe/c1939?page=1&src=c.1882.hamburger_menu_fly_out_banner', headers=headers)


# In[69]:


# parse html into beautiful soup
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify()[:100])


# In[70]:


# scripts of all item in page 1
scripts = soup.find_all('script', {'type': 'application/ld+json'})

data = []
for i in range(1,len(scripts)-1): 
    test = str(scripts[i])

    # find product_id
    pattern = r'.*"sku":"(\d+)".*'
    product_id1 = str(re.findall(pattern, test)).strip('[')
    product_id2 = product_id1.strip(']')
    product_id = product_id2.strip("'")

    # file title
    pattern = r'"name":"(.*)","des'
    title1 = str(re.findall(pattern, test)).strip('[')
    title2 = title1.strip(']')
    title = title2.strip("'")

    # find price
    pattern = r'"price":(\d+)}'
    price1 = str(re.findall(pattern, test)).strip('[')
    price2 = price1.strip(']')
    price = price2.strip("'")

    # find image
    pattern = r'"image":"(.*g)","name'
    image_url1 = str(re.findall(pattern, test)).strip('[')
    image_url2 = image_url1.strip(']')
    image_url = image_url2.strip("'")
    
    # find product_url
    pattern = r'"url":"(.*)","image"'
    product_url1 = str(re.findall(pattern, test)).strip('[')
    product_url2 = product_url1.strip(']')
    product_url = product_url2.strip("'")

    # create data contain dict of 48 items
    d_script = {'product_id':'', 'title':'', 'price':'', 'image_url':'', 'product_url':''}
    try:
        d_script['product_id'] = product_id
        d_script['title'] = title
        d_script['price'] = price
        d_script['image_url'] = image_url
        d_script['product_url'] = product_url
        data.append(d_script)

    except:
        print("We got one article error!")
        


# In[71]:


# create dataframe
import pandas as pd
 
product = pd.DataFrame(data = data)


# In[72]:


product

