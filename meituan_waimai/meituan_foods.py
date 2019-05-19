#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: meituan_foods.py 
@time: 2019-05-06 00:13
@description:
"""
import requests
import json
import pandas as pd
import time
import os
df_shop=pd.read_csv('meituan2.csv')

for poid in df_shop['mtWmPoiId']:
    if str(poid)+'.json' in os.listdir('foods2'):
        print(poid,"已存在")
    else:
        url = ' http://i.waimai.meituan.com/openh5/poi/food?_=1557074935874&X-FOR-WITH=3xFYNRjatPfAeMJSAEVqBr145vtTTe%2BTmtCOQGkoWTXTMG7SjAR1qbqnCYD8vav%2B%2FGb2mS24TEdelMn7hr3pYqjygAsCqPnxYt49BO8l79AkJR%2BK1UOz%2Bld7JiOyczM0iU17mtHKx1V%2FJW02pgEQuA%3D%3D'
        # poid = '975890765127073'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://h5.waimai.meituan.com',
            'Referer': 'http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId={}&source=shoplist&initialLat=24.5146&initialLng=117.65592&actualLat=39.902443&actualLng=116.356058'.format(
                poid),
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36',
            'Cookie': '_lx_utm=utm_source%3D60066;'
                      '_lxsdk=84B13511022B53C8AE36AF69426F87EDBA6B5054B9F21C9B5B000A4E4A13215D;'
                      '_lxsdk_cuid=16a88c0ea22c8-0ddde71241798-73216132-3b790-16a88c0ea22c8;'
                      '_lxsdk_s=16a88c0e8a6-299-053-dcd%7C149948296%7C33;'
                      'au_trace_key_net=default;'
                      'iuuid=84B13511022B53C8AE36AF69426F87EDBA6B5054B9F21C9B5B000A4E4A13215D;'
                      'mt_c_token=vsjJkXkqLiWcpNGmYtUzLAYIzKUAAAAAVAgAAPNOUcmwBaKzdw1y64n2taLDgdNeWFiog_DQukLemAjfX_wJCfUOg-lThcWkpii6BA;'
                      'openh5_uuid=84B13511022B53C8AE36AF69426F87EDBA6B5054B9F21C9B5B000A4E4A13215D;'
                      'showTopHeader=show;'
                      'token=vsjJkXkqLiWcpNGmYtUzLAYIzKUAAAAAVAgAAPNOUcmwBaKzdw1y64n2taLDgdNeWFiog_DQukLemAjfX_wJCfUOg-lThcWkpii6BA;'
                      'userFace=https://img.meituan.net/avatar/1f6a1bb89ec8addd4d5e44e07f8393eb14967.jpg;'
                      'userId=149948296;'
                      'userId=149948296;'
                      'userName=%E8%87%B4Great;'
                      'uuid=84B13511022B53C8AE36AF69426F87EDBA6B5054B9F21C9B5B000A4E4A13215D;'
                      'wm_order_channel=default;',
        }

        data = {
            'geoType': '2',
            # 'mtWmPoiId': '975890765127073',
            'mtWmPoiId': poid,
            'dpShopId': '-1',
            'source': 'shoplist',
            # 'skuId':'',
            'uuid': '84B13511022B53C8AE36AF69426F87EDBA6B5054B9F21C9B5B000A4E4A13215D',
            'platform': '3',
            'partner': '4',
            'originUrl': 'http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId={}&source=shoplist&initialLat=24.510897&initialLng=117.661801&actualLat=39.902443&actualLng=116.356058'.format(poid),
            'riskLevel': '71',
            'optimusCode': '10',
            'wm_latitude': '24510897',
            'wm_longitude': '117661801',
            'wm_actual_latitude': '39902443',
            'wm_actual_longitude': '116356058',
            # '_token':''
        }

        response = requests.post(url=url, headers=headers, data=data)
        print("正在爬取：",poid)
        with open('foods2/'+str(poid)+'.json','w',encoding='utf-8') as fout:
            json.dump(response.json(),fout,indent=4,ensure_ascii=False)
        time.sleep(6)