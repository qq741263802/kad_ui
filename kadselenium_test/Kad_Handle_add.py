# -*- coding: utf-8 -*-

import requests

def dtest():
    res=requests.get(url='http://localhost:8080/api/startTest?suite=testsuite')
    print(res.text)

dtest()

