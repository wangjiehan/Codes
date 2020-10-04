import requests
from lxml import etree

# 有 api （F12检查-网络-消息头-请求网址）的直接通过api获取准json文件，得到要爬取内容
# 没有 api 的只能通过解析 html （.xpath()）来获取
# 有问题可能性：
# （1）url 错误，requests 没法 get 到正确的 html
# （2）requests 得到的 html 信息有问题。利用 Postman 可以查看 ide 能够获得的 html
# 若浏览器中的 html 是全的，ide 中 get 不全，有可能是内容需要渲染，在浏览器中渲染过后才可见。
# 此时若想得到完整 html，则需要先进行渲染（另一个技术）

# 全商品列表页面的 headers，右键 检查，在 Network 中的 Request Headers 中找
# headers中要去掉 Host 内容，否则后面的 url 会失效，每次请求都是针对该 Host
header1 = {# 'Host': 'search.jd.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': '__jda=122270672.1809641807.1536580026.1545972887.1545991662.106; __jdu=1809641807; shshshfp=be31d6021d95254ef6191a0acc5c2df6; shshshfpa=71c24ee2-1802-3acb-0528-d5c7bbbf3ec9-1536591067; shshshfpb=096fc8291d4d56d115cc17819f5554a288b0b31d13d7400065b9684da6; qrsc=3; unpl=V2_ZzNtbRJSQBx3CENQch5YVmICF1tKURETdgEUA3JOXw1mAhAOclRCFXwURldnGlUUZwoZXEtcQRZFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHIYVAJiAxtcRGdzEkU4dlJzEFUNVwIiXHIVF0l8CERTeB0RBW4CGlpHV0oUczhHZHg%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_a4283145865b404797c728cf8f29003b|1545991714151; user-key=c3dc4d4e-9cb3-47ed-b330-9e845b957539; cn=1; xtest=7010.cf6b6759; ipLoc-djd=7-412-415-0; mt_xid=V2_52007VwMbU1VfV1oWSB9sAWNTQlRdX1tGTRsQXxliV0cBQVBSXEpVEVQGNQYRBwhYAA8XeRpdBW4fElFBW1dLH00SXwVsAhFiX2hSahZNHFwDbwsRUVRbUVIaQRBZAWAzEldbXw%3D%3D; ipLocation=%u5317%u4EAC; areaId=7; PCSYCityID=2; __jdc=122270672; rkv=V0200; 3AB9D23F7A4B3C9B=ICISS54UQSVOOK4HE3CPLKQ7KKZOXERRHZO74U3JSDJMODOCYKYM2MRPPJZZIOH33GHSTHD7UJHDRSVTVBXTAWTSDQ',
    'Upgrade-Insecure-Requests': '1'}

# 具体商品的 headers
header2 = {# 'Host': 'mercury.jd.com',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'aud=462c70118f70a454d7b0963e6a9b50ff; aud_ver=2; __jdu=1932902214; shshshfpa=c26a6e73-e6ec-d88e-261a-9880a47a153c-1548058817; shshshfpb=mhm6y2iGSgw0%2F0vhd5xRiow%3D%3D; user-key=c1bc6fbe-6bd7-4b9a-9872-97d7acd003b0; cn=0; ipLoc-djd=1-72-2799-0; unpl=V2_ZzNtbRADEB10XBIELEtZAmIFRw1LBBMRJlhOBnwcWgJgURYKclRCFX0UR1dnGV4UZwcZWUVcQxxFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsRXgZvAhFeQlJzJXI4dmR8HV4MYQUiXHJWc1chVEBdextZBSoDGl9BX0IWdghDZHopXw%3d%3d; __jda=122270672.1932902214.1535776195.1548297459.1550044578.5; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ceb90eeafc4647da8ba5ba9c64766c5f|1550044578497; avt=5; PCSYCityID=2; 3AB9D23F7A4B3C9B=AVWGXMEHFT3Z5JPGBXIFZHZW4P6GKYF5HXW5QLFFD4TR5C5JWULMS6MC7BEQCXMSNUCQYDCML324PZWBCI2XO4ZTLE; _gcl_au=1.1.925623948.1550045649; shshshfp=a47dd26228773465bb83b894ac6eab4e; mt_xid=V2_52007VwMaUF5QU1kcSRxsUDcKFlJYCwFGT0gYVBliCxsFQQtaXh1VS1lQYVNHBl1YBwkdeRpdBW8fE1FBWFBLH04SWABsBhNiX2hSahZOHV0NZgMVWltbWlgdSBFbDGUzEldbXw%3D%3D; shshshsID=41a9292856998be714ee889b0dacd0f1_22_1550049489435; __jdb=122270672.22.1932902214|5.1550044578; asn=21',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

class JdData:
    def __init__(self):
        # 评论的格式化 api，所需参数：productid、score（评论从好到差：从5到1）、page
        self.url = 'https://sclub.jd.com/comment/productPageComments.action?productId=%s&score=%s&sortType=5&page' \
                   '=%s&pageSize=10'

    @staticmethod
    def getId(keyword):
        # 全商品列表第 1 页的 url
        url = 'https://search.jd.com/Search?keyword=%s&page=%d' % (keyword, 1)
        res = requests.get(url, headers=header1)
        # print(res.text)       # html 信息

        # 把 html 信息存到 etr 中
        etr = etree.HTML(res.text)

        # 从 etr 中定位信息，提取商品id，为以后获取差评的api做铺垫
        # // 代表相对路径。div是要定位的开头，定位条件为 class=xxxx
        # 要搜索的内容为 /a/ 目录下的 href 内容（即href=后面的内容）
        # 如果不是 关键词（href）=内容，则将 @href 换成 text()
        # id_array = etr.xpath('//div[@class="p-name p-name-type-2"]/a/@href')
        id_array = etr.xpath('//li[@class="gl-item"]/@data-sku')     # 和上条一样效果，但上条要url.split(".")[-2].split("/")[-1]处理一下
        # print(id_array)
        return id_array

    # 差评api，对差评内容查看 检查，Network中
    def get_negative_eval(self, id_):
        ret = []
        # noinspection PyBroadException
        try:
            res = requests.get(self.url % (id_, 1, 0))
            print(self.url % (id_, 1, 0))
            s = res.json()
        except:
            return self.get_negative_eval(id_)
        max_page = s['maxPage']
        if max_page:
            for i in range(max_page):
                try:
                    res = requests.get(self.url % (id_, 1, i))
                    s = res.json()
                except:
                    continue
                try:
                    evs = s['comments']
                except:
                    continue
                for ev in evs:
                    ret.append(ev['content'])
        return ret
    def main_eval(self, ids):
        for i, id_ in enumerate(ids):
            print(i + 1, id_)
            # noinspection PyBroadException
            try:
                int(id_)
            except:
                continue
            jr = dict()
            jr['negative_%s' % id_] = self.get_negative_eval(id_)
            # print self.get_negative_eval(id_)
            import json
            with open('%s.json' % id_, 'w') as f:
                json.dump(jr, f)


if __name__ == '__main__':
    j = JdData()
    keywords =['bra']
    for i in keywords:
        print(i)
        ids_ = j.getId(i)
        print(ids_)
        j.main_eval(ids_)

