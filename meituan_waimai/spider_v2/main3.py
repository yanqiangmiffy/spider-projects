#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main3.py
@time: 2019-05-20 13:32
@description:
"""
import requests
import json
import time

headers = {
    'Host': 'wx.waimai.meituan.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive',
    'wm-ctype': 'wxapp',
    'uuid': '1079582746768289800',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN',
    # 'Content-Length': '2980',
    'Referer': 'https://servicewechat.com/wx2c348cf579062e56/184/page-frame.html',
    'Accept-Language': 'zh-cn',
}

data = {
    'riskLevel': '1',
    'partner': '4',
    'platform': '13',
    'open_id': 'oOpUI0Zyw8BZvw-_voc5LS6wrhsc',
    'uuid': '1079582746768289800',
    'ref_list_id': '13415385ea4525dde2fd958274676828',
    'rank_list_id': '13415385ea4525dde2fd958274676828',
    '_token': 'eJxVksmOo2gQhN+FKx6ZfSmpD5h9M/7ZodUHNrODWQpsRvPu7VKXNDNSKiMj9MUt/4ZmNYc+kBO0LtAHSpIMjpMMgmEYfoKyfzOKRAiKfWPp7AvQx0+cJk8kSf76Cuy3/0mTyAlFUeTX6T8nRrzni1HfCPRIymI5Z1UyDEX315f7n4FO30Q95MXzz4be5d59l9/afmvyreu3LnU5QB9Qob1Yb10/B4ED59ifFLyZHmW8RJTtJPZtvTb3bqxjW26DVyPIS87I/TpKy0YTMso7K3q9U0/3NihaHZsosdM92PBIDpYh5T2dMKLU4sxXNqWA9hR/sh+OqCYzfQWt4IzXZOktcff0V9jFBfwKwSxpvvSYzil83Pb80qiMb54Nud+sdGaqsjhW9zkGTjD6qk+8Mo04poPRU1WFTUBo3i6XdNzPq9PLTiBPLrY+wrCZGTOq6rIvLRCpCydFTWOJROm6vO6IFRd5d2IlK1Hks88KyIOZPfi2Fl1XQ2mmPOYYllugDrIpRpXdl7GMbVhHieH6oB3UMHbUXx3eQsf9SRvD827Wy3UiilAFlmkRKyH5fTFP1me9mEpOGaiDwfjEbK/SlTsNGVhBIYii0ksYpwbbxXKfwGQMDXpcp9kNpbfkslF7Z33KGbnhcBbiY44rLq6xUpw6LNY977iFW9EdJSSvTedV6bO6u7nVOfBCqpil3N2Druj1BNh8X7QCc0FRfraYqyQNbu4Y+BGlkXXhLFeIr7ASh/qt9AVwRgTKr65nV2+pfbIB4ADgbfLAOv8IQESMVVkugrj2yNZofhLfJbsobaWR4dhbaU+PqUVGKSZtdwNnJWR7kUXSLJcWoYvU8BzlLAyWV8J2x/TMUGgk15iaT9CNwyUKfHhJgsxTfpxDs/JYEwsvlgVKhRdlJhnAHWZLIsWQdh4Sz9XVJZNC2eD2l7csUvlqxv4WcWPz/umgzryNMgGbgB8/oH9+A3v7MPc=',
    'page_index': '1',
    'page_size': '20',
    'load_type': '1',
    'slider_select_data': '""',
    'sort_type': '0',
    'category_type': '910',
    'navigate_type': '910',
    'lch': '1089',
    'wm_dplatform': 'ios',
    'wm_ctype': 'wxapp',
    'wm_dtype': 'iPhone 6<iPhone7,2>',
    'wm_dversion': '7.0.4',
    'wm_uuid': '1079582746768289800',
    'wm_longitude': '117661801',
    'wm_latitude': '24510897',
    'wm_visitid': 'a3182857-763f-4c41-85fc-7bd1e4f0027b',
    'wm_appversion': '3.9.4',
    'wm_logintoken': 'jGBkKf7_1_5U7_XBVwgfyQnHFgsAAAAAaQgAAFfYhEjQVcxEi5Ccc_bvkXEyvj3mmUI2f2hNFOKTjJ4lXN2is1E5FL-iCHVE2bJ7EA',
    'userToken': 'jGBkKf7_1_5U7_XBVwgfyQnHFgsAAAAAaQgAAFfYhEjQVcxEi5Ccc_bvkXEyvj3mmUI2f2hNFOKTjJ4lXN2is1E5FL-iCHVE2bJ7EA',
    # 'req_time': '1558335429641',
    'waimai_sign': '/',
    'wm_actual_longitude': '116286827',
    'wm_actual_latitude': '40050594',
    'userid':'149948296',
    'user_id':'149948296'
}

for i in range(60):
    print("正在爬取{}页".format(i))
    data['page_index'] = str(i+1)
    res = requests.post(
        url='https://wx.waimai.meituan.com/weapp/v2/poi/channelpage?ui=149948296&region_id=1000110100&region_version=1558324866349',
        headers=headers,
        data=data)

    with open('shops/data{}.json'.format(str(i)), 'w', encoding='utf-8') as fout:
        json.dump(res.json(), fout, indent=4, ensure_ascii=False)
    print(res.json())
    time.sleep(30)
