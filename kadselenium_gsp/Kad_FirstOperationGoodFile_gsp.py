# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from kadselenium_code import Kad_Page,Kad_Login
from selenium.webdriver.common.by import By

#首营商品档案列表
class FirstOperation(Kad_Page.Page):

    #常量
    WareIframe='27fd005b-d2eb-4422-bd95-37305bc8bec4'
    WareArchives=(By.XPATH,'//*[@id="main_menu_tree"]/li[2]/ul/li[9]/div/span')
    ApprovalNo=(By.XPATH,'//*[@id="search_form|6"]/div/input')
    Query=(By.XPATH,'//*[@id="search_form"]/ul/li[1]/div/span')
    Confirm=(By.XPATH,'/html/body/div[9]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]')
    Reset=(By.XPATH,'//*[@id="search_form"]/ul/li[2]/div/span')
    WareCode=(By.XPATH,'//*[@id="search_form|0"]/div/input')




    #新建流程框架
    def WareIframe_ml(self):
        self.frame(self.WareIframe)



    # 首营商品档案列表
    def WareArchives_ml(self):
        self.find_element(*self.WareArchives).click()

    # 确认
    def Confirm_ml(self):
        self.find_element(*self.Confirm).click()

    # 商品编码查询文本框
    def WareCode_ml(self,text):
        self.find_element(*self.WareCode).send_keys(text)

    # 批准文号查询文本框
    def ApprovalNo_ml(self,text):
        self.find_element(*self.ApprovalNo).send_keys(text)


    # 查询按钮
    def Query_ml(self):
        self.find_element(*self.Query).click()

    # 重置按钮
    def Reset_ml(self):
        self.find_element(*self.Reset).click()






def CommonFirst(driver):
    query=FirstOperation(driver)
    query.WareArchives_ml()
    query.WareIframe_ml()
    return  query



#批准文号查询
def ApprovalNoQuery(driver,text):
    query= CommonFirst(driver)
    query.ApprovalNo_ml(text)
    query.Query_ml()


#商品编码查询
def WareCodeQuery(driver,text):
    query = CommonFirst(driver)
    query.WareCode_ml(text)
    query.Query_ml()


