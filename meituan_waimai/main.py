#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-05-19 16:14
@description:
"""

from selenium import webdriver
import time


# 登录天眼查
def login():
    driver = webdriver.Chrome('./chromedriver')
    time_start = time.time()

    # 操作行为提示
    print('在自动输入完用户名和密码前，请勿操作鼠标键盘！请保持优雅勿频繁（间隔小于1分钟）登录以减轻服务器负载。')

    # 强制声明浏览器长宽为1024*768以适配所有屏幕
    driver.set_window_position(0, 0)
    driver.set_window_size(400, 800)
    driver.get("http://h5.waimai.meituan.com/login")

    # 模拟登陆：Selenium Locating Elements by Xpath
    time.sleep(1)

    driver.find_element_by_id("phoneNumInput").send_keys("15858186425")

    # 手工登录，完成滑块验证码
    print('请现在开始操作键盘鼠标，在15s内点击登录并手工完成滑块验证码。批量爬取只需一次登录。')
    time.sleep(30)
    print('还剩5秒。')
    time.sleep(5)

    time_end = time.time()
    print('您的本次登录共用时{}秒。'.format(time_end - time_start))
    return driver

driver=login()

print(driver.get_cookies())

