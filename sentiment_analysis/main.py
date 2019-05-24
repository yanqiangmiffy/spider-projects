#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-05-15 22:37
@description:
"""
import jieba
import pandas as pd
import numpy as np

# ------ 负面词 ----------
def load_negative():
    """
    加载负面词
    :return:
    """
    negative_words = []
    nf1 = open('data/negative/负面情感词语（中文）.txt', 'r', encoding='gbk')
    negative_words += nf1.read().split('\n')[2:]
    nf1.close()

    nf2 = open('data/negative/负面评价词语（中文）.txt', 'r', encoding='gbk')
    negative_words += nf2.read().split('\n')[2:]
    nf2.close()

    nf3 = open('data/negative/NTUSD_negative_simplified.txt', 'r', encoding='utf-16le')
    negative_words += nf3.read().split('\n')
    nf3.close()

    nf4 = open('data/negative/negative.txt', 'r', encoding='utf-8')
    negative_words += nf4.read().split('\n')
    nf4.close()

    print("去重之前负面词语个数：", len(negative_words))
    negative_words = list(set(negative_words))
    print("去重之后负面词语个数：", len(negative_words))
    return negative_words


# -------- 正面词 ----------------
def load_positive():
    """
    加载正面词
    :return:
    """
    positive_words = []
    pf1 = open('data/positive/正面情感词语（中文）.txt', 'r', encoding='gbk')
    positive_words += pf1.read().split('\n')[2:]
    pf1.close()

    pf2 = open('data/positive/正面评价词语（中文）.txt', 'r', encoding='gbk')
    positive_words += pf2.read().split('\n')[2:]
    pf2.close()

    pf3 = open('data/positive/NTUSD_positive_simplified.txt', 'r', encoding='utf-16le')
    positive_words += pf3.read().split('\n')
    pf3.close()

    pf4 = open('data/positive/positive.txt', 'r', encoding='utf-8')
    positive_words += pf4.read().split('\n')
    pf4.close()

    print("去重之前正面词语个数：", len(positive_words))
    positive_words = list(set(positive_words))
    print("去重之后正面词语个数：", len(positive_words))
    return positive_words


neg_dict = load_negative()
pos_dict = load_positive()
deny_word = open('data/否定词.txt', 'r', encoding='utf-8').read().split('\n')
degree_word = open('data/程度级别词语.txt', 'r', encoding='utf-8').read().split('\n')


def judgeodd(num):
    if (num % 2) == 0:
        return 'even'
    else:
        return 'odd'


def sentiment_score_list(dataset):
    seg_sentence = dataset.replace('。','').split('。')

    count1 = []
    count2 = []
    for sen in seg_sentence:  # 循环遍历每一个评论
        segtmp = jieba.lcut(sen, cut_all=False)  # 把句子进行分词，以列表的形式返回
        i = 0  # 记录扫描到的词的位置
        a = 0  # 记录情感词的位置
        poscount = 0  # 积极词的第一次分值
        poscount2 = 0  # 积极词反转后的分值
        poscount3 = 0  # 积极词的最后分值（包括叹号的分值）
        negcount = 0
        negcount2 = 0
        negcount3 = 0
        for word in segtmp:
            if word in pos_dict:  # 判断词语是否是情感词
                poscount += 1
                c = 0
                for w in segtmp:  # 扫描情感词前的程度词
                    if w in deny_word:
                        c += 1
                if judgeodd(c) == 'odd':  # 扫描情感词前的否定词数
                    poscount *= -1.0
                    poscount2 += poscount
                    poscount = 0
                    poscount3 = poscount + poscount2 + poscount3
                    poscount2 = 0
                else:
                    poscount3 = poscount + poscount2 + poscount3
                    poscount = 0

            elif word in neg_dict:  # 消极情感的分析，与上面一致
                negcount += 1
                d = 0
                for w in segtmp:
                    if w in degree_word:
                        d += 1
                if judgeodd(d) == 'odd':
                    negcount *= -1.0
                    negcount2 += negcount
                    negcount = 0
                    negcount3 = negcount + negcount2 + negcount3
                    negcount2 = 0
                else:
                    negcount3 = negcount + negcount2 + negcount3
                    negcount = 0
            elif word == '！' or word == '!':  ##判断句子是否有感叹号
                for w2 in segtmp[::-1]:  # 扫描感叹号前的情感词，发现后权值+2，然后退出循环
                    if w2 in pos_dict or neg_dict:
                        poscount3 += 2
                        negcount3 += 2
                        break

            # 以下是防止出现负数的情况
            pos_count = 0
            neg_count = 0
            if poscount3 < 0 and negcount3 > 0:
                neg_count += negcount3 - poscount3
                pos_count = 0
            elif negcount3 < 0 and poscount3 > 0:
                pos_count = poscount3 - negcount3
                neg_count = 0
            elif poscount3 < 0 and negcount3 < 0:
                neg_count = -poscount3
                pos_count = -negcount3
            else:
                pos_count = poscount3
                neg_count = negcount3

            count1.append([pos_count, neg_count])
        count2.append(count1)
        count1 = []

    return count2


def sentiment_score(senti_score_list):
    score = []
    # print(len(senti_score_list),senti_score_list)
    for review in senti_score_list:
        score_array = np.array(review)
        Pos = np.sum(score_array[:, 0])
        Neg = np.sum(score_array[:, 1])
        AvgPos = np.mean(score_array[:, 0])
        AvgPos = float('%.1f' % AvgPos)
        AvgNeg = np.mean(score_array[:, 1])
        AvgNeg = float('%.1f' % AvgNeg)
        StdPos = np.std(score_array[:, 0])
        StdPos = float('%.1f' % StdPos)
        StdNeg = np.std(score_array[:, 1])
        StdNeg = float('%.1f' % StdNeg)
        score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score


if __name__ == '__main__':

    labels = []
    pos_scores = []
    neg_scores = []
    df = pd.read_excel('data/sample(1).xlsx', header=None)
    df.columns = ['text']
    for s in df.text.values:
        # print(s)

        score = sentiment_score(sentiment_score_list(s))
        if score[0][0] > score[0][1]:
            labels.append(1)
        elif score[0][0] < score[0][1]:
            labels.append(-1)
        else:
            labels.append(0)
        pos_scores.append(score[0][0])
        neg_scores.append(score[0][1])
    df['label'] = labels
    df['pos_score'] = pos_scores
    df['neg_score'] = neg_scores
    df['pos_neg_diff'] = df['pos_score'] - df['neg_score']
    # df['rank_label']=df['pos_neg_diff'].rank()
    print(df.head())
    r = pd.cut(df['pos_neg_diff'], 5, labels=[1, 2, 3, 4, 5])
    print(r)
    df['rank_label'] = r.values
    df.to_excel('result1.xlsx', index=None)

