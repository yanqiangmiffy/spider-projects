#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-05-23 10:54
@description:
"""
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import researchGate_id
import time
from tqdm import tqdm


def login():
    # 加载驱动
    driver = webdriver.Chrome('./chromedriver')
    # 设置最大窗口
    driver.maximize_window()
    # 隐性等待5秒
    # driver.implicitly_wait(3)
    # WebDriverWait(driver, 3)
    print("正在加载网页元素...")
    # 打开登录网页
    driver.get(url='https://www.researchgate.net/login')
    time.sleep(3)
    # 输入用户名和密码
    username = researchGate_id.user
    password = researchGate_id.password
    driver.find_element_by_id('input-login').send_keys(username)
    driver.find_element_by_id('input-password').send_keys(password)
    print("输入name和pass 完毕")
    # 点击登录按钮
    driver.find_element_by_xpath('//button[@data-testid="loginCta"]').click()
    print("登录成功")
    # 等待5秒 加载元素
    # driver.implicitly_wait(3)
    # WebDriverWait(driver, 3)
    return driver


driver = login()
# driver.get(url='https://www.researchgate.net/browse.BrowseSuggestResearcher.html')
# # 模拟下滑到底部操作
# for i in range(1, 5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     WebDriverWait(driver,10)

driver.get(url='https://www.researchgate.net/profile/Mohsen_Adam_Omar')

# links_e1 = driver.find_elements_by_xpath('//ul[@class="list-directory"]/li/a')
#
# print("正在爬取一级标签")
# links_1 = []
# for link_e1 in links_e1:
#     # print(link_e1.get_attribute('href'))
#     link_1 = link_e1.get_attribute('href')
#     links_1.append(link_1)
#
# print("正在爬取二级标签")
# links_2 = []
# for link_1 in links_1:
#     driver.get(url=link_1)
#     time.sleep(1)
#     links_e2 = driver.find_elements_by_xpath('//ul[@class="list-directory"]/li/a')
#     for link_e2 in links_e2:
#         link_2 = link_e2.get_attribute('href')
#         links_2.append(link_2)
#
# print("正在爬取三级标签")
# with open('author.txt', 'a', encoding='utf-8') as f:
#     for link_2 in links_2:
#         driver.get(url=link_2)
#         time.sleep(2)
#         links_e3 = driver.find_elements_by_xpath('//ul[@class="list-directory"]/li/a')
#         for link_e3 in links_e3:
#             link_3 = link_e3.get_attribute('href')
#             f.write(link_3 + '\n')

driver.quit()
driver.close()
