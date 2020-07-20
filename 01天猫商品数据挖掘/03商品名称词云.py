#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pandas as pd


#----------------------------------------------读取数据----------------------------------------------
# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
#n = time.strftime("%Y-%m-%d") + "bak.CSV"
data = pd.read_csv(n)

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
#x[0]: x[1] for x in word_count.head(100).values




#----------------------------------------------词云可视化----------------------------------------------

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import imageio as im
#尺寸大小
plt.figure(figsize=(8, 8))

# 读取图片，用于限制大小
pic = im.imread("../file/PNG/猫.PNG")
#print(pic)
w_c = WordCloud(font_path="simhei.ttf", background_color="black",mask=pic,max_font_size=100, margin=1)
wc = w_c.fit_words({
    x[0]: x[1] for x in word_count.head(100).values
})

#显示词云
plt.imshow(wc, interpolation='bilinear')
#坐标刻度隐藏
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file('../file/PNG/01商品名称词云.PNG')

