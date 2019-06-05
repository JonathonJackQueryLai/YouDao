#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 20:23
# @Author  : @乌鸦坐飞机
# Description   : 数据库
import pymysql
from dbyouDao.dbConnection import dbConn
from SpiderData.translation import Spider
#连接mysql需要用到的参数
class Dbfun(dbConn):
    def get_word_by_name(self, word):
        try:
            self.connect()
            sql = "SELECT * FROM translation WHERE word = '%s'"%(word)
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            self.con.commit()
            if row:
                return row

        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.con.close()
    def save_word(self, arg):
        try:
            self.connect()
            sql = "INSERT  INTO translation VALUES('{word}', '{result}', '{smartResult}', now());".format(word=arg[0],result=arg[1],smartResult=arg[2])
            self.cursor.execute(sql)
            self.con.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.con.close()


if __name__ == '__main__':
    myspider = Spider()
    arg = myspider.post('virtual')

    mydd =Dbfun()
    print(mydd.get_word_by_name('python'))
    print(mydd.save_word(arg))






