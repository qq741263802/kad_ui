# -*- coding: UTF-8 -*-
from selenium import webdriver
from kadselenium_code import Kad_Login,Kad_Common
from kadselenium_model import Kad_Connect_db,Kad_Oracle_db
import time,os

#将cookise写入文本
def CookiesText():

    try:
        driver=webdriver.Chrome()
        login=Kad_Login.ManageLogin()
        login.DrpLogin(driver)
        tokenrb=driver.get_cookie(name='Kad_Token')['value']
        tokenwb = open('C:\Python27\cookies.txt','w')
        tokenwb.write(tokenrb)
    except Exception as e:
        print (e)
    finally:
        driver.quit()
        tokenwb.close()



#更新Mysql数据库2.0后台cookise信息
def MlCookies():

    try:
        driver=webdriver.Chrome()
        login=Kad_Login.ManageLogin()
        login.TestLogin(driver)
        tokenrb=driver.get_cookie(name='Kad_Token')['value']
        name = driver.get_cookie(name='Kad_LoginName')['value']
        uptoken=Kad_Connect_db.KadModel()
        uptoken.UpdateToken(tokenrb,name)
    except Exception as e:
        print (e)
    finally:
        driver.quit()






#更新ORACLE数据库2.0后台cookise信息
def ManageCookies():
    try:
        driver=webdriver.Chrome()
        login=Kad_Login.ManageLogin()
        login.TestLogin(driver)
        tokenrb=driver.get_cookie(name='Kad_Token')['value']
        name = driver.get_cookie(name='Kad_LoginName')['value']
        nowtime=Kad_Common.ObtainNowTime()
        Kad_Oracle_db.UpdateToken(tokenrb,nowtime,name)
    except Exception as e:
        print (e)
    finally:
        driver.quit()

#更新ORACLE数据库E+移动端cookise信息
def WeixinCookies():
    try:
        driver=webdriver.Chrome()
        login=Kad_Login.ManageLogin()
        login.WeixinLogin(driver)
        tokenrb=driver.get_cookie(name='k_e_m_token')['value']
        name = driver.get_cookie(name='k_e_m_user')['value']
        nowtime=Kad_Common.ObtainNowTime()
        Kad_Oracle_db.UpdateToken(tokenrb,nowtime,name)
    except Exception as e:
        print (e)
    finally:
        driver.quit()




ManageCookies()
WeixinCookies()


