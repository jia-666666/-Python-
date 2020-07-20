#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
df=pd.read_csv('data.csv',header=None,names=['date','num'])
#将数据类型转换为日期类型
df['date']=pd.to_datetime(df['date'])
#设置索引
df=df.set_index('date')
s=pd.Series(df['num'],index=df.index)
#print(s.head(2))
#print(df['2020-03'])
#TODO 1 按照日期筛选数据
df=df.sort_values('date')
#print(df.truncate('2020-01','2020-03'))
#print(s['2020-03-27'])
# print(df)
#TODO 2 按日期显示数据
# df_period=df.to_period('M')#按月显示，但是不统计
#
# df_period=df.to_period('Q')#按季度显示，但是不统计
# #df_period=df.to_period('A')#按年显示，但是不统计
#
# print(df_period.sum)
#print(df_period.head(20))

#TODO 统计并显示
# print(df.resample('AS').sum().to_period('A'))# 按年统计并显示
#
print(df.resample('Q').sum().to_period('Q').head())# 按季度统计并显示

print(df.resample('Q').sum().to_period('M').head(200))# 按月度统计并显示

#TODO 按年度频率显示
# print(df_period.index.asfreq('A'))# 'A'默认是'A-DEC',其他如'A-JAN'
# print(df_period.index.asfreq('A-JAN'))# 'A'默认是'A-DEC',其他如'A-JAN'

#TODO 按季度频率显示
# print(df_period.index.asfreq('Q')) # 'Q'默认是'Q-DEC',其他如“Q-SEP”，“Q-FEB”
# print(df_period.index.asfreq('Q-SEP'))# 可以显示不同的季度财年，“Q-SEP”，“Q-FEB”
# print(df_period.index.asfreq('Q-DEC') )  # 可以显示不同的季度财年，“Q-SEP”，“Q-FEB”

#print(df_period.index.asfreq('M')) # 按月份显示

#TODO 按工作日显示
# print(df_period.index.asfreq('B', how='start'))
# # print(df_period.index.asfreq('B', how='end') )


#TODO 按日期统计数据
# print(df.resample('w').sum().head())#w 周
# print(df.resample('M').sum().head())# "MS"是每个月第一天为开始日期, "M"是每个月最后一天
# print(df.resample('Q').sum().head())# "QS"是每个季度第一天为开始日期, "Q"是每个季度最后一天
# print(df.resample('AS').sum())# "AS"是每年第一天为开始日期, "A是每年最后一天

