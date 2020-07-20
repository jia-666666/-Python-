#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/25'
"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/24'
"""
import time
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)
data.fillna(value=0,inplace=True)
huawei,xioami,sanxing,apple,vivo,oppo,other=0,0,0,0,0,0,0
for item in data['商品名']:
    #print(item)
    if '华为' in item:
        huawei+=1
    elif '小米' in item:
        xioami+=1
    elif '三星' in item:
        sanxing+=1
    elif '苹果' in item:
        apple+=1
    elif 'vivo' in item:
        vivo+=1
    elif 'oppo' in item:
        oppo+=1
    else:
        other+=1

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#获取数据

names = ['华为','小米','三星','苹果','VIVO','OPPO','其他']
nums = [huawei,xioami,sanxing,apple,vivo,oppo,other]


# 绘图
plt.figure(figsize=(15,4))
plt.plot(names,nums)
plt.xticks(rotation=-90) # X轴标签旋转，避免重叠
plt.grid(linestyle='-.')
plt.ylabel('评价数')
plt.title('每日评价数量趋势图')
plt.show()

# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [1, 4, 9, 16]
# y3 = [1, 8, 27, 64]
# y4 = [1, 16, 81, 124]
# # 创建一个画布
# plt.figure()
# # 在figure下线
# plt.plot(x, y1, "-o") #实线
# plt.plot(x, y2, "--o") #虚线
# plt.plot(x, y3, "-.o") #虚点线
# plt.plot(x, y4, ":o") # 点线
# # 展现画布
# plt.show()