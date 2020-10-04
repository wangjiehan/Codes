# coding=utf-8
import requests
import re  # 正则表达式
import bs4  # Beautiful Soup 4 解析模块
import urllib.request  # 网络访问模块
import News  # 自己定义的新闻结构
import codecs  # 解决编码问题的关键 ，使用codecs.open打开文件
import sys  # 1解决不同页面编码问题
import importlib
import socket
import time

importlib.reload(sys)


# 从首页获取所有链接
def GetAllUrl(home):
    html = urllib.request.urlopen(home).read().decode('utf8')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    pattern = 'http://www.ziliaoku.org/rmrb/[\d\S].*?'
    links = soup.find_all('a', href=re.compile(pattern))
    for link in links:
        url_set.add(link['href'])


def GetAllUrlL(home):
    html = urllib.request.urlopen(home).read().decode('utf8')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    pattern = 'http://www.ziliaoku.org/rmrb/[\d\S].*?'
    links = soup.find_all('a', href=re.compile(pattern))
    for link in links:
        url_set1.add(link['href'])


def GetNews(url, i):
    response = requests.get(url)
    html = response.text
    article = News.News()
    try:
        article.title = re.findall(r'<h2 id=".*?">(.+?)</h2>', html)
        article.content = re.findall(r'<div class="article">([\w\W]*?)</div>', html)

        t = ""
        for j in article.title:
            t += str('标题：' + j + '\n')
        c = ""
        for m in article.content:
            c += str(m)
        article.content1 = '　' + '\n'.join(c.split(' ')).strip()

        file = codecs.open('/tmp/luo/news ' + str(i) + '.txt', 'w+')
        file.write(t + "\t" + article.content1)
        file.close()
        print('ok')
    except Exception as e:
        print('Error1:', e)
    response.close()


def GetAllUrlK(home, i):
    html = urllib.request.urlopen(home).read().decode('utf8')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    pattern = 'http://www.ziliaoku.org/rmrb/[\d\S].*?'
    link = soup.find('a', href=re.compile(pattern))
    link1 = link['href']
    print(link1)
    GetNews(link1, i)

t_default = 10
socket.setdefaulttimeout(t_default)
url_set = set()  # url集合
url_set1 = set()  # url集合
home = 'http://www.ziliaoku.org/rmrb?from=groupmessage&isappinstalled=0'
GetAllUrl(home)
try:
    for d in url_set:
        GetAllUrlL(d)
        print(d)
    i = 0
    for b in url_set1:
        i = i + 1
        print(b)
        GetAllUrlK(b, i)
        time.sleep(20)
except Exception as e:
    print('Error:', e)

# home = 'http://www.ziliaoku.org/rmrb/1984-06-21'
# i = 10
# GetAllUrlK(home,i)
