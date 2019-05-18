#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-05-18 09:53
@description:
"""

# load python packages
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib
import IPython
import sklearn
import keras
import scipy.io


def acc_score(y_test, y_pred):
    """
    Calculation accuracy
    :param y_test:
    :param y_pred:
    :return:
    """
    y_test = y_test.reshape(-1, 1)
    y_pred = y_pred.reshape(-1, 1)
    check = np.array(y_test == y_pred)
    total_num = y_test.size
    acc = np.sum(check) / total_num
    return acc


class KNearestNeighbor(object):
    """
    a kNN classifier with euclidean distance
    """

    def __init__(self):
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        For the knn algorithm, the training process simply stores all the training data.
        Input:
        - X: shape is a numpy array of (num_train, D) containing training data consisting of
        num_train samples and each sample dimension D.
        - y: y: shape is a (N,) numpy array containing the labels of the training data, where y[i] is the label of X[i].
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X, k=1):
        """
        Use a classifier to predict the type of test data.
        Input:
        - X: shape is a numpy array of (num_train, D) containing test data consisting of
         num_train samples and each sample dimension D.
        - k: The number of neighbors used in the forecast category.
        Return:
        - y: shape is a (num_test,) numpy array containing the

         label of the training data, where y[i] is the label of X[i].
        """
        dists = self.compute_distances(X)
        return self.predict_labels(dists, k=k)

    def compute_distances(self, X):
        """
        Calculate the euclidean distance between each test data and each of the other training data.
        Input:
        - X: shape is a numpy array of (num_train, D) containing test data consisting of
         num_train samples and each sample dimension D.
         return:
        - dists: shape is a numpy array of (num_test, num_train), the [i, j] elements are the Euclidean
         distance of the i-th test data and the j-th training data.
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        x2 = np.sum(X ** 2, axis=1).reshape((num_test, 1))
        y2 = np.sum(self.X_train ** 2, axis=1).reshape((1, num_train))
        xy = -2 * np.matmul(X, self.X_train.T)
        dists = np.sqrt(x2 + xy + y2)
        # print(dists)
        return dists

    def predict_labels(self, dists, k=1):
        """
         Enter the distance matrix of the test data and the training data to predict the category of each test data.
         Input:
         - dists: shape is a numpy array of (num_test, num_train), the [i, j] elements are the
            Euclidean distance of the i-th test data and the j-th training data.
         Return:
         - y: shape is a (num_test,) numpy array containing the prediction labels for
            the training data, where y[i] is the label of X[i].
         """
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test, dtype=int)
        for i in range(num_test):
            # Array of length k, containing the category of k training data closest to the test data
            closest_x = np.argsort(dists[i])[:k]
            closest_y = [self.y_train[val] for val in closest_x]
            labels, counts = np.unique(closest_y, return_counts=True)
            y_pred[i] = labels[np.argmax(counts)]
        return y_pred


# load dataset
dataset = scipy.io.loadmat('dataset.mat')
# get training and testing sets
x_train = dataset['train_image']
x_test = dataset['test_image']
y_train = dataset['train_label']
y_test = dataset['test_label']
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
x_train = x_train.reshape(x_train.shape[0], 24 * 24 * 1)
x_test = x_test.reshape(x_test.shape[0], 24 * 24 * 1)

k_range = [i for i in range(1, 11)]
k_scores = []
for i in k_range:
    knn = KNearestNeighbor()
    # training model...
    knn.fit(x_train, y_train)
    # test
    y_pred = knn.predict(x_test, k=i)
    from sklearn import metrics

    # metric of model
    print("Accuracy:{} of k={}:".format(acc_score(y_test, y_pred), i))
    k_scores.append(acc_score(y_test, y_pred))
print(k_scores)
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Accuracy')
plt.show()
