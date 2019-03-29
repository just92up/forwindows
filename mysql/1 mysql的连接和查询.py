#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author :qinyu
import pymysql
conn = pymysql.connect(
    host='47.107.170.114',
    port=3306,
    user='root',
    passwd='bestbest',
    db='reading',
    charset='utf8'
)
cur = conn.cursor()


def read():
    sql = 'select * from dushu where id = 2'
    cur.execute(sql)
    res = cur.fetchall()
    for i in res:
        print(i)

    cur.close()
read()