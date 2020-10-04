#!/usr/bin/env python
#coding=utf-8

import pymysql
import urllib
import urllib.request
import re
import os

from urllib.parse import quote
import string

db = pymysql.connect(
	host = 'rm-uf6h0d6x74xv514n1ao.mysql.rds.aliyuncs.com',
	user = 'root',
	password = 'BCxTYzgCxSYL2Td2',
	database = 'qtt',
	charset = 'utf8mb4',
	)
cursor = db.cursor()


def get_pic(content):
	# 匹配到第一张图
	# 加 ? 是防止贪婪匹配
	# reg = r'http://[\S]*jpg'		# 只能匹配出最终为 .jpg 的图片
	reg = r'img .*[^>]'		# 无扩展名、.png格式都能匹配出来
	reg_2 = r'http://[^\s"]*("|\s)'
	
	pattern = re.compile(reg)
	pattern_2 = re.compile(reg_2)
	
	html = pattern.search(content)
	try:
		html = html.group(0)
		html = pattern_2.search(html)
		html = html.group(0)[:-1]
	except Exception as e:
		print("None can be matched!")
		return None
	else:
		return html

# 从 url 中获取 jpg 的 html
def open_html(url):
	# 防止读取url时 ASCII 编码问题报错
	url = urllib.parse.quote(url, safe=string.printable)
	
	require = urllib.request.Request(url)
	reponse = urllib.request.urlopen(require)
	html = reponse.read()
	return html

# 通过 jpg 的 html 获取图片并下载
def load_image(html, download_path, pic_name):
	photo = open_html(html)
	with open(download_path + pic_name, 'wb') as f:
		f.write(photo)
		f.close()

if __name__ == "__main__":
	
	sql = """SELECT content FROM `aiw_read_article`"""
	# sql = """SELECT content FROM `aiw_read_article` WHERE `index` = 32"""
	try:
		cursor.execute(sql)
		results = cursor.fetchall()

	except:
		print ("Error: unable to fetch data")
	else:
		for i, element in enumerate(results):
			html = get_pic(str(element))
			# print(html)
			if html:
				subfolder = i // 5000 + 1
				pic_name = "/%s/%d.jpg" % (str(subfolder), i + 1)
				pic_path = "/data/res/pic" + pic_name
				
				sql_update = """UPDATE aiw_read_article SET pic = '%s' WHERE `index` = '%s'""" % (pic_path, (i + 1))
				try:
					cursor.execute(sql_update)
					db.commit()
					print("Success in filling the picture path where `index` = %d" % (i + 1))
				except:
					db.rollback()

	db.close()

