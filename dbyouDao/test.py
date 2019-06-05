#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 21:46
# @Author  : @乌鸦坐飞机
# Description   :

# class func1():
#     def __init__(self,word):
#         self.sign = '123'
#         self.word =word
#         self.salt = 'hello'
# class func2(func1):
#     def func(self):
#         print(self.word,self.sign)
# my = func2('456')
# my.func()
from dbyouDao.dbFunction import Dbfun
from SpiderData.translation import Spider

# word = myspider.post()[0]
# result = myspider.post()[1]
# smartResult = ''
# for i in myspider.post()[2]:
#     smartResult += i
# if __name__ == '__main__':
#     word = 'python'
#     myspider = Spider(word)
#     myDb = Dbfun(word)
#     if word in myDb.query_word():
#         myDb.query_word()
#     else:
#         myspider.post(word)
#         myDb.save_word(myspider.post(word))