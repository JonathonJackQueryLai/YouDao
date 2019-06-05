#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 16:24
# @Author  : @乌鸦坐飞机
# Description   : 首页
import tornado.web
class IndexHander(tornado.web.RequestHandler):
    def run(self):
        self.render('home.html')



