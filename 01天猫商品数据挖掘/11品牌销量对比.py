#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/24'
"""
import time
import pandas as pd


# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)
data.fillna(value=0,inplace=True)


huawei,xioami,sanxing,apple,vivo,oppo,other=0,0,0,0,0,0,0
for item,num in zip(data['商品名'],data['销量']):
    if '华为' in item:
        huawei+=num
    elif '小米' in item:
        xioami+=num
    elif '三星' in item:
        sanxing+=num
    elif '苹果' in item:
        apple+=num
    elif 'vivo' in item:
        vivo+=num
    elif 'oppo' in item:
        oppo+=num
    else:
        #print(item)
        other+=num



#------------------------------------------------------------------------------
# 第二步：绘制柱状图
#------------------------------------------------------------------------------
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
plt.bar(names,nums, width=0.3, color='green')

# 设置标题
plt.xlabel("品牌", fontproperties='SimHei', size=12)
plt.ylabel("销量", fontproperties='SimHei', rotation=90, size=12)
plt.title("品牌-销量关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(names), fontproperties='SimHei', rotation=-0, size=10)
# 显示数字
for a, b in zip(list(names), list(nums)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)

plt.grid(linestyle='-.')
plt.savefig('../file/PNG/10品牌销量关系图.png')
plt.show()
