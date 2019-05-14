#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: utils.py 
@time: 2019-05-15 01:50
@description:
"""
import execjs


def aes_decrypt(s):
    with open('yingSoftSetTest.js', 'r', encoding='utf-8') as fout:
        js = fout.read()

    ctx = execjs.compile(js)
    res = ctx.call("aesDecrypt", s)
    return res
