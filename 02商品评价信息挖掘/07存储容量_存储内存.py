#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
n = '../file/CSV/手机_评价.csv'
data = pd.read_csv(n)
#print(data['评价时间']['2020'])

#所有数据
total_data = {}
for item in data['存储容量']:
    item = str(item).split('（')[0]
    if item=='128GB':
        item='8+'+item
    elif item=='64GB':
        item='6+'+item
    elif item=="32GB":
        item='4+'+item
    elif item=="512GB":
        item='12+'+item
    elif item == "256GB":
        item = '8+' + item

    #字符格式整理
    k = item.split('+')
    k[0]=k[0].replace('GB','').replace('G','')
    k[1] = k[1].replace('B','')
    item = k[0] + '+' + k[1]

    if item not in total_data:
        total_data.update({item:0})
        total_data[item] += 1
    else:
        total_data[item] +=1
print(total_data)





#
ROM_data={}
RAM_data = {}
for i in total_data:
    k = str(i).split('+')
    #运行内存处理
    k[0]=k[0].replace('G', '').replace('B', '')+'GB'
    if k[0] not in ROM_data:
        ROM_data.update({k[0]:0})
        ROM_data[k[0]] += total_data[i]
    else:
        ROM_data[k[0]]+=total_data[i]
    #机身内存处理
    if k[1] not in RAM_data:
        RAM_data.update({k[1]: 0})
        RAM_data[k[1]] += total_data[i]
    else:
        RAM_data[k[1]] += total_data[i]

# print(RAM_data)
# print(ROM_data)
#




import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

names=list(RAM_data.keys())
nums=list(RAM_data.values())
# 绘图
plt.figure(figsize=(10,4))
plt.bar(names,nums)
plt.xticks(rotation=-90) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('销售量')
plt.title('存储内存销量关系图')

# 显示数字
for a, b in zip(list(names), list(nums)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)
plt.grid(linestyle='-.')
plt.savefig('../file/PNG/15机身内存销量关系图.png')
plt.show()
