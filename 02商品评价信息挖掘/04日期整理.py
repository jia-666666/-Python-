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

#------------------------------------------------------------------------------
# 第二步：日期格式整理及写入
#------------------------------------------------------------------------------
with open('../file/CSV/data.csv','a+',encoding='utf-8') as f:
    for i in day_list:
        f.write(str(i[0])+','+str(i[1])+'\n')
