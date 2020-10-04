import re
import time
import json
import requests
from lxml import etree
from urllib import quote
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def get_login_cookies_code():
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://login.taobao.com/member/login.jhtml')
    time.sleep(10)
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


def get_login_cookies_user():
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')
    driver = webdriver.Chrome(chrome_options=option)
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


def crawl_eval(url, cookies):
    from setting import header
    res = requests.get(url=url % 1, headers=header, cookies=cookies)
    eva = json.loads(res.text[11:-1])['rateDetail']
    try:
        total_eva = eva['rateList']
        total_page = eva['paginator']['lastPage']
        for p in xrange(2, int(total_page)):
            print p
            res = requests.get(url=url % p, headers=header, cookies=cookies)
            eva = json.loads(res.text[11:-1])['rateDetail']
            total_eva += eva['rateList']
        return total_eva
    except:
        return


def crawl_id(keywords):
    cookies = get_login_cookies_code()
    for keyword in keywords:
        url = 'https://list.tmall.com/search_product.htm?q=' + quote(keyword)
        res = requests.get(url)
        et = etree.HTML(res.text)
        ids = et.xpath('//div[@class="product  "]/@data-id')
        print ids
        for id_ in ids:
            print id_
            second_url = 'https://detail.tmall.com/item.htm?id=%s' % id_
            res = requests.get(url=second_url, cookies=cookies)
            spuid = re.findall(r'\"spuId\"\:\".*?\"', res.text)[0].split(':')[1]
            print spuid
            sellerid = re.findall(r'sellerId\:\".*?\"', res.text)[0].split(':')[1]
            print sellerid
            third_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=%s&spuId=%s&sellerId=%s&currentPage=%s' % (id_, int(spuid[1:-1]), int(sellerid[1:-1]), '%s')
            data = crawl_eval(url=third_url, cookies=cookies)
            if data:
                with open('eval_total_tm/%s.json' % id_, 'w') as f:
                    json.dump(data, f)


if __name__ == '__main__':
    # 华为, 小米, 苹果, 酷派, 一加, 诺基亚, oppo, vivo, 三星, 魅族, 努比亚, 360手机
    # p =['华为', '小米', '苹果', '酷派', '一加', '诺基亚', 'oppo', 'vivo', '三星', '魅族', '努比亚', '360手机', '黑莓']
    p = ['华为手机', '小米手机', '苹果手机', '酷派手机', '一加手机', '诺基亚手机', 'oppo手机', 'vivo手机', '三星手机', '魅族手机', '努比亚手机', '360手机', '黑莓手机', 'HTC手机']
    crawl_id(p)
