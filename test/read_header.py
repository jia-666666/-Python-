#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'https请求头获取'
__author__ = 'jia666666'
__mtime__ = '2020/2/29'
"""
import re


def read_header():
    print("一 正在获取https请求头")
    headerDict, f = {}, open('headers.txt', 'r')  # 初始化字典，只读打开文件
    headersText = f.read().replace(' ', '')  # 读取文件并用替换句式去除文本空格
    headers = re.split('\n', headersText)  # 以换行键分割，返回列表形式数据
    for header in headers:  # 遍历列表
        j, result = 0, re.split(':', header, maxsplit=1)  # maxsplit是执行拆分的最高次数
        for i in result:
            j = j + 1
            if j % 2 == 1:
                key = i
            if j % 2 == 0:
                headerDict[key] = i
    print("二 请求头获取完成")
    f.close()
    return headerDict
