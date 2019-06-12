#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main_rnn.py
@time: 2019-06-12 10:17
@description:
"""
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,RNN,SimpleRNN
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('data37.txt', sep='\t', header=None,
                 names=['x1', 'x2', 'x3', 'x4', 'x5',
                        'y1', 'y2', 'y3', 'y4', 'y5'])
X,y=df[['x1','x2','x3','x4','x5']].values,df['y1'].values.reshape(-1,1)
scalarX, scalarY = MinMaxScaler(), MinMaxScaler()
scalarX.fit(X)
scalarY.fit(y)
X = scalarX.transform(X).reshape(-1,1,5)
print(X)
y = scalarY.transform(y)

# 定义并拟合模型
model = Sequential()
model.add(SimpleRNN(10,input_shape=(None,5),return_sequences=False))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='adam')
model.summary()
model.fit(X, y, epochs=1000, verbose=1)

y_pred=model.predict(X)
y_pred=scalarY.inverse_transform(y_pred)
print(y_pred)
print(scalarY.inverse_transform(y_pred))