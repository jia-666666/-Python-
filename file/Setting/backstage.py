#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pandas as pd


def get_information():
    # 读取数据
    n = '../CSV/智能手机'  + '-all.csv'
    data = pd.read_csv(n)
    #缺省值处理
    data.fillna(value=0, inplace=True)
    return data

def get_assess():
    # 读取数据
    n = '../CSV/手机_评价'+'.csv'
    data = pd.read_csv(n)
    #缺省值处理
    data.fillna(value=0, inplace=True)
    return data

def get_header():
    headerDict,f = {},open('../TXT/headers.txt', 'r')#初始化字典，只读打开文件
    headersText = f.read().replace(' ', '') #读取文件并用替换句式去除文本空格
    headers = re.split('\n', headersText)   # 以换行键分割，返回列表形式数据
    for header in headers:#遍历列表
        j ,result =0, re.split(':', header, maxsplit=1)# maxsplit是执行拆分的最高次数
        for i in result:
            j = j + 1
            if j % 2 == 1:
                key = i
            if j % 2 == 0:
                headerDict[key] = i
    f.close()
    return headerDict

