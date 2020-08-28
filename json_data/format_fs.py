#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

import requests


class FormatFuncs(object):
    def __init__(self, json_file=None):
        file = r'rate_request10.json'
        if json_file:
            file = json_file
        with open(file, 'r', encoding='utf-8') as fp:
            self.json_dic = json.load(fp)
            self.json_str = json.dumps(self.json_dic)


if __name__=='__main__':
    json_rate=FormatFuncs().json_dic
    res = requests.post(url='http://58.214.27.26:8888/member/anon/rate', json=json_rate)
    print(res.text)
    print(type(json.loads(res.text)["data"]["amount"]/100))
    '''
    print(d["dateTypeMap"])
    print(d["dateTypeMap"]["20200710"])
    print(type(d))
    '''
