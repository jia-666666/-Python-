#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/27'
"""
import operator
import pandas as pd
data=pd.read_csv('../file/CSV/手机_评价.csv')
#------------------------------------------------------------------------------
# 第一步：日期读取及统计
#------------------------------------------------------------------------------
day_list = {}
for item in data['评价时间']:
    if item not in day_list:
        day_list.update({item:1})
    else:
        day_list[item] +=1
#字典升序排序
day_list=sorted(day_list.items(),key=operator.itemgetter(0),reverse=False)
#print(day_list)

# #------------------------------------------------------------------------------
# # 第二步：年份及月份处理及统计
# #------------------------------------------------------------------------------
month_list={}
year_list={}
for time in day_list:
    #print(time)
    day=str(time[0])
    k=str(day).split('-')
    year=k[0]
    month=k[0]+'-'+k[1]
    if year not in  year_list:
        year_list.update({year:time[1]})
    else:
        year_list[year]+=time[1]
    if month not in  month_list:
        month_list.update({month:time[1]})
    else:
        month_list[month]+=time[1]

# print(year_list)
# print(month_list)

# #------------------------------------------------------------------------------
# # 第三步：绘制图形
# #------------------------------------------------------------------------------

import matplotlib.pyplot as plt


plt.figure(figsize=(16,8))
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号


#
# 绘图
p1=plt.subplot(122)

plt.plot(list(month_list.keys()),list(month_list.values()))
plt.xticks(rotation=-90) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('销售量')
plt.title('月份销量图')

#显示数字
for a, b in zip(list(month_list.keys()),list(month_list.values())):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)

plt.sca(p1)


# plt.show()




#------------------------------------------------------------------------------
# 第二步：绘制柱状图
#------------------------------------------------------------------------------
p2=plt.subplot(121)
plt.bar(list(year_list.keys()),list(year_list.values()))
plt.xticks(rotation=-90) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('销售量')
plt.title('年份销量图')

# 显示数字
for a, b in zip(list(year_list.keys()),list(year_list.values())):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)
plt.sca(p2)
plt.savefig('../file/PNG/20月份销售图.png')
plt.show()



#------------------------------------------------------------------------------
#：文件保存
#------------------------------------------------------------------------------
# n='data.CSV'
# with open(n,'a+',encoding='utf-8') as f:
#     for i in day_list:
#         #print(day_list[0][0])
#         f.write(str(i)+','+str(day_list[i])+'\n')
