# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,time,os
from kadselenium_code import Kad_Page
from kadselenium_model import Kad_Connect_db,Kad_Oracle_db



#2.0后台cookies获取
def CreateCookies(driver):
    token=Kad_Oracle_db.QueryToken('lihuaming')
    driver.get("http://tstmanage.360kad.com")
    driver.add_cookie({'name': 'Kad_LoginName', 'value': 'lihuaming'})
    driver.add_cookie({'name': 'Kad_Token', 'value': token})
    driver.get("http://tstmanage.360kad.com")
    driver.find_element_by_id("mico00").click()





class ManageLogin():
    #官网登录函数
    def PcLogin(self,driver,username,password):
        driver.get("http://tstuser.360kad.com/Login?ReturnUrl=http://tstwww.360kad.com/")
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys(username)
        driver.find_element_by_id("UserPassword").clear()
        driver.find_element_by_id("UserPassword").send_keys(password)
        driver.find_element_by_id("LoginButton").click()

    #官网退出登录函数
    def PcLogout(self,driver):
        driver.find_element_by_link_text(u"退出").click()



    #微信登录函数
    def WeixinLogin(self,driver):
        driver.get('http://tsteweixin.360kad.com/Store/Home/GetShopHotSaleTopWare')
        user = '18905847739'
        unionid = 'opeeCv7qsFfGvfoXR4k9uO1jrShM'
        openid = 'oZMPOt99k9ND-7Ufq_Y8E6IK6KqY'
        token = Kad_Oracle_db.QueryToken(user)
        driver.add_cookie({'name': 'k_e_m_token', 'value': token})
        driver.add_cookie({'name': 'k_e_m_user', 'value': user})
        driver.add_cookie({'name': 'kad_e_unionid', 'value': unionid})
        driver.add_cookie({'name': 'kad_e_openid', 'value': openid})
        driver.get("http://tsteweixin.360kad.com/Store/Home/GetShopHotSaleTopWare")



    #2.0后台登录函数
    def TestLogin(self,driver):
        CreateCookies(driver)


    #2.0后台登录函数（分销系统）
    def DrpLogin(self,driver):
        CreateCookies(driver)
        driver.find_element_by_id("8b0c8c85-8b5c-4b8e-aadf-6e11e8b7fc9e").click()

    #2.0后台登录函数(采购系统)
    def PoLogin(self,driver):
        CreateCookies(driver)
        driver.find_element_by_id("51ab57a7-2d6c-495a-8c1a-dbc126c39424").click()

        # 2.0后台登录函数(GSP系统）
    def GspLogin(self, driver):
        CreateCookies(driver)
        driver.find_element_by_id("8dd718ae-d866-4b12-af5e-af13b2ec9223").click()


    #2.0后台退出登录函数
    def ManageLogout(self,driver):
        driver.find_element_by_id('logout').click()