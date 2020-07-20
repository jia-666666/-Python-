#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/25'
"""
# -*- coding: utf-8 -*-
import time, json, requests
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
# n = time.strftime("%Y-%m-%d") + "bak.CSV"
# data = pd.read_csv(n)
# list_data = zip(list(data['province']), list(data['confirm']))
#print(type(list_data))
# [('湖北', 48206), ('广东', 1241), ('河南', 1169), ('浙江', 1145), ..., ('澳门', 10), ('西藏', 1)]

import time
import pandas as pd


# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
#n = time.strftime("%Y-%m-%d") + "bak.CSV"
data = pd.read_csv(n)

total_data = {}
for item in data['省份']:
    #print(item)
    if item not in total_data:
        #向字典中更新每个省份默认0病例
        total_data.update({item:1})
    else:
        total_data[item]+=1

province=total_data.keys()
num=total_data.values()

list_data=zip(province,num)


#-------------------------------------------------------------------------------------
# 第二步：绘制全国商家地图
#-------------------------------------------------------------------------------------
def map_cn_disease_dis() -> Map:
    c = (
        Map()
        .add('中国', list_data, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全国商家店铺省份分布图'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=6,
                                              is_piecewise=True,  # 是否为分段型
                                              pos_top='center',
                                              pieces=[
                                                   {'min': 1000, 'color': '#7f1818'},  #不指定 max
                                                   {'min': 400, 'max': 999},
                                                   {'min': 200, 'max': 399},
                                                   {'min': 100, 'max': 199},
                                                   {'min': 10, 'max': 99},
                                                   {'min': 0, 'max': 5} ],
                                              ),
        )
    )
    return c
#保存html文件
map_cn_disease_dis().render('../file/HTML/全国商家省份分布图.html')
print('文件保存完成')
