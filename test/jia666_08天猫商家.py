#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jia666666'
__time__ = '2020/3/24'
"""
import re,time

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




#TODO 1 界面可视
browser=webdriver.Chrome()

#TODO 2 界面不可视，后台运行
# browser=webdriver.PhantomJS()
# browser.set_window_size(1400,900)


wait=WebDriverWait(browser, 10)


def search(kyes):
    print('正在搜索')
    try:

        browser.get('https://login.tmall.com/')        #获取天猫登录界面

        #time.sleep(20)#睡眠20s，用于扫码登录天猫

        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mq")))        #找到搜素框

        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mallSearch > form > fieldset > div > button')))        #找到搜素按钮

        input.send_keys(keys)      #输入搜索内容

        submit.click()    #点击搜索按钮




        #写入csv列头
        #店铺名称,店铺链接,商品名,价格,销量
        n = '../file/CSV/' + keys + '.csv'
        with open(n, 'a+', encoding='utf-8') as f:
            productlist = '店铺名称' + ',' + '店铺链接' + ',' + '商品名' + ',' + '价格' + ',' + '销量' + '\n'
            f.write(productlist)


        get_profucts()  #TODO 获取产品信息，执行函数

    #判断超时
    except Exception as e:
        print(e)

        #return search()     #重新执行
def next_page(page_number):
    #提示信息
    print('正在翻页',page_number)
    try:
        #定位到页码输入框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div.ui-page > div > b.ui-page-skip > form > input.ui-page-skipTo")))
        #定位到确定按钮
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div.ui-page > div > b.ui-page-skip > form > button')))
        #页码框情况
        input.clear()
        #输入页码
        input.send_keys(page_number)
        #点击确定翻页
        submit.click()
        #判断高亮当前页码，确保是否成功加载
        # wait.until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > div > p.btmFeed > a")))
        # #TODO 执行函数，获取该页所有的产品信息

        get_profucts()
    #超时重新加载
    except TimeoutException:
        next_page(page_number)
def get_profucts():

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_ItemList')))    #等待，确保产品列表加载完成

    html=browser.page_source    #获取网页源码

    doc=pq(html)#PyQuery解析

    items = doc('#J_ItemList .product').items()    #信息提取

    #保存数据
    n='../file/CSV/0'+keys+'.csv'
    fw = open(n, 'a+', encoding='utf-8')
    for item in items:
        sale = item('.productStatus span em').text().replace('笔', '')
        if '万' in sale:
            sale = str(float(sale.replace('万', '')) * 10000)
        fw.write(item('.productShop-name').text() + ',' +
                 item('.productTitle a').attr('href') + ',' +
                 item('.productTitle a').text().replace(' ', '').replace(',','').replace('，','.') + ',' +
                 item('.productPrice em').attr('title') + ',' +sale +
                 '\n')
def main(keys):
    try:
        search(keys)    #开始搜索
        total = 80# 天猫搜索页面默认含有80页商品
        for i in range(2,total+1):
            time.sleep(3)
            next_page(i)

        print('信息写入完成，可以查看文件.')
        browser.close()        # 浏览器关闭
    except Exception as e:
        print(e)



if __name__ == '__main__':
    keys='智能手机'
    main(keys)