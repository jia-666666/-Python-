#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import pymysql

# 连接database
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test",
    charset="utf8mb4")

# 获取一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 将结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 创建评价表（id，网络类型，机身颜色，套餐类型，存储容量，版本类型，评价内容，评价时间）
sql = """
        CREATE TABLE if not exists phone_assess(
            id INT auto_increment PRIMARY KEY ,
            Network_type varchar(30) ,
            body_color varchar(30) NOT NULL ,
            package_type TEXT NOT NULL,
            storage_capacity varchar(30) NOT NULL,
            version_type varchar(30) NOT NULL,
            evaluation_content Text NOT Null,
            evaluation_time Date
        )ENGINE=innodb DEFAULT CHARSET=utf8mb4;
    """

cursor.execute(sql)  # 执行SQL语句


def execute_sql():
    f = open('../file/CSV/手机_评价.csv', 'r', encoding='UTF-8', )
    # 跳过第一行
    next(f)
    line = f.readlines()  # 读取一行文件，包括换行符
    for i in line:
        k = i.split(',')
        print((k[0],k[1],k[2],k[3],k[4],k[5]),k[6])
        try:
            cursor.execute(
                "insert into phone_assess"
                "(Network_type,body_color,package_type,storage_capacity,version_type,evaluation_content, evaluation_time)"
                " values(%s,%s,%s,%s,%s,%s,%s)",
                (k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
            conn.commit()

        except Exception as e:
            print(e)

        # finally:
        #     pass


print('正常数据导入操作，请等候（预计10s）')
execute_sql()

cursor.close()  # 关闭光标对象


conn.close()  # 关闭数据库连接
print('导入操作完成')
