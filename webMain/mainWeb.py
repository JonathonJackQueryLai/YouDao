#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 10:49
# @Author  : @乌鸦坐飞机
# Description   : web
import tornado.ioloop
from  tornado import web
from SpiderData.translation import Spider
# from .. import SpiderData
# from ..SpiderData.post import car
# try:
#     from ..SpiderData.post import car
# except Exception: #ImportError
#     from ..SpiderData import post

class MainHandler(web.RequestHandler):
    # def __init__(self,title):
    #     self.title = '乌鸦坐飞机'
    def get(self):
        self.render("maoMi.html")

settings = {
    'template_path':'template',
    'static_path' : 'static',
}
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/index',Spider)
    ],**settings)
    application.listen(9999)
    tornado.ioloop.IOLoop.current().start()




