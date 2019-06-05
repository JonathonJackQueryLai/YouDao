# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:28:46 2018

@author: 14414
"""
import json
import urllib.request
import urllib
import time, random, hashlib
class Youdao:
    def __init__(self,url):
        self.url = url 
        self.header = {'Host': 'fanyi.youdao.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
          'Referer': 'http://fanyi.youdao.com/', 'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
          }
        self.header['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        
        self.header['Accept-Language'] = 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'
        self.header['Connection'] = 'keep-alive'
        self.header['X-Requested-With'] = 'XMLHttpRequest'
        self.header['Origin'] = 'http://fanyi.youdao.com'
        self.header['Referer'] = 'http://fanyi.youdao.com/'
        self.header['Cookie'] = 'OUTFOX_SEARCH_USER_ID=-1645744815@10.169.0.84; JSESSIONID=aaa9_E-sQ3CQWaPTofjew; OUTFOX_SEARCH_USER_ID_NCOO=2007801178.0378454; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=' + str(int(time.time()*1000))
    def post(self):
        keyword = input('请输入你要翻译的单词：')
        
        datajoin = {'i': keyword,
                'client': 'fanyideskweb',
                'from': 'AUTO',
                'to': 'AUTO',
                'doctype': 'json',
                'action': 'FY_BY_REALTIME',
                'typoResult': 'false',
                'version': '2.1',
                'smartresult': 'dict',
                'keyfrom': 'fanyi.web',
                }
        request = urllib.request.Request(self.url, headers=self.header)
        datajoin['salt'] = str(int(time.time()*1000) + random.randint(1,10))
        # sign: o, o = md5('fanyideskweb' + t + i + 'ebSeFb%=XZ%T[KZ)c(sy!')
        datajoin['sign'] = hashlib.md5(('fanyideskweb' + keyword + datajoin['salt'] + 'ebSeFb%=XZ%T[KZ)c(sy!').encode()).hexdigest()
        # print(datajoin)
        data = urllib.parse.urlencode(datajoin)
        data = data.encode('ascii')
        webopener = urllib.request.urlopen(request, data=data)
        print(webopener.status)
        result = json.loads(webopener.read().decode())
        src = result['translateResult'][0][0]['src']
        tgt = result['translateResult'][0][0]['tgt']
        print('\033[5;31;40m翻译结果为:{0}!\033[0m'.format(tgt))
        print(result)
if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/'
    myTranslate = Youdao(url)
    myTranslate.post()
