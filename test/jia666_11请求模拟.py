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
    headerDict,f = {},open('../file/TXT/headers.txt', 'r')#初始化字典，只读打开文件
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

#------------------------------------------------------------------------------
# 第二步：拼接关键字搜索链接
#------------------------------------------------------------------------------
def get_search_URL(key):
    requests_page_url=[]
    for i in range(0,80):
        page_num=i*60
        url = 'https://list.tmall.com/search_product.htm?q='+str(key)+'&type=p&vmarket=&spm=a2156.1676643.a2227oh.d100' \
                                                                      '&from=mallfp..pc_1_searchbutton'+'&s='+str(page_num)
        requests_page_url.append(url)
    # print('三 搜素链接已生成')
    # with open('../file/CSV/手机_评价.csv', 'a+', encoding='utf-8') as f:
    #     productlist = '网络类型'+','+'机身颜色'+','+'套餐类型'+','+'存储容量'+','+'版本类型'+','+'评价内容'+','+'评价时间'+'\n'
    #     f.write(productlist)
    return requests_page_url

#------------------------------------------------------------------------------
# 第三步：获取返回的商品店铺的评价链接
#------------------------------------------------------------------------------
def get_productlist(url):
    url=url

    try:
        print("四 正在尝试获取商品网页")
        head['user-agent'] = UserAgent().chrome
        response=requests.get(url,headers=head)#请求网页
        if response.status_code==200:#获取网页的状态码
            doc=pq(response.text)#网页解析
            print(doc)
            items = doc('#J_ItemList .product').items()  # 信息提取
            # 保存数据
            n = '../file/CSV/天猫商品信息1'  + '.csv'
            fw = open(n, 'a+', encoding='utf-8')
            for item in items:
                sale = item('.productStatus span em').text().replace('笔', '')
                if '万' in sale:
                    sale = str(float(sale.replace('万', '')) * 10000)
                fw.write(item('.productShop-name').text() + ',' +
                         item('.productTitle a').attr('href') + ',' +
                         item('.productTitle a').text().replace(' ', '').replace(',', '').replace('，', '.') + ',' +
                         item('.productPrice em').attr('title') + ',' + sale +
                         '\n')
        else:
            print(response.status_code)
            print("请求" + url + "失败")
    except Exception as e:
        print(e)
        time.sleep(10)
        get_productlist(url)





if __name__ == '__main__':
    start_time=time.time()
    head = strheader()#调用类，获取https请求头

    key='智能手机'#天猫搜索关键字
    URL=get_search_URL(key)#拼接搜索链接
    for link in URL:
        shoplist=get_productlist(link)#
    #TODO 用时: 1197.9221110343933，大约20分钟
    print("用时:",time.time()-start_time)

