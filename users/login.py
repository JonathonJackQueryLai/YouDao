#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 15:34
# @Author  : @乌鸦坐飞机
# Description   : 登录
import tornado.web
class LoginHandler(tornado.web.RequestHandler):    #登录
    def get(self):
        self.render('08login.html',error=None)
    def post(self):
        username = User.by_name(self.get_argument('name',''))
        passwd = self.get_argument('password','')
        if username and username[0].password == passwd:
            self.render('08sqlalchemy.html',
                        username=username[0].username
                        )
        else:
            self.render('08login.html',error='登陆失败')



