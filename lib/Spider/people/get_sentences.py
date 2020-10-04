import requests
from lxml import etree

# 全商品列表页面的 headers，右键 检查，在 Network 中的 Request Headers 中找
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'BAIDUID=AF80FC8993112AADB5475B90948F1614:FG=1; BIDUPSID=AF80FC8993112AADB5475B90948F1614; PSTM=1535352595; BDUSS=RGMllXQWZHNGx0WUg2S1hYV3dJYzJObE91VlFkeVdValRQN2RNT3ZRVjFrMjljQVFBQUFBJCQAAAAAAAAAAAEAAAAT9MMyZnJlZXdpbmQyMDEzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHUGSFx1BkhcTW; H_PS_PSSID=1425_21113_18560_28413_22072; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
'Host': 'eclick.baidu.com',
'Referer': 'https://pos.baidu.com/wh/o.htm?ltr=',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

class PeopleData:
    def __init__(self):
        # 评论的格式化 api，所需参数：productid、score（评论从好到差：从5到1）、page
        self.url = 'https://sclub.jd.com/comment/productPageComments.action?productId=%s&score=%s&sortType=5&page' \
                   '=%s&pageSize=10'

    @staticmethod
    def getId():
        # 全商品列表第 1 页的 url
        url = 'http://bj.people.com.cn/n2/2019/0213/c82837-32633891.html'
        res = requests.get(url, headers=header)
        print(res.text)       # html 信息

        # 把 html 信息存到 etr 中
        etr = etree.HTML(res.text)

        id_array = etr.xpath('//div[@class="box_con"]/@data-sku')     # 和上条一样效果，但上条要url.split(".")[-2].split("/")[-1]处理一下
        # print(id_array)
        return id_array

if __name__ == '__main__':
    j = PeopleData()
    print(j.getId())

