# -*- coding: utf-8 -*-bu
"""
Created on Wed May 19 11:51:19 2021

@author: joukey
"""

import requests as req
from bs4 import BeautifulSoup


res = req.get('https://mutualfunds.com/screener/')
soup = BeautifulSoup(res.text, 'html.parser')

span_tags = soup.find_all('a')

for tag in span_tags:
    print(tag)
    
#%%

import os
import selenium

dir_path = __file__.rfind('\\')
dir_path = __file__[:dir_path]
os.chdir(dir_path)

from selenium import webdriver
browser = webdriver.Chrome('./chromedriver.exe')
#%%
browser.get("https://mutualfunds.com/screener")
button = browser.find_element_by_css_selector('button.m-table-pagination-page-button')