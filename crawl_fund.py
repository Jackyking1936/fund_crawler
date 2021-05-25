# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:00:45 2021

@author: joukey
"""

import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bts4


# connect to the us news money website with browser header

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
res = req.get('https://money.usnews.com/funds/mutual-funds/rankings/large-blend', headers=header)
#%%

# get all href
soup = bts4(res.text, 'html.parser')
all_a = soup.find_all('a')

#%%

# get the href needed by check string

target_href_ls = list()
for tag in all_a:
    target = tag.get('href')
    if target:
        if 'https://money.usnews.com/funds/mutual-funds/' in target:
            target_href_ls.append(tag.get('href'))
            
#%%

# get the holdings

h_res = req.get('https://money.usnews.com/funds/mutual-funds/large-growth/fidelity-blue-chip-growth-k6-fund/fbcgx/holdings', headers=header)
h_soup = bts4(h_res.text, 'html.parser')

tag_long_name = h_soup.find_all('h3', attrs={'class': 'Heading__HeadingStyled-sc-1w5xk2o-0-h3 gHzvTb Heading-sc-1w5xk2o-1 holdings-assembly__TableHeading-kcfwi5-1 NJLrK cVqbYe'})
for tag in tag_long_name:
    print(tag.text)
tag_short_name = h_soup.find_all('span', attrs={'class': "Span-sc-19wk4id-0 holdings-assembly__TickerSpan-kcfwi5-2 hQfOVg eAWRl"})
for tag in tag_short_name:
    print(tag.text)
#%%

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dir_idx = __file__.rfind('\\')
dir_path = __file__[:dir_idx]+'\\'

opts = Options()

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
opts.add_argument("user-agent={}".format(ua))

browser = webdriver.Chrome(dir_path+'chromedriver.exe', options=opts)
#%%
browser.get('https://money.usnews.com/funds/mutual-funds/rankings/large-blend')

js="var action=document.documentElement.scrollTop=10000"
browser.execute_script(js)
#%%

submit_button = browser.find_element_by_class_name('button-content')
submit_button.click()