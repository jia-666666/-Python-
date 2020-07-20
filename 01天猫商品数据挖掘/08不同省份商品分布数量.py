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

total_data = {}
for item in data['省份']:
    #print(item)
    if item not in total_data:
        #向字典中更新每个省份默认0病例
        total_data.update({item:1})
    else:
        total_data[item]+=1
print(total_data)
#------------------------------------------------------------------------------
# 第二步：绘制柱状图
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#获取数据

names = total_data.keys()
nums = total_data.values()
print(names)
print(nums)

# 绘图
plt.figure(figsize=[10,6])
#plt.bar(names, nums, width=0.3, color='green')
plt.bar(names,nums, width=0.3, color='green')

# 设置标题
plt.xlabel("省份", fontproperties='SimHei', size=12)
plt.ylabel("店铺数量", fontproperties='SimHei', rotation=90, size=12)
plt.title("省份店铺关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(names), fontproperties='SimHei', rotation=-40, size=10)
# 显示数字
for a, b in zip(list(names), list(nums)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)

plt.grid(linestyle='-.')
plt.savefig('../file/PNG/07省份店铺关系.png')
plt.show()
