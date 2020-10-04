# -*- coding:utf-8 -*-
# 爬取并下载网页图片
import urllib
import urllib.request
import re
import os

from urllib.parse import quote
import string

# 从 url 中获取 jpg 的 html
def open_html(url):
	# 防止读取url时 ASCII 编码问题报错
	url = urllib.parse.quote(url, safe=string.printable)
	
	require = urllib.request.Request(url)
	reponse = urllib.request.urlopen(require)
	html = reponse.read()
	return html

# 通过 jpg 的 html 批量获取图片并下载
def load_image_in_batch(html, download_path):
	reg = 'http://[\S]*jpg'
	pattern = re.compile(reg)
	get_image = re.findall(pattern, repr(html))
	
	num = 1
	for img in get_image:
		photo = open_html(img)
		with open(download_path + "/%d.jpg" % num, 'wb') as f:
			print("Begin to download pictures...")
			f.write(photo)
			print("Downloading the No. %d picture..." % num)
			f.close()
		num += 1
	if num > 1:
		print("Succeed in downloading!")
	else:
		print("Fail in getting pictures!")
		
def load_image(html, download_path):
	photo = open_html(html)
	with open(download_path + "/single.jpg", 'wb') as f:
		f.write(photo)
		print("Succeed in downloading from html: %s!" % html)
		f.close()


# download_path = r"C:\Users\24299\Desktop\pic"
download_path = os.path.dirname(os.path.realpath(__file__)) + "/pic"
# print(download_path)


# html 就是 'http://www.qiqipu.com/'
# url 就是 'http://www.qiqipu.com/xxxxx.jpg'

# （1）若提供的是某个网页地址，则要先用一步 open_html(url) 从 url 中解析多条 html，
# 再让 html 进入 load_image()，再经过一步 open_html()
url = 'http://www.qiqipu.com/'
url_list = open_html(url)
load_image_in_batch(url_list, download_path)

# （2）若提供的是网页中某个图片资源地址，则直接进入 load_image()，只经过一步 open_html()
url_single = 'http://static.1sapp.com/qupost/image/20181025/11/11458a7a4f2e47b729a0f739b115c17f1044aab5water.jpg'
load_image(url_single, download_path)


