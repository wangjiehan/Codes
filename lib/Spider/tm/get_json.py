import re
import time
import json
import requests
from lxml import etree
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

print("Running from", os.path.dirname(os.path.realpath(__file__)))

chromedriver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver\chromedriver.exe")

# jsonp 转 json
def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')

def get_login_cookies_code():
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')
    driver = webdriver.Chrome(chrome_options=option, executable_path=chromedriver_path)
    driver.get('https://login.taobao.com/member/login.jhtml')
    time.sleep(30)
    # scan two dimension by mobile taobao
    if 'login' in driver.current_url:
        driver.quit()
        return get_login_cookies_code()
    cookies = driver.get_cookies()
    driver.quit()
    ck = dict()
    for cookie in cookies:
        ck[cookie['name']] = cookie['value']
    return ck

# 滑块
def get_login_cookies_user():
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')
    driver = webdriver.Chrome(chrome_options=option, executable_path=chromedriver_path)
    driver.get('https://login.taobao.com/member/login.jhtml')
    driver.find_element_by_xpath('//i[@class="iconfont static"]').click()
    user = driver.find_element_by_xpath('//input[@type="text"]')
    user.send_keys('13034050406')
    password = driver.find_element_by_xpath('//input[@type="password"]')
    password.send_keys('cpp')
    drag = driver.find_element_by_id('nc_1_n1z')
    action = ActionChains(driver)
    for index in range(500):
        # noinspection PyBroadException
        try:
            action.drag_and_drop_by_offset(drag, 500, 0).perform()
        except:
            break
        time.sleep(1)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    if 'https://i.taobao.com/my_taobao.htm' not in driver.current_url:
        return get_login_cookies_user()
    cookies = driver.get_cookies()
    ck = dict()
    for cookie in cookies:
        ck[cookie['name']] = cookie['value']
    return ck

# 获取一个商品的 json 数据
# x = loads_jsonp(res_.text)
# maxpage = x["rateDetail"]["paginator"]["lastPage"]
# comments = x["rateDetail"]["rateList"][0]["rateContent"]
def get_js_data(url, cookies):
    from setting import header
    # 先爬该商品的第一页评论，获取评论总页数
    res = requests.get(url=url % 1, headers=header, cookies=cookies)
    # print(res.text)
    eva = json.loads(res.text[11:-1])['rateDetail']     # [11:-1] 切片相当于jsonp 转 json，也可以直接用 loads_jsonp()函数
    try:
        total_eva = eva['rateList']
        total_page = eva['paginator']['lastPage']
        for p in range(2, int(total_page)):
            # print(p)
            res = requests.get(url=url % p, headers=header, cookies=cookies)
            eva = json.loads(res.text[11:-1])['rateDetail']
            total_eva += eva['rateList']
        return total_eva
    except Exception as e:
        print(e)


def main(keywords):
    cookies = get_login_cookies_code()
    # print(cookies)
    for keyword in keywords:
        time.sleep(30)
        try:
            os.mkdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "jsonfile/digital/%s" % keyword))
        except FileExistsError:
            pass
        print("Preparing for %s" % keyword)
        url = 'https://list.tmall.com/search_product.htm?q=' + quote(keyword)
        res = requests.get(url)
        et = etree.HTML(res.text)
        ids = et.xpath('//div[@class="product  "]/@data-id')
        print(ids)
        for id_ in ids:
            # print(id_)
            # 二级 url，该商品的详情页
            second_url = 'https://detail.tmall.com/item.htm?id=%s' % id_
            res = requests.get(url=second_url, cookies=cookies)
            spuid = re.findall(r'\"spuId\"\:\".*?\"', res.text)[0].split(':')[1]
            # print(spuid)
            sellerid = re.findall(r'sellerId\:\".*?\"', res.text)[0].split(':')[1]
            # print(sellerid)

            # 通过 id_, spuid 和 sellerid 获取 api
            # 三级 url，即 api，记录该商品信息的 json 文件
            third_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=%s&spuId=%s&sellerId=%s&currentPage=%s' % (id_, int(spuid[1:-1]), int(sellerid[1:-1]), '%s')
            # 获取一个商品的 json 数据
            js_data = get_js_data(url=third_url, cookies=cookies)
            if js_data:
                with open('jsonfile/digital/%s/%s.json' % (keyword, id_), 'w') as f:
                    json.dump(js_data, f)
                    time.sleep(5)


if __name__ == '__main__':
    # p = ['华为手机', '小米手机', '苹果手机', '酷派手机', '一加手机', '诺基亚手机', 'oppo手机', 'vivo手机', '三星手机', '魅族手机', '努比亚手机', '360手机', '黑莓手机', 'HTC手机']
    # p = ["ONLY", "Vero Moda", "伊芙丽", "欧时力", "太平鸟", "哥弟", "丽丽", "Five Plus", "Teenie Weenie", "摩安珂", "音儿", "ZARA", "拉夏贝尔"]
    # p = ["雅诗兰黛", "阿芙", "美潮", "欧舒丹", "肌肤之钥", "茵芙莎", "糖果小姐", "资生堂", "娇韵诗", "倩碧", "海蓝之谜", "兰蔻", "苏秘37°", "玉兰油", "自然堂", "欧莱雅", "兰芝"]
    # p = ["联想笔记本", "华硕笔记本", "戴尔笔记本", "华为笔记本", "苹果笔记本", "小米笔记本", "惠普笔记本", "ThinkPad", "荣耀笔记本", "神舟笔记本", "宏碁笔记本", "微软笔记本", "炫龙笔记本", "火影笔记本", "雷蛇笔记本", "清华同方笔记本", "雷神笔记本", "中柏笔记本"]
    # p = ["机械键盘", "鼠标", "游戏手柄", "组装电脑"]
    p = ["移动硬盘"]

    main(p)
