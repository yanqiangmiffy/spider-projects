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

# print(aes_decrypt('9341f888530869cd3b5d7be5913b69cef749311ba5a32e3d8a38acfefd1c7f1cf63b0ca49153b8dbb124762fcb81a369c89baaad978217f341406630bd0dd7ee'))
