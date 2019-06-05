#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 22:33
# @Author  : @乌鸦坐飞机
# Description   : 别人的
import urllib.request

import urllib.parse
import json
import time
import random
import hashlib
header = {'Host': 'fanyi.youdao.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
          'Referer': 'http://fanyi.youdao.com/',
          'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
          }
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/'
# data = {}
#
# u = 'fanyideskweb'
# d = content
# f = str(int(time.time()*1000) + random.randint(1,10))
# c = 'rY0D^0\'nM0}g5Mm1z%1G4'
#
# sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
# salt = str(int(time.time()*1000) + random.randint(1,10))
# sign = hashlib.md5(('fanyideskweb' + 'hello' + salt + 'ebSeFb%=XZ%T[KZ)c(sy!').encode()).hexdigest()
i = str((int(time.time()*1000) + random.randint(1,10)))
o = hashlib.md5(('fanyideskweb' + 'hello' + i +'ebSeFb%=XZ%T[KZ)c(sy!').encode()).hexdigest()
formTable = {
    'action':'FY_BY_CLICKBUTTION',
    'client':'fanyideskweb',
    'doctype':'json',
    'from':'AUTO',
    'i': 'hello',
    'keyfrom':'fanyi.web',
    'salt': i,
    'sign': o,
    'smartresult':'dict',
    'to':'AUTO',
    'typoResult':'true',
    'version':'2.1',
}

data = urllib.parse.urlencode(formTable)
data = data.encode('ascii')
request = urllib.request.Request(url=url,data=data,method='POST',headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode())




