from urllib import request
import os
# 获取下载url并存入数组txt中的函数
def download(filename):
	with open(filename) as obj:
		txt = obj.readlines()
	return txt
filename = 'download.txt'
txt = download(filename)

# print(os.path.dirname(os.path.realpath(__file__)))

i = 1
for url in txt:
	with request.urlopen(url) as web:
		with open(str(i)+'.mp4', 'wb') as outfile:
			outfile.write(web.read())
			outfile.close()
	i += 1
	os.path.dirname(os.path.realpath(__file__))
