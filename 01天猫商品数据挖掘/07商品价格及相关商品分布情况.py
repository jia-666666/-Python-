#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/24'
"""

import pandas as pd


# 读取数据
#n = time.strftime("%Y-%m-%d") + "bak.CSV"
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)

data=list(data['价格'])

price_1000,price_2000,price_3000,price_4000,price_5000,price_6000,price_more =0,0,0,0,0,0,0
for i in data:
    i=int(i)
    if i<1000:
        price_1000+=1
    elif i<2000:
        price_2000+=1
    elif i<3000:
        price_3000+=1
    elif i<4000:
        price_4000+=1
    elif i<5000:
        price_5000+=1
    elif i<6000:
        price_6000+=1
    else:
        price_more+=1



import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号


nume=['0_1000','1000_2000','2000_3000','3000_4000','4000_5000','5000_6000','6000+']
sales=[price_1000,price_2000,price_3000,price_4000,price_5000,price_6000,price_more ]
# 绘图
plt.figure(figsize=[10,6])
#plt.bar(names, nums, width=0.3, color='green')
plt.bar(nume,sales, width=0.3, color='green')

# 设置标题
plt.xlabel("价格", fontproperties='SimHei', size=12)
plt.ylabel("商品数量", fontproperties='SimHei', rotation=90, size=12)
plt.title("价格商品关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(nume), fontproperties='SimHei', rotation=0, size=10)

plt.grid(linestyle='-.')
# 显示数字
for a, b in zip(list(nume), list(sales)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)

plt.savefig('../file/PNG/03价格区间分布图.png')
plt.show()
