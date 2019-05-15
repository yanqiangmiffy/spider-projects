#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: extract.py
@time: 2019-05-15 13:35
@description:
"""

import pandas as pd

df=pd.read_csv('data/full.csv')
df[df['试题名称']=='2017年真题第二单元'].to_csv('2017年真题第二单元.csv',index=None)