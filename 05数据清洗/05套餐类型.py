#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
#------------------------------------------------------------------------------
# 第一步：连接数据库
# - 初始化数据库连接，使用pymysql模块
# - MySQL的用户：root, 密码:123456, 端口：3306,数据库：test
# - 查询语句，选出phone_assess表中的所有数据
# - read_sql_query的两个参数: sql语句， 数据库连接
# - 按照颜色分组统计数据
# - 数据转字典，获取每个色系及统计数量
#------------------------------------------------------------------------------

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

sql = ''' select id,package_type from phone_assess; '''

colors = pd.read_sql(sql, engine)

group_Count = colors.groupby('package_type').count()

color_sum=group_Count.to_dict()['id']


#------------------------------------------------------------------------------
# 第二步：绘制柱状图
#------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

index=list(color_sum.keys())#获取字典的键值对的前键
data=list(color_sum.values())#获取字典的键值对的后键（值）

# 绘图
plt.figure(figsize=(10,4))
plt.bar(index,data)
plt.xticks(rotation=-0) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('销售量')
plt.title('套餐类型销量关系图')


for a, b in zip(list(index), list(data)):# 显示数字
    plt.text(a,b,b, ha='center', va='bottom', size=10)    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小

plt.grid(linestyle='-.')#显示栅格线
plt.savefig('../file/PNG/22套餐类型销量关系图.png')#保存图片
plt.show()#显示图片



