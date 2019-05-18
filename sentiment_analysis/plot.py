#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: plot.py
@time: 2019-05-18 19:29
@description:
"""
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']

import matplotlib

a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)

df1 = pd.read_excel('plotdata.xlsx', sheet_name=0)
df2 = pd.read_excel('plotdata.xlsx', sheet_name=1)
df3 = pd.read_excel('plotdata.xlsx', sheet_name=2)

# print(df1)
# print(df2)
# print(df3)

for df in [df1, df2, df3]:
    k_range = [i for i in range(1, 1 + len(df))]
    train_scores = df['频数'].values
    plt.plot(k_range, train_scores, label=df.columns[0])
plt.xlabel('数据')
plt.ylabel('频数')
plt.legend()  # show legned
plt.show()
