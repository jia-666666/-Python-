import time
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)

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
#获取数据

names = ['华为','小米','三星','苹果','VIVO','OPPO','其他']
nums = [huawei,xioami,sanxing,apple,vivo,oppo,other]
goods_sum=len(data['商品名'])

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号


plt.pie(nums,labels=names,autopct='%.2f%%')
plt.title("品牌市场比重", fontproperties='SimHei', size=16)
plt.axis('equal')
plt.legend()

plt.savefig('../file/PNG/09品牌市场比重.png')
plt.show()


