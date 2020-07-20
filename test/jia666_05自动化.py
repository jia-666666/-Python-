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
        #获取天猫主页
        browser.get('https://jx.tmall.com/')
        #找到搜素框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mq")))
        #找到搜素按钮
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mallSearch > form > fieldset > div > button')))
        #输入搜索内容
        input.send_keys(keys)
        #点击搜索按钮
        submit.click()


        #天猫搜索页面默认含有80页商品
        total=80

        #TODO 获取产品信息，执行函数
        #get_profucts()

        #返回页数信息
        return total
    #判断超时
    except Exception as e:
        print(e)
        #重新执行
        #return search()
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
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page_number)))
        #TODO 执行函数，获取该页所有的产品信息

        # n = time.strftime("%Y-%m-%d") + ".CSV"
        # fw = open(n, 'a+', encoding='utf-8')
        # fw.write('店铺名称,店铺链接,商品名,价格,销量,省份\n')
        #
        # get_profucts()
    #超时重新加载
    except TimeoutException:
        next_page(page_number)
def get_profucts():
    #等待，确保产品列表加载完成
    #print('deafda')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_ItemList')))
    #print('112')
    #获取网页源码
    html=browser.page_source
    #PyQuery解析
    doc=pq(html)
    #信息提取
    print(doc)
    time.sleep(100)
    items=doc('#mainsrp-itemlist .items .item').items()
    #print(list(items[0]))
    #保存数据
    n = time.strftime("%Y-%m-%d") +"bak.CSV"
    fw = open(n, 'a+', encoding='utf-8')
    for item in items:
        fw.write(item.find('.shop').text() + ',' +
                 item.find('.pic a').attr('href') + ',' +
                 item.find('.title').text().replace(' ', '').replace(',','') + ',' +
                 item.find('.price').text().strip().replace('¥', '').replace('.00', '') + ',' +
                 item.find('.deal-cnt').text()[:-3].replace('.', '').replace('万', '000').replace('+', '') + ',' +
                 item.find('.location').text().split(' ')[0] +
                 '\n')

    # with open('天猫商品数据抓取.txt', 'a+', encoding='utf-8') as f:
    #     print('正在写入信息........')
    #     for item in items:
    #         #格式整理与写入
    #         product='title'+":"+item.find('.title').text()+'\n'+\
    #                 'link'+":"+item.find('.pic a').attr('href')+'\n'+\
    #                 'price'+":"+item.find('.price').text().strip()+'\n'+\
    #                 'deal'+":"+item.find('.deal-cnt').text()[:-3]+'\n'+\
    #                 'shop'+":"+item.find('.shop').text()+'\n'+\
    #                 'location'+":"+item.find('.location').text()+'\n'
    #
    #         f.write(str(product)+'\n\n')
    #     f.close()




def main(keys):
    try:
        #开始搜索
        total=search(keys)
        # print(total)
        # #总页数提取
        # total= int(re.compile('(\d+)').search(total).group(1))
        #循环遍历所有页数
        for i in range(2,81):
            print(i)
            next_page(i)
        print('信息写入完成，可以查看文件.')
        # 浏览器关闭
        browser.close()
    except Exception:
        print('错误了，请检查')
    finally:
        pass


if __name__ == '__main__':
    keys='智能手机'
    main(keys)