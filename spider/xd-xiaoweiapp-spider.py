#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23
# @Author  : XDN01
# @Site    : www.raosong.cc
# @File    : xd-xiaoweiapp-spider.py
import requests
import csv
import json

with open("./spider.csv","w",encoding='utf-8') as f:
    writer = csv.writer(f)
    key_array = ['userId','userNum','name','sex','address','certificate','nationId','nationName',
    'phone','email','schoolName','faculty','grade','class','profession','sysStuDetailId','sourceId',
    'sourceName','feature','type','suspId']
    writer.writerow(key_array)

    for a in range(2,20):
        url = 'http://example.com/search.php?userId={}'.format(a)
        json_data =requests.get(url).json()['data']
        # print(json_data)
        value_array = []
        for k in key_array:
            if k in json_data:
                value_array.append(json_data[k])
            else:
                value_array.append('null')
        # print(value_array)
        writer.writerow(value_array)
        print('第{}条数据写入完成'.format(a-1))
