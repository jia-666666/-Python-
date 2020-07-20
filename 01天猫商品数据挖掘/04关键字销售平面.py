#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/24'
"""
import time
import pandas as pd


#----------------------------------------------读取数据----------------------------------------------
# 读取数据
#n = time.strftime("%Y-%m-%d") + "bak.CSV"
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)
data_sales=data['销量']
#查看数据维度（行，列）
#print(data.shape)

#取出商品标题，区域，价格，销售四个维度的数据
#data=data[['商品名','价格','销售','省份']]



#对每个标题进行分词，使用jieba分词

#----------------------------------------------s商品名称分词处理----------------------------------------------
import jieba

title=data['商品名']

title_s=[]
#商品名分词
for line in title:
    title_cut=jieba.lcut(line)
    for i in title_cut:
        title_s.append(i)
#print(title_s)


# 导入停用此表
stopwords = [line.strip() for line in open('../file/TXT/StopWords.txt', 'r', encoding='utf-8').readlines()]
#print(stopwords)

# 剔除停用词
title_clean = []
for line in title_s:
        if line not in stopwords:
            title_clean.append(line)
#print(title_clean)


# 把列表 allwords_clean_dist 转为数据框
df_allwords_clean_dist = pd.DataFrame({
    'allwords': title_clean
})

#print(df_allwords_clean_dist)
#
# # 对过滤_去重的词语 进行分类汇总
word_count = df_allwords_clean_dist.allwords.value_counts().reset_index()
word_count.columns = ['word', 'count']
#print(word_count)



#----------------------------------------------词云可视化----------------------------------------------

#------------------------------------------------------------------------------
# 第二步：绘制柱状图
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#获取数据

nume,sales=[],[]
for shopname,shopsales in word_count.head(30).values:
    nume.append(shopname)
    sales.append(shopsales)
# names = total_data.keys()
# # nums = total_data.values()
# # print(names)
# # print(nums)

# 绘图
plt.figure(figsize=[10,6])
#plt.bar(names, nums, width=0.3, color='green')
plt.bar(nume,sales, width=0.3, color='green')

# 设置标题
plt.xlabel("卖点", fontproperties='SimHei', size=12)
plt.ylabel("频率", fontproperties='SimHei', rotation=90, size=12)
plt.title("卖点频率关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(nume), fontproperties='SimHei', rotation=-40, size=10)
# 显示数字
for a, b in zip(list(nume), list(sales)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)

#保存并显示
plt.savefig('../file/PNG/02卖点频率关系图.png')
plt.show()

