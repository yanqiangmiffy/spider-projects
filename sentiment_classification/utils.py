#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: utils.py
@time: 2019-06-18 12:04
@description:
"""


def set_label(sentiment):
    """
    根据每个类别的情感值设置label
    :param sentiment:
    :return:
    """
    max = 0
    label = ''
    for sent in sentiment.split()[1:]:
        data = sent.split(':')
        # print(data)
        if int(data[1]) >= max:
            label = data[0]
            max = int(data[1])
    return label
    # print(eval(str(sentiment.split()).replace('[','').replace(']','')))


if __name__ == '__main__':
    sentiment = 'Total:735 感动:27 同情:45 无聊:105 愤怒:44 搞笑:392 难过:56 新奇:60 温馨:6'
    set_label(sentiment)
