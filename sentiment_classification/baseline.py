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
import numpy as np
from utils import set_label
from sklearn.preprocessing import LabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier  # 1 vs all
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.metrics import f1_score, accuracy_score
from scipy.stats import pearsonr

train = pd.read_csv('sina/sinanews.train', sep='\t', header=None)
train.columns = ['datetime', 'sentiment', 'news']
test = pd.read_csv('sina/sinanews.test', sep='\t', header=None)
test.columns = ['datetime', 'sentiment', 'news']

df = pd.concat([train, test], axis=0)
df['label'] = df['sentiment'].apply(lambda x: set_label(x))

# print(train.shape, test.shape, df.shape)
# print(df['label'].value_counts())
# 1 构建训练集和测试集
# 提取tf-idf特征
tf_vec = TfidfVectorizer(ngram_range=(1, 1), max_df=0.95, min_df=2)
X = tf_vec.fit_transform(df['news'])
# 标签one hot
lb = LabelBinarizer()
y = lb.fit_transform(df['label'].values)
train_size = len(train)
x_train, x_test, y_train, y_test = X[:train_size], X[train_size:], \
                                   y[:train_size], y[train_size:]
clf = OneVsRestClassifier(LogisticRegression(penalty='l2', dual=False, random_state=2019))
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print(lb.inverse_transform(y))
print("accuracy score:", accuracy_score(y_test, y_pred))
print("micro f1-score:", f1_score(y_test, y_pred, average='micro'))
print(pearsonr(np.argmax(y_test,axis=1),np.argmax(y_pred,axis=1)))


y_test,y_pred=np.argmax(y_test,axis=1),np.argmax(y_pred,axis=1)
print(y_test)
print(y_pred)
print("accuracy score:", accuracy_score(y_test, y_pred))
print("macro f1-score:", f1_score(y_test, y_pred, average='macro'))
print(pearsonr(y_test,y_pred))