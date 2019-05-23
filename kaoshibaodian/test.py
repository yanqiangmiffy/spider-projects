#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: test.py
@time: 2019-05-23 15:59
@description:
"""
import json
import csv
from utils import aes_decrypt
def read_exam(filename):
    """
    读取试题
    :return:
    """

    with open(filename, 'r', encoding='utf-8') as fout:
        data = json.loads(fout.read())
        with open('data/test.csv', 'a', encoding='utf-8') as fout:
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
                if style['StyleID'] == 1 or style['StyleID'] == 2 or style['StyleID'] == 5:
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

read_exam('data/exam/195.json')