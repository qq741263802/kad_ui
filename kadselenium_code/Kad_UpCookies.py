# -*- coding: utf-8 -*-
import sys,time,json,requests,re,datetime,uuid,os,HTMLTestRunner,unittest
from kadselenium_code import Kad_Login,Kad_Page,Kad_Common
from kadselenium_model import Kad_Connect_db,Kad_Oracle_db
from http import cookiejar
import urllib.request,urllib.parse

def InterfaceCookies(url,name,token):
#变量
    argsdata = {"filters": [], "sorts": [], "dbKey": None, "entityType": None, "page": 1, "pageSize": 20}
    dataurlencode = urllib.parse.urlencode(argsdata)
    posturl = url
    if name=='lihuaming':
        cookies = 'Kad_LoginName=' + name + ';Kad_Token=' + token

    else:
        cookies = 'k_e_m_user=' + name + ';k_e_m_token=' + token

    cookie_headers = {"Cookie": cookies}
    tokenvalue=None



#定义接收服务器cookies方法
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)


#请求接口
    req = urllib.request.Request(url=url)
    res_data = urllib.request.urlopen(req)
    return res_data


#保存cookies值
    for c in cj:
        tokenvalue = c.value

    nowtime = Kad_Common.ObtainNowTime()
    Kad_Oracle_db.IFUpdateToken(tokenvalue, nowtime, name)


#刷新2.0后台token
url='http://tstmanage.360kad.com/DRP/MealSetting/Query'
name='lihuaming'
token=Kad_Oracle_db.IFQueryToken(name)
InterfaceCookies(url,name,token)

#刷新微信token
weixinurl='http://tsteweixin.360kad.com/Store/Home/GetShopHotSaleTopWare'
weixinname='18905847739'
weixintoken=Kad_Oracle_db.IFQueryToken(weixinname)
InterfaceCookies(weixinurl,weixinname,weixintoken)



