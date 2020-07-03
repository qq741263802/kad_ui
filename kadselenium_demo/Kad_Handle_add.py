# -*- coding: utf-8 -*-

import requests

def dtest():
    res=requests.get(url='http://www.baidu.com')
    print(res.text)



