#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-06-18 11:39
@description:
"""
import pandas as pd
from utils
from sklearn.linear_model import LogisticRegression # 逻辑回归
from sklearn.preprocessing import OneHotEncoder

train=pd.read_csv('sina/sinanews.train',sep='\t',header=None)
train.columns=['datetime','sentiment','news']
test=pd.read_csv('sina/sinanews.test',sep='\t',header=None)
test.columns=['datetime','sentiment','news']

print(train.shape,test.shape)
df=pd.concat([train,test],axis=0)
print(df.shape)