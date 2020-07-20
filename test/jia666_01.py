#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/26'
"""
import requests
import re
from pyquery import PyQuery as pq
import time
from fake_useragent import UserAgent


#header请求头获取
def strheader():
    print("一 正在获取https请求头")
    headerDict,f = {},open('head.txt', 'r')#初始化字典，只读打开文件
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


#获取返回的商品店铺的评价链接
def get_productlist(url):
    try:
        print("四 正在尝试获取商品网页")
        head['user-agent'] = UserAgent().chrome
        response=requests.get(url,headers=head)#请求网页
        if response.status_code==200:#获取网页的状态码
            doc=pq(response.text)#网页解析
            #print(doc)
            k=doc('.product .productImg-wrap ').items()#从html文件中过滤符合条件的内容，返回的是列表形式
            print("五 正在分析商品ID与卖家ID")
            with open('手机.txt', 'a+', encoding='utf-8') as f:
                for i in k:
                    k=i('a').attr('href')#获取a标签中的链接，即店铺链接
                    nk = re.findall('id=(.*?)&.*?&user_id=(.*?)&',k)#获取商品ID与店铺卖家ID，用于后面拼接
                    URL='https://rate.tmall.com/list_detail_rate.htm?itemId='+nk[0][0]+'&sellerId='+nk[0][1]+'&currentPage=1'  #拼接店铺商品的评价链接
                    page=get_assesslink(URL)
                    print(page)
                    # for i in range(page+1):
                    #     URL=URL[:-1]+str(i)
                    #     f.write(URL+'\n')
        else:
            print(response.status_code)
            print("请求" + url + "失败")
    except Exception as e:
        print(e)

#获取商品店铺的评价链接的最大页数
def get_assesslink(url):
    try:
        print(url)
        response = requests.get(url, headers=head)
        if response.status_code==200:
            # 获取评价的最大页数
            page = (re.findall('lastPage":(.*?),', response.text))
            print(page)
            return page[0]
        else:
            print('请求最大页数失败')
    except Exception as e:
        print('获取最大页数失败，请处理错误')
        print(e)

#获取商品店铺的评价页数


#拼接关键字搜索链接
def get_search_URL(key):
    #
        #url='https://list.tmall.com/search_product.htm?q='+str(key)+'&type=p&vmarket=&spm=a2156.1676643.a2227oh.d100&from=mallfp..pc_1_searchbutton&s='+str(page)
        url = 'https://list.tmall.com/search_product.htm?q='+str(key)+\
              '&type=p&vmarket=&spm=a2156.1676643.a2227oh.d100&from=mallfp..pc_1_searchbutton'
        #print(url)
        get_productlist(url)



if __name__ == '__main__':
    head = strheader()#调用类，获取https请求头
    key='手机'#天猫搜索关键字
    URL=get_search_URL(key)#拼接搜索链接
    # shoplist=get_productlist(URL)#


