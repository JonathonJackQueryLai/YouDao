#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 20:29
# @Author  : @乌鸦坐飞机
# Description   : 爬取有道的资料
import requests,json,hashlib,time,random
import tornado.web
class Spider(tornado.web.RequestHandler):
    def __init__(self):
        # self.word = word
        # self.salt = self.salt()
        # self.sign = self.sign()
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/'

    # def salt(self):
    #     return
    # def sign(self):
    #     return
    def post(self,word):
        salt = str(int(time.time() * 1000) + random.randint(1, 10))
        sign = hashlib.md5(('fanyideskweb' + word + salt + 'ebSeFb%=XZ%T[KZ)c(sy!').encode()).hexdigest()
        data = {'i': word, 'client': 'fanyideskweb', 'from': 'AUTO', 'to': 'AUTO', 'doctype': 'json',
            'action': 'FY_BY_REALTIME', 'typoResult': 'false', 'version': '2.1', 'smartresult': 'dict',
            'keyfrom': 'fanyi.web', 'salt': salt, 'sign': sign, }
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,mt;q=0.8', 'Connection': 'keep-alive', 'Content-Length': '240',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;', # 'Host': 'fanyi.youdao.com',
            # 'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
            # 'X-Requested-With': 'XMLHttpRequest'
        }
        html = requests.post(url=self.url, data=data, headers=header)
        result = json.loads(html.text)
        translateword = result['translateResult'][0][0]['src']
        translateResult = result['translateResult'][0][0]['tgt']
        smartResult = result['smartResult']['entries']

        # print('翻译结果：{0}'.format(translateResult))
        # print('完整的结果：')
        smartResultlist = ''
        for i in smartResult:
            if i != '':
                smartResultlist += i
        return (translateword,translateResult,smartResultlist)
        # print(smartResult)
        # print(result)








