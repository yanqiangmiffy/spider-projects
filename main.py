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
import json
import pickle
import pandas as pd
from utils import aes_decrypt
import time
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


def read_exam():
    """
    读取试题
    :return:
    """

    with open('data/exam35.json', 'r', encoding='utf-8') as fout:
        data = json.loads(fout.read())
        with open('data/question.csv', 'w', encoding='utf-8') as fout:
            csv_writer = csv.DictWriter(fout, fieldnames=
            ['Title', 'Explain', 'TestPoint', 'Answer',
             'OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE',
             'StyleType', 'AllTestID', 'ATestID', 'SrcID', 'SbjID', 'CptID'])
            csv_writer.writeheader()
            for style in data['data']['test']['StyleItems']:
                for item in style['TestItems']:
                    print(item, len(item['SelectedItems']))
                    question = dict()
                    question['Title'] = aes_decrypt(item['Title'])
                    question['Explain'] = item['Explain']
                    question['TestPoint'] = item['TestPoint']
                    question['Answer'] = item['Answer']
                    question['OptionA'] = item['SelectedItems'][0]['Content']
                    question['OptionB'] = item['SelectedItems'][1]['Content']
                    question['OptionC'] = item['SelectedItems'][2]['Content']
                    question['OptionD'] = item['SelectedItems'][3]['Content']
                    question['OptionE'] = item['SelectedItems'][4]['Content']
                    question['StyleType'] = item['StyleType']
                    question['AllTestID'] = item['AllTestID']
                    # question['ATestID']=item['ATestID']
                    question['SrcID'] = item['SrcID']
                    question['SbjID'] = item['SbjID']
                    question['CptID'] = item['CptID']
                    csv_writer.writerow(question)


if __name__ == '__main__':
    # read_chapter()
    # read_exam()
    chapter=pd.read_csv('data/chapter.csv')
    for id in chapter.third_id:
        print("正在爬取：",id)
        get_chapter_exam(id)
        time.sleep(2)
