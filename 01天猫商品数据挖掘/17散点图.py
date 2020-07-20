#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/24'
"""
import time
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)
data.fillna(value=0,inplace=True)

huawei,xioami,sanxing,apple,vivo,oppo,other=0,0,0,0,0,0,0
for item in data['商品名']:
    #print(item)
    if '华为' in item:
        huawei+=1
    elif '小米' in item:
        xioami+=1
    elif '三星' in item:
        sanxing+=1
    elif '苹果' in item:
        apple+=1
    elif 'vivo' in item:
        vivo+=1
    elif 'oppo' in item:
        oppo+=1
    else:
        other+=1

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#获取数据

names = ['华为','小米','三星','苹果','VIVO','OPPO','其他']
nums = [huawei,xioami,sanxing,apple,vivo,oppo,other]


# 绘图
plt.figure(figsize=[10,6])
#plt.bar(names, nums, width=0.3, color='green')
plt.scatter(names, nums)
plt.xlabel("售价（元）")
plt.ylabel("销量（件）")
plt.grid(linestyle='-.')
plt.show()

#------------------------------------------------------------------------------
# 颜色控制符
#------------------------------------------------------------------------------

# 字符	颜色
# # 'b'	blue
# # 'g'	green
# # 'r'	red
# # 'c'	cyan 青色
# # 'm'	magenta平红
# # 'y'	yellow
# # 'k'	black
# # 'w'	white

#------------------------------------------------------------------------------
# 线条控制符  https://www.cnblogs.com/zyg123/p/10504633.html
#------------------------------------------------------------------------------
#
# 字符	类型
# '-'	实线
# '--'	虚线
# '-.'	虚点线
# ':'	点线
# ' '	空类型，不显示线
#
#
# '.'	点
# ','	像素点
# 'o'	原点
#
#
# '^'	上三角点
# 'v'	下三角点
# '<'	左三角点
# '>'	右三角点
#
#
# '1'	下三叉点
# '2'	上三叉点
# '3'	左三叉点
# '4'	右三叉点
#
#
# 's'	正方点
# 'p'	五角点
# '*'	星形点
# 'h'	六边形1
# 'H'	六边形2
#
#
# '+'	加号点
# 'x'	乘号点
# 'D'	实心菱形点
# 'd'	细菱形点
# '_'	横线点
# '|'	竖线点

#------------------------------------------------------------------------------
# 风格
#------------------------------------------------------------------------------

# color="green" 指定颜色为绿色
# linestyle="dashed" 指定线形为dashed类型
# marker="o" 指定标记类型为o点
# markerfacecolor="blue"指定标记的颜色为蓝色
# markersize=20 指定标记的大小为20

# plt.plot(x, y1, "-P")
# plt.plot(x, y2, "-|")
# plt.plot(x, y3, color="#000000")
# plt.plot(x, y4, "-o", markersize=20)
# plt.plot(x, y5, "-^", markerfacecolor="blue")