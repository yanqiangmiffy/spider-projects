#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: lenet3.py
@time: 2019-05-18 16:50
@description:
"""

import numpy as np
import tensorflow as tf
import scipy.io
from keras import backend as K

dataset = scipy.io.loadmat('dataset.mat')
# get training and testing sets
x_train = dataset['train_image']
x_test = dataset['test_image']
y_train = dataset['train_label'].reshape(-1, )
y_test = dataset['test_label'].reshape(-1, )
print(y_train.shape)
# batch size for gradient descent
batch_size = 16
# number of classes
num_classes = 2
# number of epochs (1 epoch = amount of iterations that covers the whole training set)
epochs = 200  # try a larger number of epochs here (for example 10 or larger)
# input image dimensions
nmb_samples, img_rows, img_cols = x_train.shape[0], x_train.shape[1], x_train.shape[2]
nmb_test_samples = x_test.shape[0]
lr = 0.05  # learning rate

# process mnist data
train_dataset = tf.data.Dataset.from_tensor_slices(
    (x_train, y_train)).shuffle(20000).repeat(100).batch(batch_size)
iterator = train_dataset.make_initializable_iterator()
next_batch = iterator.get_next()

tf_x = tf.placeholder(tf.float32, [None, 24, 24], name='x') / 255. * 2. - 1.  # normalize to (-1, 1)
image = tf.reshape(tf_x, [-1, 24, 24, 1], name='img_x')  # (batch, height, width, channel)
tf_y = tf.placeholder(tf.int32, [None, ], name='y')  # input y

# network structure
with tf.variable_scope('LeNet'):
    # conv1
    net = tf.layers.conv2d(  # [batch, 28, 28, 1]
        inputs=image,
        filters=6,
        kernel_size=5,
        strides=1,
        padding='same',
        name="conv1")  # -> [batch, 28, 28, 6]
    # max1
    net = tf.layers.max_pooling2d(
        inputs=net,
        pool_size=2,
        strides=2,
        name="maxpool1")  # -> [batch, 14, 14, 6]
    net = tf.layers.conv2d(net, 16, 5, 1, padding="same", name="conv2")  # -> [batch, 14, 14, 16]
    net = tf.layers.max_pooling2d(net, 2, 2, name="maxpool2")  # -> [batch, 7, 7, 16]
    net = tf.layers.flatten(net, name='flat')  # -> [batch, 7*7*16=784]
    logits = tf.layers.dense(net, 2, name='fc4')  # -> [batch, n_classes]

loss = tf.losses.sparse_softmax_cross_entropy(labels=tf_y, logits=logits)  # compute cost
train_op = tf.train.AdamOptimizer(lr).minimize(loss)

accuracy = tf.metrics.accuracy(  # return (acc, update_op), and create 2 local variables
    labels=tf_y, predictions=tf.argmax(logits, axis=1), )[1]

sess = tf.Session()
sess.run(tf.group(  # initialize var in graph
    tf.global_variables_initializer(),
    tf.local_variables_initializer(),
    iterator.initializer)
)  # the local var is for accuracy_op

writer = tf.summary.FileWriter('./log', sess.graph)  # write to file

# training
for step in range(200):
    b_x, b_y = sess.run(next_batch)
    _, loss_ = sess.run([train_op, loss], {tf_x: b_x, tf_y: b_y})
    if step % 10 == 0:
        accuracy_ = sess.run(accuracy, {tf_x: x_test, tf_y: y_test})
        print('Step:', step, '| train loss: %.4f' % loss_, '| test accuracy: %.2f' % accuracy_)
