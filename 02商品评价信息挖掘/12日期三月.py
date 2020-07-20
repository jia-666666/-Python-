#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df=pd.read_csv('../file/CSV/data.csv',header=None,names=['date','num'])


#将数据类型转换为日期类型
df['date']=pd.to_datetime(df['date'])

df=df.set_index('date')

s=pd.Series(df['num'],index=df.index)

#TODO 1 按照日期筛选数据
df=df.sort_values('date')

k=df.truncate('2020-03-01')
k=k.to_dict()
names=[]
nums=[]
for o in k['num']:
    names.append((str(o))[:-9])
    nums.append(k['num'][o])




import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

# 绘图
plt.figure(figsize=(10,4))
plt.plot(names,nums)
plt.xticks(rotation=-90) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('销售量')
plt.title('三月份手机销量图')

# 显示数字
for a, b in zip(list(names), list(nums)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)

plt.grid(linestyle='-.')
plt.savefig('../file/PNG/19日期销售图.png')
plt.show()
