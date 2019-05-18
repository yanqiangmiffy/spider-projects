#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: tf-lenet.py
@time: 2019-05-18 15:16
@description:
"""
import scipy.io
import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.contrib.layers import flatten
from sklearn.utils import shuffle

# load dataset
dataset = scipy.io.loadmat('dataset.mat')
# get training and testing sets
x_train = dataset['train_image']
x_test = dataset['test_image']
y_train = dataset['train_label']
y_test = dataset['test_label']

# Re-shape the data format into 28x28x1
image_size = 24
num_labels = 2
num_channels = 1  # grayscale


def reformat(dataset, labels):
    dataset = dataset.reshape((-1, image_size, image_size, num_channels)).astype(np.float32)
    return dataset, labels


x_train, y_train = reformat(x_train, y_train)
x_test, y_test = reformat(x_test, y_test)
print('Training set :', x_train.shape, y_train.shape)
print('Validation set :', x_test.shape, y_test.shape)


# LeNet-5 architecture implementation using TensorFlow
def LeNet_5(x):
    # Layer 1 : Convolutional Layer. Input = 32x32x1, Output = 28x28x1.
    conv1_w = tf.Variable(tf.truncated_normal(shape=[5, 5, 1, 6], mean=0, stddev=0.1))
    conv1_b = tf.Variable(tf.zeros(6))
    conv1 = tf.nn.conv2d(x, conv1_w, strides=[1, 1, 1, 1], padding='VALID') + conv1_b
    # TODO: Activation.
    conv1 = tf.nn.relu(conv1)

    # Pooling Layer. Input = 28x28x1. Output = 14x14x6.
    pool_1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # TODO: Layer 2: Convolutional. Output = 10x10x16.
    conv2_w = tf.Variable(tf.truncated_normal(shape=[5, 5, 6, 16], mean=0, stddev=0.1))
    conv2_b = tf.Variable(tf.zeros(16))
    conv2 = tf.nn.conv2d(pool_1, conv2_w, strides=[1, 1, 1, 1], padding='VALID') + conv2_b
    # TODO: Activation.
    conv2 = tf.nn.relu(conv2)
    # TODO: Pooling. Input = 10x10x16. Output = 5x5x16.
    pool_2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # TODO: Flatten. Input = 5x5x16. Output = 400.
    fc1 = flatten(pool_2)

    # TODO: Layer 3: Fully Connected. Input = 400. Output = 120.
    fc1_w = tf.Variable(tf.truncated_normal(shape=(144, 120), mean=0, stddev=0.1))
    fc1_b = tf.Variable(tf.zeros(120))
    fc1 = tf.matmul(fc1, fc1_w) + fc1_b

    # TODO: Activation.
    fc1 = tf.nn.relu(fc1)

    # TODO: Layer 4: Fully Connected. Input = 120. Output = 84.
    fc2_w = tf.Variable(tf.truncated_normal(shape=(120, 84), mean=0, stddev=0.1))
    fc2_b = tf.Variable(tf.zeros(84))
    fc2 = tf.matmul(fc1, fc2_w) + fc2_b
    # TODO: Activation.
    fc2 = tf.nn.relu(fc2)

    # TODO: Layer 5: Fully Connected. Input = 84. Output = 2.
    fc3_w = tf.Variable(tf.truncated_normal(shape=(84, 2), mean=0, stddev=0.1))
    fc3_b = tf.Variable(tf.zeros(2))
    logits = tf.matmul(fc2, fc3_w) + fc3_b
    return logits


x = tf.placeholder(tf.float32, shape=[None, 24, 24, 1])
y_ = tf.placeholder(tf.int32, (None))

# Invoke LeNet function by passing features
logits = LeNet_5(x)
# Softmax with cost function implementation
cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_, logits=logits)
loss_operation = tf.reduce_mean(cross_entropy)
optimizer = tf.train.AdamOptimizer(learning_rate=0.1)
training_operation = optimizer.minimize(loss_operation)

correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y_, 1))
accuracy_operation = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# Evaluate function
def evaluate(X_data, y_data):
    num_examples = len(X_data)
    total_accuracy = 0
    sess = tf.get_default_session()
    for offset in range(0, num_examples, BATCH_SIZE):
        batch_x, batch_y = X_data[offset:offset + BATCH_SIZE], y_data[offset:offset + BATCH_SIZE]
    accuracy = sess.run(accuracy_operation, feed_dict={x: batch_x, y_: batch_y})
    total_accuracy += (accuracy * len(batch_x))
    return total_accuracy / num_examples


# To initialise session and run
EPOCHS = 200
BATCH_SIZE = 16
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    num_examples = len(x_train)

    print("Training... with dataset - ", num_examples)
    print()
    for i in range(EPOCHS):
        x_train, y_train = shuffle(x_train, y_train)
        for offset in range(0, num_examples, BATCH_SIZE):
            end = offset + BATCH_SIZE
            batch_x, batch_y = x_train[offset:end], y_train[offset:end]
            sess.run(training_operation, feed_dict={x: batch_x, y_: batch_y})

        validation_accuracy = evaluate(x_train, y_train)
        print("EPOCH {} ...".format(i + 1))
        print("Validation Accuracy = {:.3f}".format(validation_accuracy))
        print()

    saver = tf.train.Saver()
    save_path = saver.save(sess, '/tmp/lenet.ckpt')
    print("Model saved %s " % save_path)

    test_accuracy = evaluate(x_test, y_test)
    print("Test Accuracy = {:.3f}".format(test_accuracy))
