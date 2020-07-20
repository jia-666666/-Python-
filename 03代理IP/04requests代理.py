#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from pyquery import PyQuery as pq
import time
from fake_useragent import UserAgent

#------------------------------------------------------------------------------
# 第一步：获取请求头
#------------------------------------------------------------------------------
#header请求头获取
def strheader():
    print("一 正在获取https请求头")
    headerDict,f = {},open('headers.txt', 'r')#初始化字典，只读打开文件
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
    print("二 请求头获取完成")
    f.close()
    return headerDict
from urllib3 import disable_warnings
disable_warnings()
#------------------------------------------------------------------------------
def get_productlist(url):
    #head['user-agent'] = UserAgent().chrome
    response=requests.get(url,headers=head,verify=False)#请求网页
    if response.status_code==200:#获取网页的状态码
        doc=pq(response.text)#网页解析
        print(doc)



#------------------------------------------------------------------------------
# 第四步：获取商品店铺的评价链接的最大页数



if __name__ == '__main__':
    head = strheader()#调用类，获取https请求头
    URL='https://2020.ip138.com/'
    shoplist=get_productlist(URL)#

