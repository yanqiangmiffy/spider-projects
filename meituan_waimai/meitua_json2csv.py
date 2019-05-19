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
import os

with open('food1.csv', 'a', encoding='utf-8', newline='') as fout:
    csv_writer = csv.DictWriter(fout,
                                fieldnames=['mtWmPoiId', 'shopName', 'categoryName', 'spuName', 'spuId', 'saleVolume',
                                            'originPrice', 'currentPrice', 'spuDesc', 'praiseNum', 'boxFee',
                                            'skuPromotionInfo'])
    csv_writer.writeheader()
    for js in os.listdir('foods1/'):
        if js.endswith('.json'):
            with open('foods1/' + js, 'r', encoding='utf-8') as fin:
                print(js)
                data = json.load(fin)
                tmp = dict()
                if data['code'] != 1:
                    # print(data['data'])
                    tmp['mtWmPoiId'] = data['data']['mtWmPoiId']
                    tmp['shopName'] = data['data']['shopInfo']['shopName']
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
                            csv_writer.writerow(tmp)
