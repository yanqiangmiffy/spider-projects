#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: a3a4b1.py
@time: 2019-05-15 15:24
@description:
"""
import json
from utils import aes_decrypt

# with open('data/exam/898.json', 'r', encoding='utf-8') as fout:
#     data = json.loads(fout.read())
#     with open('data/question.csv', 'a', encoding='utf-8') as fout:
#         for style in data['data']['test']['StyleItems']:
#             if style['StyleID'] == 4:
#                 # print(style)
#                 for item in style['TestItems']:
#                     with open('item.json', 'w', encoding='utf-8') as f:
#                         json.dump(item, f, indent=4, ensure_ascii=False)
#                         FrontTitle = aes_decrypt(item['FrontTitle'])
#                         # A3TestItems
#                         for a3item in item['A3TestItems']:
#                             title = FrontTitle + aes_decrypt(a3item['Title'])
#                             print(title)
#                             print(a3item)
#                             # print(a3item['SelectedItems'])
#                         break


# with open('data/exam/898.json', 'r', encoding='utf-8') as fout:
#     data = json.loads(fout.read())
#     with open('data/question.csv', 'a', encoding='utf-8') as fout:
#         for style in data['data']['test']['StyleItems']:
#             if style['StyleID'] == 4:
#                 # print(style)
#                 for item in style['TestItems']:
#                     FrontTitle = aes_decrypt(item['FrontTitle'])
#                     # A3TestItems
#                     for a3item in item['A3TestItems']:
#
#                         title = FrontTitle + aes_decrypt(a3item['Title'])
#                         title = title.strip()
#
#                         question = dict()
#                         question['Title'] = title
#                         question['Explain'] = a3item['Explain']
#                         question['TestPoint'] = a3item['TestPoint']
#                         question['Answer'] = a3item['Answer']
#
#                         question['OptionA'] = ''
#                         question['OptionB'] = ''
#                         question['OptionC'] = ''
#                         question['OptionD'] = ''
#                         question['OptionE'] = ''
#
#                         question['OptionA'] = a3item['SelectedItems'][0]['Content']
#                         question['OptionB'] = a3item['SelectedItems'][1]['Content']
#                         question['OptionC'] = a3item['SelectedItems'][2]['Content']
#                         question['OptionD'] = a3item['SelectedItems'][3]['Content']
#                         if len(a3item['SelectedItems']) > 4:
#                             question['OptionE'] = a3item['SelectedItems'][4]['Content']
#                         question['StyleType'] = item['StyleType']
#                         question['AllTestID'] = item['AllTestID']
#                         # question['ATestID']=item['ATestID']
#                         question['SrcID'] = item['SrcID']
#                         question['SbjID'] = item['SbjID']
#                         question['CptID'] = item['CptID']
#                         # print(a3item['SelectedItems'])
#             if style['StyleID'] == 3:
#                 # print(style)
#                 for item in style['TestItems']:
#                     # print(item)
#                     for bitem in item['BTestItems']:
#                         # print(bitem)
#                         title = aes_decrypt(bitem['Title'])
#                         # print(title)
#                         # print(item['SelectedItems'])
#                         title = title.strip()
#                         question = dict()
#                         question['Title'] = title
#                         question['Explain'] = bitem['Explain']
#                         question['TestPoint'] = bitem['TestPoint']
#                         question['Answer'] = bitem['Answer']
#
#                         question['OptionA'] = ''
#                         question['OptionB'] = ''
#                         question['OptionC'] = ''
#                         question['OptionD'] = ''
#                         question['OptionE'] = ''
#
#                         question['OptionA'] = item['SelectedItems'][0]['Content']
#                         question['OptionB'] = item['SelectedItems'][1]['Content']
#                         question['OptionC'] = item['SelectedItems'][2]['Content']
#                         question['OptionD'] = item['SelectedItems'][3]['Content']
#                         if len(item['SelectedItems']) > 4:
#                             question['OptionE'] = item['SelectedItems'][4]['Content']
#                         question['StyleType'] = item['StyleType']
#                         question['AllTestID'] = item['AllTestID']
#                         # question['ATestID']=item['ATestID']
#                         question['SrcID'] = item['SrcID']
#                         question['SbjID'] = item['SbjID']
#                         question['CptID'] = item['CptID']
#                         print(question)

from main import read_exam
read_exam('data/exam/898.json')