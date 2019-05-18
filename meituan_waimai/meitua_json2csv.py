#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: meitua_json2csv.py 
@time: 2019-05-06 11:17
@description:
"""
import json
import pandas as pd
import csv

with open('foods/844460470917242.json', 'r', encoding='utf-8') as fin:
    data = json.load(fin)
    tmp = dict()
    tmp['mtWmPoiId'] = data['data']['mtWmPoiId']
    tmp['shopName'] = data['data']['shopInfo']['shopName']
    with open('food.csv','a',encoding='utf-8',newline='') as fout:
        for cate in data['data']['categoryList']:
            tmp['categoryName'] = cate['categoryName']
            for spu in cate['spuList']:
                tmp['spuName'] = spu['spuName']
                tmp['spuId'] = spu['spuId']
                tmp['saleVolume'] = spu['saleVolume']
                tmp['originPrice'] = spu['originPrice']
                tmp['currentPrice'] = spu['currentPrice']
                tmp['spuDesc'] = spu['spuDesc']
                tmp['praiseNum'] = spu['praiseNum']
                tmp['boxFee'] = spu['skuList'][0]['boxFee']
                tmp['skuPromotionInfo'] = spu['skuList'][0]['skuPromotionInfo']
                csv_writer = csv.DictWriter(fout,fieldnames=list(tmp.keys()))
                # csv_writer = csv_writer.writeheader()
                csv_writer.writerow(tmp)
                # print(tmp)
# print(data['data']['mtWmPoiId'])
