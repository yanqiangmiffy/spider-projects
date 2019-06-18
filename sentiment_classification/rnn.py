#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: rnn.py 
@time: 2019-06-18 22:30
@description:
"""
import pandas as pd
import numpy as np
from utils import set_label
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import f1_score, accuracy_score
from scipy.stats import pearsonr
from keras.layers import Conv1D, MaxPooling1D, Embedding, Dropout, LSTM, GRU, Bidirectional
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding, Dropout
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

plt.switch_backend('agg')

train = pd.read_csv('sina/sinanews.train', sep='\t', header=None)
train.columns = ['datetime', 'sentiment', 'news']
test = pd.read_csv('sina/sinanews.test', sep='\t', header=None)
test.columns = ['datetime', 'sentiment', 'news']

df = pd.concat([train, test], axis=0)
df['label'] = df['sentiment'].apply(lambda x: set_label(x))
tokenizer = Tokenizer()
texts = df['news']
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
print('Number of Unique Tokens', len(word_index))

data = pad_sequences(sequences, maxlen=500)

lb = LabelBinarizer()
labels = lb.fit_transform(df['label'].values)
print('Shape of Data Tensor:', data.shape)
print('Shape of Label Tensor:', labels.shape)

indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

train_size = len(train)

x_train = data[:train_size]
y_train = labels[:train_size]
x_test = data[train_size:]
y_test = labels[train_size:]

embedding_matrix = np.random.random((len(word_index) + 1, 100))
embedding_layer = Embedding(len(word_index) + 1,
                            100, weights=[embedding_matrix],
                            input_length=500, trainable=True)

sequence_input = Input(shape=(500,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)

l_lstm = Bidirectional(LSTM(100))(embedded_sequences)
preds = Dense(8, activation='softmax')(l_lstm)
model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])

print("Bidirectional LSTM")
model.summary()

cp = ModelCheckpoint('models/model_rnn.hdf5', monitor='val_acc', verbose=1, save_best_only=True)
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5, batch_size=32, callbacks=[cp])

fig1 = plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Training loss', 'Validation Loss'], fontsize=18)
plt.xlabel('Epochs ', fontsize=16)
plt.ylabel('Loss', fontsize=16)
plt.title('Loss Curves :RNN', fontsize=16)
fig1.savefig('pictures/loss_rnn.png')
plt.show()

fig2 = plt.figure()
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['Training Accuracy', 'Validation Accuracy'], fontsize=18)
plt.xlabel('Epochs ', fontsize=16)
plt.ylabel('Accuracy', fontsize=16)
plt.title('Accuracy Curves : RNN', fontsize=16)
fig2.savefig('pictures/accuracy_rnn.png')
plt.show()

from keras.utils.vis_utils import plot_model

plot_model(model, to_file='pictures/rnn_model.png', show_shapes=True, show_layer_names=True)
