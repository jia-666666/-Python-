#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

# 连接database
conn = pymysql.connect(
host="127.0.0.1",
user ="root",
password ="123456",
database ="test",
charset ="utf8mb4")

# 获取一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 将结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = """
        CREATE TABLE if not exists phone(
            id INT auto_increment PRIMARY KEY ,
            shop_name text ,
            shop_link varchar(100) NOT NULL ,
            title TEXT NOT NULL,
            price int NOT NULL,
            sale int NOT NULL default 0,
            province char(3) NOT Null
        )ENGINE=innodb DEFAULT CHARSET=utf8mb4;
    """

cursor.execute(sql)  # 执行SQL语句

import re
def execute_sql():
    f = open('../file/CSV/智能手机-all-bak.csv', 'r', encoding='UTF-8', )
    #跳过第一行
    next(f)
    line = f.readlines()  # 读取一行文件，包括换行符
    for i in line:
        k = i.split(',')
        #print(k[0], k[1], k[2],k[3],k[4],k[5])
        if k[4]=='':#销量为空时默认为0
            k[4]=0
        try:
            cursor.execute("insert into phone(shop_name,shop_link,title,price,sale,province) values(%s,%s,%s,%s,%s,%s)",
                           (k[0], k[1], k[2], k[3], k[4], k[5]))
            conn.commit()

        except Exception as e:
            print(e)
        # finally:
        #     pass
print('正常进行数据导入操作，请等候（预计10s）')
execute_sql()

cursor.close()  # 关闭光标对象
conn.close()  # 关闭数据库连接
print('导入操作完成')