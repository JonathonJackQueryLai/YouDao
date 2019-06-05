#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 20:55
# @Author  : @乌鸦坐飞机
# Description   : 链接数据库
import pymysql
class dbConn(object):
    def __init__(self):
        self.db_config = {
                'host': '127.0.0.1', # 告诉需要连接哪一个mysql服务器，ip一般是IP地址，localhost
                'user': 'root', # 需要用哪个用户去登入mysql
                'password': 'qwe123', #该用户的密码
                'db': 'youdao', # 指定数据库
                'charset': 'utf8' # 指定字符串
                    }
    def connect(self):
        self.con = pymysql.connect(**self.db_config)
        self.cursor = self.con.cursor()

# class db(dbConn):
#     def test(self):
#         try:
#
#             self.connect()
#             sql = "select * from translation "
#             self.cursor.execute(sql)
#             row = self.cursor.fetchall()
#             for i in row:
#                 print(i)
#         except Exception as e:
#             print(e)

# if __name__ == '__main__':
#     mydb = db()
#     mydb.test()


