#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-05-14 13:39
@description:
"""
import requests
import csv
import os
import json
import pickle
import pandas as pd
from utils import aes_decrypt
import time
import argparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def get_chapters():
    """
    获取章节目录
    :return:
    """
    params = {
        'appEName': 'ZY_LCZY_YTMJ',
        'clientver': 'wide.ksbao.com'

    }

    url = 'https://slb-exam.ksbao.com/api/chapterMenu/getChapterMenuX'
    res = requests.get(url=url, params=params, headers=headers)
    print(res.text)
    data = res.text
    print(res.encoding)
    # with open('data/chapter.json', 'w', encoding='utf-8') as fout:
    #     json.dump(data, fout, ensure_ascii=False, indent=4)

    with open('data/chapter.json', 'w', encoding='utf-8') as fout:
        fout.write(str(data))


def read_chapter():
    """
    读取章节数据
    :return:
    """
    with open('data/chapter.json', 'r', encoding='utf-8') as fout:
        data = json.loads(fout.read())
        # print(data)
        # print(data.keys())
        # print(data['data']['ChapterMenuJson'])
        child = json.loads(data['data']['ChapterMenuJson'])['Childs']
        with open('data/chapter.csv', 'w', encoding='utf-8') as fout:
            csv_writer = csv.DictWriter(fout, fieldnames=
            ['first_id', 'first_name', 'second_id', 'second_name', 'third_id', 'third_name'])
            csv_writer.writeheader()
            for ch in child:
                print(ch)
                print('--------' * 10)
                for c in ch['Childs']:
                    print(c, '\n', '****' * 100)
                    for thc in c['Childs']:
                        tmp_dict = dict()
                        tmp_dict['first_id'] = ch['ID']
                        tmp_dict['first_name'] = ch['Name']
                        tmp_dict['second_id'] = c['ID']
                        tmp_dict['second_name'] = c['Name']
                        tmp_dict['third_id'] = thc['ID']
                        tmp_dict['third_name'] = thc['Name']
                        csv_writer.writerow(tmp_dict)


def get_chapter_exam(id):
    data = {
        'appID': '1328',
        'cptID': str(id),
        'queryHistory': '1',
        'queryTestInfo': '1',
        'queryKnowledge': '0',
        'guid': '41NOZ5DGrvAfpy8GwrmAuDkW9QWwgI7u52978331',
        'agentCode': '889',
        'clientver': 'wide.ksbao.com',

    }

    url = 'https://slb-exam.ksbao.com/api/exam/getChapterTestEx'
    res = requests.post(url=url, data=data)
    # print(res.json())
    data = res.json()
    with open('data/exam/' + str(id) + '.json', 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)


def read_exam(filename):
    """
    读取试题
    :return:
    """

    with open(filename, 'r', encoding='utf-8') as fout:
        data = json.loads(fout.read())
        with open('data/question.csv', 'a', encoding='utf-8') as fout:
            csv_writer = csv.DictWriter(fout, fieldnames=
            ['Title', 'Explain', 'TestPoint', 'Answer',
             'OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE',
             'StyleType', 'AllTestID', 'ATestID', 'SrcID', 'SbjID', 'CptID'])
            # csv_writer.writeheader()
            for style in data['data']['test']['StyleItems']:
                if style['StyleID'] == 4:
                    # print(style)
                    for item in style['TestItems']:
                        FrontTitle = aes_decrypt(item['FrontTitle'])
                        # A3TestItems
                        for a3item in item['A3TestItems']:

                            title = FrontTitle + aes_decrypt(a3item['Title'])
                            title = title.strip()

                            question = dict()
                            question['Title'] = title
                            question['Explain'] = a3item['Explain']
                            question['TestPoint'] = a3item['TestPoint']
                            question['Answer'] = a3item['Answer']

                            question['OptionA'] = ''
                            question['OptionB'] = ''
                            question['OptionC'] = ''
                            question['OptionD'] = ''
                            question['OptionE'] = ''

                            question['OptionA'] = a3item['SelectedItems'][0]['Content']
                            question['OptionB'] = a3item['SelectedItems'][1]['Content']
                            question['OptionC'] = a3item['SelectedItems'][2]['Content']
                            question['OptionD'] = a3item['SelectedItems'][3]['Content']
                            if len(a3item['SelectedItems']) > 4:
                                question['OptionE'] = a3item['SelectedItems'][4]['Content']
                            question['StyleType'] = item['StyleType']
                            question['AllTestID'] = item['AllTestID']
                            # question['ATestID']=item['ATestID']
                            question['SrcID'] = item['SrcID']
                            question['SbjID'] = item['SbjID']
                            question['CptID'] = item['CptID']
                            csv_writer.writerow(question)
                            # print(a3item['SelectedItems'])
                if style['StyleID'] == 3:
                    # print(style)
                    for item in style['TestItems']:
                        # print(item)
                        for bitem in item['BTestItems']:
                            # print(bitem)
                            title = aes_decrypt(bitem['Title'])
                            # print(title)
                            # print(item['SelectedItems'])
                            title = title.strip()
                            question = dict()
                            question['Title'] = title
                            question['Explain'] = bitem['Explain']
                            question['TestPoint'] = bitem['TestPoint']
                            question['Answer'] = bitem['Answer']

                            question['OptionA'] = ''
                            question['OptionB'] = ''
                            question['OptionC'] = ''
                            question['OptionD'] = ''
                            question['OptionE'] = ''

                            question['OptionA'] = item['SelectedItems'][0]['Content']
                            question['OptionB'] = item['SelectedItems'][1]['Content']
                            question['OptionC'] = item['SelectedItems'][2]['Content']
                            question['OptionD'] = item['SelectedItems'][3]['Content']
                            if len(item['SelectedItems']) > 4:
                                question['OptionE'] = item['SelectedItems'][4]['Content']
                            question['StyleType'] = item['StyleType']
                            question['AllTestID'] = item['AllTestID']
                            # question['ATestID']=item['ATestID']
                            question['SrcID'] = item['SrcID']
                            question['SbjID'] = item['SbjID']
                            question['CptID'] = item['CptID']
                            csv_writer.writerow(question)
                # A1 A2
                if style['StyleID'] == 1 or style['StyleID'] == 2:
                    for item in style['TestItems']:
                        # print(item, len(item['SelectedItems']))
                        question = dict()
                        question['Title'] = aes_decrypt(item['Title'])
                        question['Explain'] = item['Explain']
                        question['TestPoint'] = item['TestPoint']
                        question['Answer'] = item['Answer']

                        question['OptionA'] = ''
                        question['OptionB'] = ''
                        question['OptionC'] = ''
                        question['OptionD'] = ''
                        question['OptionE'] = ''

                        question['OptionA'] = item['SelectedItems'][0]['Content']
                        question['OptionB'] = item['SelectedItems'][1]['Content']
                        question['OptionC'] = item['SelectedItems'][2]['Content']
                        question['OptionD'] = item['SelectedItems'][3]['Content']
                        if len(item['SelectedItems']) > 4:
                            question['OptionE'] = item['SelectedItems'][4]['Content']
                        question['StyleType'] = item['StyleType']
                        question['AllTestID'] = item['AllTestID']
                        # question['ATestID']=item['ATestID']
                        question['SrcID'] = item['SrcID']
                        question['SbjID'] = item['SbjID']
                        question['CptID'] = item['CptID']
                        csv_writer.writerow(question)


def process_question():
    df_question = pd.read_csv('data/question.csv')
    df_chapter = pd.read_csv('data/chapter.csv')
    # first_id, first_name, second_id, second_name, third_id, third_name

    first_dict = dict(zip(df_chapter['first_id'], df_chapter['first_name']))
    second_dict = dict(zip(df_chapter['second_id'], df_chapter['second_name']))
    third_dict = dict(zip(df_chapter['third_id'], df_chapter['third_name']))
    # print(first_dict)
    df_question['章节名称'] = df_question['SrcID'].apply(lambda x: first_dict[x])
    df_question['科目名称'] = df_question['SbjID'].apply(lambda x: second_dict[x])
    df_question['试题名称'] = df_question['CptID'].apply(lambda x: third_dict[x])
    print(len(df_question))
    df_question.to_csv('data/full.csv', index=None)
    df_question.dropna(subset=['Title'], inplace=True)
    print(len(df_question))

    # df_question.head(20).to_csv('data/sample.csv', index=None)
    df_question.to_csv('data/data.csv', index=None)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="程序运行参数")
    parser.add_argument('--get_chapter', '-c', action='store_true', help='爬取章节并存储到chapter.csv')
    parser.add_argument('--get_exam', '-e', action='store_true', help='爬取试题')
    parser.add_argument('--read_exam', '-r', action='store_true', help='提取json文件到question.cv')
    parser.add_argument('--process_question', '-p', action='store_true', help='整理最终结果到data.csv')

    args = parser.parse_args()
    if args.get_chapter:
        print("获取章节...")
        get_chapters()
        read_chapter()

    if args.get_exam:
        chapter = pd.read_csv('data/chapter.csv')
        for id in chapter.third_id:
            print("正在爬取试题：", id)
            get_chapter_exam(id)
            time.sleep(2)

    if args.read_exam:
        for filename in os.listdir('data/exam'):
            print(filename)
            read_exam('data/exam/' + filename)

    if args.process_question:
        print("整理最终结果到 data.csv")
        process_question()
