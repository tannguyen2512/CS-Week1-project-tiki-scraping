# -*- coding: utf-8 -*-
"""Tikiproject_week1.ipynb
"""
import requests
import re
import json
from bs4 import BeautifulSoup

# Following informations need to be extract: 
#     * Product ID
#     * Seller ID
#     * Product title
#     * Price
#     * URL of the product image
#     * URL of that product page
# Bonus information:
# * Is it TikiNow (delivery within 2 hours)
# * Is it free delivery?
# * Number of reviews?
# * How many stars or percentage of stars?
# * Does it got "badge under price" (Rẻ hơn hoàn tiền)
# * Discount percentage?
# * Does it got "shocking price" badge ?
# * Does it allowed to be paid by installments?
# * Does it comes with free gifts?


### REMEMBER: start small with page "may pha ca phe"
### BUT ONCE IT WORK, IT MUST SCRAPE DATA FROM A BIG CATEGORY

# request page may pha ca phe
def get_url_and_make_soup(url) :
    '''
    Input: URL on tiki
    Output: BeautifulSoup object of this URL
    This function take a URL from tiki, requests.get it and then parse the HTML 
    and return a corresponding BeautifulSoup object
    '''

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    r = requests.get(
        url,
        headers=headers)
    # print(r.text[:1000])

    # parse html into beautiful soup
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify()[:100])

    return soup

soup = get_url_and_make_soup('https://tiki.vn/may-pha-ca-phe/c1939?src=c.1882.hamburger_menu_fly_out_banner')

# We scrape from the script, not use this anymore
# print("\nAll occurences of the product div sections:")
# products = soup.find_all('a', {'class': 'product-item'})
# print("Type:", type(products))
# print("Number of products:", len(products))

scripts = soup.find_all('script', {'type': 'application/ld+json'})
test = scripts[1]
print(test)

# pattern = r'.*"sku":"(\d+)".*'
# print(pattern)
# sku = re.search(pattern, scripts[0].text)
# script_element = test.text.split(',')
# for i in script_element :
# print(i)
# print(script_element)
# print(script_element)

# find product_id
pattern = r'.*"sku":"(\d+)".*'
product_id = re.findall(pattern, test.text)
print(product_id)

# file title
# pattern = r'"name":"(.*)","des'
# title = re.findall(pattern, test.text)
# print(title)

# # find price
# pattern = r'"price":(\d+)}'
# price = re.findall(pattern, test.text)
# print(price)

# # find image
# pattern = r'"image":"(.*\.jpg)"'
# image = re.findall(pattern, test.text)
# print(image)