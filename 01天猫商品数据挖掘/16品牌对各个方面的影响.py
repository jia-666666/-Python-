#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/25'
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/25'
"""
import time
import pandas as pd


# 读取数据
n = '../file/CSV/智能手机'  + '-all.csv'
data = pd.read_csv(n)
data.fillna(value=0,inplace=True)
#数据定义
count_1000,count_2000,count_3000,count_4000,count_5000,count_6000,count_more =0,0,0,0,0,0,0
sale_1000,sale_2000,sale_3000,sale_4000,sale_5000,sale_6000,sale_more =0,0,0,0,0,0,0
money_1000,money_2000,money_3000,money_4000,money_5000,money_6000,money_more =0,0,0,0,0,0,0
#数据处理
for item,i,j in zip(data['商品名'],data['价格'],data['销量']):
    i=int(i)
    #print(i)
    if '华为' in item:
        count_1000+=1
        sale_1000+=j
        money_1000+=i*j
    elif '小米' in item:
        count_2000 += 1
        sale_2000 += j
        money_2000 += i * j
    elif '三星' in item:
        count_3000 += 1
        sale_3000 += j
        money_3000 += i * j
    elif '苹果' in item:
        count_4000 += 1
        sale_4000 += j
        money_4000 += i * j
    elif 'vivo' in item or 'VIVO' in item :
        count_5000 += 1
        sale_5000 += j
        money_5000 += i * j
    elif 'oppo' in item or 'OPPO' in item:
        count_6000 += 1
        sale_6000 += j
        money_6000 += i * j
    else:
        count_more += 1
        sale_more += j
        money_more += i * j
#print(count_2000)
#------------------------------------------------------------------------------
# 初始化
#------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=[20,18])
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#------------------------------------------------------------------------------
# 数据获取
#------------------------------------------------------------------------------
index=['华为','小米','三星','苹果','VIVO','OPPO','其他']
count=[count_1000,count_2000,count_3000,count_4000,count_5000,count_6000,count_more ]
sale=[sale_1000,sale_2000,sale_3000,sale_4000,sale_5000,sale_6000,sale_more]
money=[money_1000,money_2000,money_3000,money_4000,money_5000,money_6000,money_more]


#------------------------------------------------------------------------------
# p1价格商品关系条形图
#------------------------------------------------------------------------------
p1=plt.subplot(221)
plt.bar(index,count, width=0.3, color='green')
# 设置标题
plt.xlabel("品牌", fontproperties='SimHei', size=12)
plt.ylabel("商品数量", fontproperties='SimHei', rotation=90, size=12)
plt.title("品牌商品数量关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(index), fontproperties='SimHei', rotation=0, size=10)
# 显示数字
for a, b in zip(list(index), list(count)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)
plt.grid(linestyle='-.')
plt.sca(p1)
#------------------------------------------------------------------------------
# 品牌商品数量饼图
#------------------------------------------------------------------------------
p2=plt.subplot(222)

plt.pie(count,labels=index,autopct='%.2f%%')
plt.title("品牌商品总量占比", fontproperties='SimHei', size=16)
plt.axis('equal')
plt.legend()
plt.sca(p2)
#------------------------------------------------------------------------------
# 品牌销量关系
#------------------------------------------------------------------------------
p3=plt.subplot(223)
plt.bar(index,sale, width=0.3, color='black')

# 设置标题
plt.xlabel("品牌", fontproperties='SimHei', size=12)
plt.ylabel("销量", fontproperties='SimHei', rotation=90, size=12)
plt.title("品牌销量关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(index), fontproperties='SimHei', rotation=0, size=10)
# 显示数字
for a, b in zip(list(index), list(sale)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)
plt.grid(linestyle='-.')
plt.sca(p3)


#------------------------------------------------------------------------------
# 品牌销售额
#------------------------------------------------------------------------------
p4=plt.subplot(224)
plt.bar(index,money, width=0.3, color='red')

# 设置标题
plt.xlabel("品牌", fontproperties='SimHei', size=12)
plt.ylabel("销售额", fontproperties='SimHei', rotation=90, size=12)
plt.title("品牌销售额关系图", fontproperties='SimHei', size=16)
#倾斜度角
plt.xticks(list(index), fontproperties='SimHei', rotation=0, size=10)
# 显示数字
for a, b in zip(list(index), list(money)):
    #x轴，y轴，显示数值，水平居中，垂直底部，字体大小
    plt.text(a,b,b, ha='center', va='bottom', size=10)
plt.grid(linestyle='-.')
plt.sca(p4)

#------------------------------------------------------------------------------
# 数据显示
#------------------------------------------------------------------------------


plt.savefig('../file/PNG/12品牌影响关系图.png')
plt.show()

