#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/27'
"""
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
n = '../file/CSV/手机_评价.csv'
data = pd.read_csv(n)
#print(data['评价时间'])

day_list = {}
for item in data['评价时间']:
    if item not in day_list:
        day_list.update({item:1})
    else:
        day_list[item] +=1

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号
names=day_list.keys()
names=list(names)
nums=list(day_list.values())
# 绘图
plt.figure(figsize=(15,4))
plt.plot(names,nums)
plt.xticks(rotation=-90) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('评价数')
plt.title('每日评价数量趋势图')
plt.show()