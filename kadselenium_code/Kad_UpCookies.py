# -*- coding: utf-8 -*-
import sys,time, urllib, urllib2, json,requests,re,datetime,uuid,os,HTMLTestRunner,unittest,thread,cookielib
sys.path.append('D:\\rj\pycharm\untitled\kadselenium_code')
from kadselenium_code import Kad_Login,Kad_Page,Kad_Common
from kadselenium_model import Kad_Connect_db,Kad_Oracle_db


def InterfaceCookies(url,name,token):
#变量
    argsdata = {"filters": [], "sorts": [], "dbKey": None, "entityType": None, "page": 1, "pageSize": 20}
    dataurlencode = urllib.urlencode(argsdata)
    posturl = url
    if name=='lihuaming':
        cookies = 'Kad_LoginName=' + name + ';Kad_Token=' + token

    else:
        cookies = 'k_e_m_user=' + name + ';k_e_m_token=' + token

    cookie_headers = {"Cookie": cookies}
    tokenvalue=None


#定义接收服务器cookies方法
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)



#请求接口
    req = urllib2.Request(url=posturl,data=dataurlencode,headers=cookie_headers)
    res_data = urllib2.urlopen(req)


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



