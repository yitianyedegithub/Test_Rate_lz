#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import configparser, pymysql


class OperateDB:
    def __init__(self, file_name=None, section=None):
        """
        初始化函数，用来初始化类的属性，属性不用单独写出来，直接用self.属性名就生成了
        和java的严格格式不一样，python比较宽松
        """
        if file_name:
            self.file = file_name
        else:
            self.file = '../DBTools/config.ini'
        if section:
            self.section = section
        else:
            self.section = 'test'
        self.conn = self.getConn(self.section)
        self.cursor = self.getCur()

    def getConn(self, section):
        cfg = configparser.ConfigParser()
        cfg.read(self.file, encoding='utf-8')

        sec = cfg.items(section)
        dicSec = dict(sec)
        host = dicSec['host']
        port = int(dicSec['port'])
        user = dicSec['user']
        password = dicSec['pwd']
        database = dicSec['database']
        conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        return conn

    def getCur(self):
        return self.conn.cursor()

    def searchAll(self, sql=None):
        if sql:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            print('没有sql语句！')



    def update_yty(self,sql):
        if sql:
            self.cursor.execute(sql)
            # self.conn.commit()
        else:
            print('没有sql语句！')

    #可以返回条件语句，或是赋值的语句的一部分
    def kw_link(self, link_word='AND', **kwargs):
        #隐藏使用要求：link_word 只能是',','and','or';并且只能单表查询
        link = ''
        for i in kwargs:
            '''
            where a = 1 and c = 2
            where a = 'a' and b = 'b'
            '''
            # if isinstance(kwargs[i], str):
            #     link += i + " = '" + kwargs[i] + "' " + link_word + " "
            # else:
            link += i + " = " + str(kwargs[i]) + " " + link_word + " "
        # 将最后一个多余的连接符以及前后的空格去掉
        link = link[:-len(link_word) - 2]
        # print(link)
        if link_word != ',':
            link = ' where ' + link
        return link

    #返回update语句的前半部分
    def update_sql(self, table=None, **kwargs):  # **kwargs是个字典，类似于{'dta': '1111', 'b': 'djjdje'}
        sql = 'update ' + table + ' set ' + self.kw_link(',', **kwargs)
        return sql


if __name__ == '__main__':
    odb = OperateDB()
    sql = 'select * from cases_rate'
    odb.cursor.execute(sql)
    print(odb.cursor.fetchall())
