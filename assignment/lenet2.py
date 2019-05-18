#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: lenet3.py
@time: 2019-05-18 16:50
@description:
"""

import tensorflow as tf
import scipy.io

dataset = scipy.io.loadmat('dataset.mat')
# get training and testing sets
x_train = dataset['train_image']
x_test = dataset['test_image']
y_train = dataset['train_label'].reshape(-1, )
y_test = dataset['test_label'].reshape(-1, )

# batch size for gradient descent
batch_size = 16
# number of classes
num_classes = 2
# number of epochs (1 epoch = amount of iterations that covers the whole training set)
epochs = 200  # try a larger number of epochs here (for example 10 or larger)
# input image dimensions
nmb_samples, img_rows, img_cols = x_train.shape[0], x_train.shape[1], x_train.shape[2]
nmb_test_samples = x_test.shape[0]
lr = 0.0001  # learning rate

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# 搭建CNN
x = tf.placeholder(tf.float32, [None, 24, 24, 1], name='x')
y_ = tf.placeholder(tf.int32, [None], name='y_')


def LeNet(input_tensor, regularizer, size):
    """

    :param input_tensor:X
    :param regularizer:
    :param x: the size of MLP hidden layers
    :return:
    """
    # conv1: Convolution layer, the size of the filter is 5×5, the depth is 6, and the full 0 is not used, and the step size is 1.
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable('weight', [5, 5, 1, 6], initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable('bias', [6], initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='VALID')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    # max pool1: Pooling layer, the size of the filter is 2×2, supplemented with all 0s, and the step size is 2.
    with tf.name_scope('layer2-pool1'):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # conv2 layer: Convolution layer, the size of the filter is 5×5, the depth is 16, and the full 0 is not used, and the step size is 1.
    with tf.variable_scope('layer3-conv2'):
        conv2_weights = tf.get_variable('weight', [5, 5, 6, 16],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2_biases = tf.get_variable('bias', [16], initializer=tf.constant_initializer(0.0))
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding='VALID')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))
    # max pool2: Pooling layer, the size of the filter is 2×2, supplemented with all 0s, and the step size is 2。
    with tf.variable_scope('layer4-pool2'):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    pool_shape = pool2.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    reshaped = tf.reshape(pool2, [-1, nodes])
    # fc1
    with tf.variable_scope('layer5-fc1'):
        fc1_weights = tf.get_variable('weight', [nodes, size], initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable('bias', [50], initializer=tf.constant_initializer(0.1))
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        fc1 = tf.nn.dropout(fc1, 0.5)
    # fc2
    with tf.variable_scope('layer6-fc2'):
        fc2_weights = tf.get_variable('weight', [50, size / 2], initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable('bias', [size / 2], initializer=tf.truncated_normal_initializer(stddev=0.1))
        fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)
        fc2 = tf.nn.dropout(fc2, 0.5)

    # activation：Activation layer，x->2
    with tf.variable_scope('layer7-fc3'):
        fc3_weights = tf.get_variable('weight', [size / 2, 2], initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc3_weights))
        fc3_biases = tf.get_variable('bias', [2], initializer=tf.truncated_normal_initializer(stddev=0.1))
        logit = tf.matmul(fc2, fc3_weights) + fc3_biases
    return logit

# 正则化，交叉熵，平均交叉熵，损失函数，最小化损失函数，预测和实际equal比较，tf.equal函数会得到True或False，
# accuracy首先将tf.equal比较得到的布尔值转为float型，即True转为1.，False转为0，最后求平均值，即一组样本的正确率。
# 比如：一组5个样本，tf.equal比较为[True False True False False],转化为float型为[1. 0 1. 0 0],准确率为2./5=40%。
regularizer = tf.contrib.layers.l2_regularizer(0.001)
y = LeNet(x, regularizer,50)
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=y_)
cross_entropy_mean = tf.reduce_mean(cross_entropy)
loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
train_op = tf.train.AdamOptimizer(learning_rate=lr).minimize(loss)
correct_prediction = tf.equal(tf.cast(tf.argmax(y, 1), tf.int32), y_)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# 每次获取batch_size个样本进行训练或测试
def get_batch(data, label, batch_size):
    for start_index in range(0, len(data) - batch_size + 1, batch_size):
        slice_index = slice(start_index, start_index + batch_size)
        yield data[slice_index], label[slice_index]


# 创建Session会话
with tf.Session() as sess:
    # 初始化所有变量(权值，偏置等)
    sess.run(tf.global_variables_initializer())

    # 将所有样本训练10次，每次训练中以64个为一组训练完所有样本。
    # train_num可以设置大一些。

    for step in range(epochs):

        train_loss, train_acc, batch_num = 0, 0, 0
        for train_data_batch, train_label_batch in get_batch(x_train, y_train, batch_size):
            _, train_loss_, train_accuracy_ = sess.run([train_op, loss, accuracy],
                                                       feed_dict={x: train_data_batch, y_: train_label_batch})
            train_loss += train_loss_
            train_acc += train_accuracy_
            batch_num += 1
        # print("train loss:", train_loss / batch_num)
        # print("train acc:", train_acc / batch_num)
        print('Step:', step, '| train loss: %.4f' % train_loss_,
              '| train accuracy: %.2f' % train_accuracy_)
        test_loss, test_acc, batch_num = 0, 0, 0
        for test_data_batch, test_label_batch in get_batch(x_test, y_test, batch_size):
            test_loss_, test_accuracy_ = sess.run([loss, accuracy],
                                                  feed_dict={x: test_data_batch, y_: test_label_batch})
            test_loss += test_loss_
            test_acc += test_accuracy_
            batch_num += 1
        # print("test loss:", test_loss / batch_num)
        # print("test acc:", test_acc / batch_num)
        print('Step:', step, '| test loss: %.4f' % test_loss_,
              '| test accuracy: %.2f' % test_accuracy_)
