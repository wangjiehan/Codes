import requests
from lxml import etree
from urllib.request import quote
from setting import jd_headers


class JdData:

    def __init__(self):
        self.url = 'https://sclub.jd.com/comment/productPageComments.action?productId=%s&score=%s&sortType=5&page' \
                   '=%s&pageSize=10'

    @staticmethod
    def get_ids(keyword):
        urls = ['https://search.jd.com/Search?keyword=%s&enc=utf-8&page=%s' % (quote(keyword), i) for i in xrange(40)]
        ids = []
        for url in urls:
            print(url)
            res = requests.get(url=url, headers=jd_headers)
            et = etree.HTML(res.text)
            ids += et.xpath('//li[@class="gl-item"]/@data-sku')
        return list(set(ids))

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
        p_ret = set(range(max_page))
        while len(p_ret):
            p = list(p_ret)[0]
            # noinspection PyBroadException
            try:
                res = requests.get(self.url % (id_, 1, p))
                s = res.json()
                p_ret.remove(p)
            except:
                continue
            try:
                evs = s['comments']
            except:
                p_ret.remove(p)
                continue
            for ev in evs:
                ret.append(ev['content'])
        return ret

    def main_eval(self, ids):
        for ind, id_ in enumerate(ids):
            print(ind, id_)
            # noinspection PyBroadException
            try:
                int(id_)
            except:
                continue
            jr = dict()
            jr['negative_%s' % id_] = self.get_negative_eval(id_)
            # print self.get_negative_eval(id_)
            import json
            with open('eval_total_jd_new/%s.json' % id_, 'w') as f:
                json.dump(jr, f)


if __name__ == '__main__':
    j = JdData()
    ps =['苹果', '华为', '中兴', 'HTC手机', '酷派', '一加手机', '诺基亚', 'oppo手机', 'vivo手机', '三星手机', '魅族', '努比亚手机', '360手机手机']
    for p in ps:
        print(p)
        ids_ = j.get_ids(p)
        print(ids_)
        j.main_eval(ids_)

