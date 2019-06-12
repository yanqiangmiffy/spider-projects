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
import matplotlib.pyplot as plt


df = pd.read_csv('data37.txt', sep='\t', header=None,
                 names=['x1', 'x2', 'x3', 'x4', 'x5',
                        'y1', 'y2', 'y3', 'y4', 'y5'])
for i in range(1,6):
    X,y=df[['x1','x2','x3','x4','x5']].values,df['y'+str(i)].values.reshape(-1,1)
    scalarX, scalarY = MinMaxScaler(), MinMaxScaler()
    scalarX.fit(X)
    scalarY.fit(y)
    X = scalarX.transform(X).reshape(-1,1,5)
    y = scalarY.transform(y)


    # 定义并拟合模型
    model = Sequential()
    model.add(SimpleRNN(10,input_shape=(None,5),return_sequences=False))
    model.add(Dense(4, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='adam')
    model.summary()
    model.fit(X, y, epochs=500, verbose=1)

    y_pred=model.predict(X)
    y_pred=scalarY.inverse_transform(y_pred)
    df['y_pred'+str(i)]=y_pred
    # print(y_pred)
    y=scalarY.inverse_transform(y)
    # print(y)
    fig=plt.figure()

    index=[i for i in range(1,36)]
    plt.plot(index,y,label='y')
    plt.plot(index,y_pred,label='y_pred')
    plt.title('Product '+str(i))
    plt.legend()
    plt.show()

df.to_csv('result.csv',index=None)