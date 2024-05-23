# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crawler
   Author :       huangkai
   date：          2024/2/22
-------------------------------------------------
"""
import datetime
from bs4 import BeautifulSoup
import requests
import re

url = "http://127.0.0.1:8888/"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }

html = requests.get(url,timeout=5 )
url_list = []
print(html)
if html.ok:
    html.encoding = 'utf8'
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup.text)
