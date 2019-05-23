#!/usr/bin/env python
# encoding: utf-8
"""
@author: quincyqiang
@software: PyCharm
@file: main.py
@time: 2019-05-23 10:54
@description:
"""
import requests

headers = {
    # ':method': 'GET',
    # ':authority': 'www.researchgate.net',
    # ':scheme': 'https',
    # ':path': '/profile.ProfileFeaturedResearchItems.html?accountId=AC%3A1247637',
    # 'accept': 'application/json',
    'rg-request-token': 'aad-QyCRDncoZ0OZVoNFYY/wFFZ42KiBaFckt/mcJ8BSustVMxeLg34vhWxF8bCWjrt5StrkZ8/mAeri019pxfR0XcriEJ5iLe/rcKBrTgTUnOqs+Fhstzi19hGl/K30txdWX700s9H7pN11U6isHbd9Svdg8sQHTLd6YUx3JbDyVF6wGcVwIwo5R0n5s1OyVq3FEqPG/AMX/8MY3E1LVGOQAy1ZKtWXaA4HRFGLIxt2WGQZsmH+/HiiuUkCQGLCFJUKge+BYKKThWJUUy5F3jdzOno3Z0GA',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'referer': 'https://www.researchgate.net/profile/Antonio_Di_Martino3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '__cfduid=d5908767f32d93c057f5d8e88ad8ef4b21557599185; ptc=RG1.7388656050694273863.1557599186; did=jL8qBhrhzplf0h11lmEIoCSdta2OTUvzrTXJBekSL9W0xnZGKYF8ucvFkYwe3msf; _ga=GA1.2.620069123.1557599187; cc=1; rghfp=true; _gid=GA1.2.1549704099.1558577112; isResearcher=yes; classification=institution; pl=i1fRL2MMFZFuRNpGE7HFDnN2CfM5wn8yIEK0DO2vfvjnILvdVt04lLMqTKVICouKvXZLkafwzKwr6O0uXFxfYkC5HQyGQCWQ4MkUQ2Kzhul3ndbTbpZmPpk2DMSL17jn; sid=2Iv0f7sT8pgD0BfqObjlh9cuzy3qnY3Xd6jKjIY0vJ6MXoTmsGAaRrF9iydOqT8ZdOiei4vYFO3jNK5uUkAFPbF1gUigeqx31vxWOyjlebVUqJFu1LsnkuT7wp1A7B7R; cili=_2_YzY4MThlYmQwMjc0NzNmYTJiY2I5MWQyMDk5YjQwNGEyYzRlYjg4NDBkMTM3ZGJjNGY4YWJjYzljYWVjNWYxN18xNTc3NTUxMjsw; cirgu=_1_ndqavgf9ViYxg2HCYh4fBaoAC32TSJzSVOExUiQLoMsqgzxtUrwbeNv94rU4uj7uMCJXeS8%3D; _mkto_trk=id:931-FMK-151&token:_mch-researchgate.net-1558578329714-44690; _gat=1',
    'referer': 'https://www.researchgate.net/profile/Antonio_Di_Martino3',
    'rg-request-token': 'aad-QyCRDncoZ0OZVoNFYY/wFFZ42KiBaFckt/mcJ8BSustVMxeLg34vhWxF8bCWjrt5StrkZ8/mAeri019pxfR0XcriEJ5iLe/rcKBrTgTUnOqs+Fhstzi19hGl/K30txdWX700s9H7pN11U6isHbd9Svdg8sQHTLd6YUx3JbDyVF6wGcVwIwo5R0n5s1OyVq3FEqPG/AMX/8MY3E1LVGOQAy1ZKtWXaA4HRFGLIxt2WGQZsmH+/HiiuUkCQGLCFJUKge+BYKKThWJUUy5F3jdzOno3Z0GA',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
res = requests.get(url=' https://www.researchgate.net/profile.ProfileFeaturedResearchItems.html?accountId=AC%3A1247637',headers=headers)
print(res.text)