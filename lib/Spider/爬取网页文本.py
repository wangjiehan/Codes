# -*- coding:utf-8 -*-
# 爬取网页文本
import requests
from bs4 import BeautifulSoup
def spider(url, label):
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, stream=True)
	response.encoding = "utf-8"
	data = response.text
	soup = BeautifulSoup(data, features="lxml")
	content_div = soup.find_all("div", {label: "content"})
	if content_div is not None and len(content_div) > 0:
		content = content_div[0].get_text()
		print("content: %s " % content)
		print("########################################")
		print('Success in getting information at url: %s !' % url)
		
url_class = "http://html2.qktoutiao.com/detail/2018/07/31/113729586.html"
url_id = 'http://www.136book.com/mieyuechuanheji/ewqlwb/'

spider(url_class, 'class')
spider(url_id, 'id')

