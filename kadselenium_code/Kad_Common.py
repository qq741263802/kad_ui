# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os,HTMLTestRunner,datetime,uuid,urllib, urllib2,sys,cookielib



#启动浏览器驱动函数
def BrowserDrive():

    driver=webdriver.Chrome()

    return driver


def BrowserDriveIe():

    driver=webdriver.Ie()

    return driver


#返回到最顶层框架
def RetrunContent(driver):
    driver.switch_to_default_content()



#获取系统当前时间
def ObtainNowTime():
    timeArray = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowtimedate = datetime.datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S')
    return nowtimedate


#生成guid
def GetGuid():
    guid = uuid.uuid1()
    return guid


def Httpcclientapi(url):

#定义接收服务器cookies方法
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)



#请求接口
    req = urllib2.Request(url=url)
    res_data = urllib2.urlopen(req)
    return res_data


