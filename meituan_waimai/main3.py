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
    '_token': 'eJxVjMeuo2gQhd+FLR4Rf8KVemETTDAZg6HVC5IBg8kmjebdh9bcRY9UqlPn6Dv1NzTIKfSFnqBphL4wABiCAARB0Qx5gpI/MpJAKYCdoHjweOjrJ0GDEwDg1+/APvxPGqAnDMPQX6c/Tpw85jcjHwjURXk2IkkRNU1W//Xb/c9Ap2+ibNJs/W9DR/ntHuVDq2+NvnX61rHMG+gLypSNvdfYjG/nO+JMrtQUkTHyAa6rQS3GCtx7OJb2fb+1RT6IfNDqzagTI7YwNDUmb/rhMwtPNMuNIB7XkMsmbJjhTByGtf/EDkjyVSY9r8N3goDRaOUF0dosjNc07BzePTi/CEs7pXV1o5VYPdL9vWMMkV4fe8LDzRrsiJb5bP00K/aa9npFne0uu0XAaMF8PHNn1jmeWZNOtXUhWZ4mP6YeDcvqPOwyeOBzs4a2ZYtC2vG9gb0UufQwUVC5u+J6anKAwuAMsDimanV5SVkElspP17JGUOu5uRmGS+FHJl+RGpDcUnA3N6Id4A1UZ7XqhErduvb1zWGwlVxC8HZ3M4+N0XzdzdzfrjxHKVXXjz3KNx4x9an23mn2URB3jzMyaZXgxFwR7+zD67R/yiEN6r3s6mX0Rt/cHwqdbPCz3lu4CtUZZgk+mdi5pXvYYDSRqLdpKNnPBGdVNrw4vBfr+dYnFDBdePOyhjXroGpJ9v7ZXqpTFEsDBOSMpXQ4dL6aU2igonPqX4wxv8rOp7Dol3om6IscRQWC2GXQS4H/eoKgtbmrFjTSYPqeljmy5TRc0C22Ges3rG/i6Grfn6FgV+vHlq4X0WgY3E2Zy4oGoJTKPmbTJx998neQmkO8FgMmP2vG0DkT1iZh7p3cRjiLHDzHNW7rzMrKpN5xpGGMUBgokE+60NmcrqlYJRovBIDL/pin6cyga5n3WjHoY3RTmgsX7VOyyU+tqj4C5zlKTLL1rIsLM59//ID++RdXIzWL',
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
