# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from kadselenium_code import Kad_Page,Kad_Login
from selenium.webdriver.common.by import By

#新建流程-库存分析转计划申请
class FlowList(Kad_Page.Page):

    #常量区
    Createpo=(By.XPATH,'//*[@id="main_menu_tree"]/li[1]/ul/li[1]/div/span')
    CreatIframe='66c71e81-4961-47bb-a5ba-23be186ce440'
    ShowAddView=(By.XPATH,'//*[@id="list_panel"]/div[2]/div[2]/ul/li/a')
    StockIfram='新建请求【库存分析转计划申请】'
    FiltrationWare=(By.XPATH,'//*[@id="search_form|18"]/div/a')
    FiltrationSales=(By.XPATH,'//*[@id="search_form|19"]/div/a')
    WareCode=(By.NAME,'WareCode')
    Query=(By.XPATH,'//*[@id="layout1"]/div[1]/div[2]/div/div[1]/div[1]/span')
    CheckBoxes=(By.XPATH,'//*[@id="main_grid|hcell|c102"]/div/div')
    CreatePlan=(By.XPATH,'//*[@id="main_menu"]/div[1]/span')
    BuyingLeads=(By.XPATH,'//*[@id="main_grid|2|r1001|c108"]')










    #新建流程框架
    def CreatIframe_fl(self):
        self.frame(self.CreatIframe)


    #选择库存分析转计划框架
    def StockIfram_fl(self):
        self.frame(self.StockIfram)

    # 新建流程列表
    def Createpo_fl(self):
        self.find_element(*self.Createpo).click()

    #库存分析转计划申请
    def ShowAddView_fl(self):
        self.find_element(*self.ShowAddView).click()


    #商品编码填写框
    def WareCode_fl(self,text):
        self.find_element(*self.WareCode).send_keys(text)

    #采购需求数量填写框
    def BuyingLeads_fl(self,text):
        self.find_element(*self.BuyingLeads).send_keys(text)

    # 采购需求数量填写框
    def Buying_fl(self):
        self.find_element(*self.BuyingLeads).click()

    #过滤请购商品复选框
    def FiltrationWare_fl(self):
        self.find_element(*self.FiltrationWare).click()

    #过滤30天无销量复选框
    def FiltrationSales_fl(self):
        self.find_element(*self.FiltrationSales).click()


    #查询按钮
    def Query_fl(self):
        self.find_element(*self.Query).click()


    #勾选商品复选框
    def CheckBoxes_fl(self):
        self.find_element(*self.CheckBoxes).click()



    #生成采购计划
    def CreatePlan_fl(self):
        self.find_element(*self.CreatePlan).click()

def CommonFlowList(driver):
    create=FlowList(driver)
    create.Createpo_fl()
    create.CreatIframe_fl()
    return  create


#新增库存周转计划
def ShowAddViewAdd(driver):
    create=CommonFlowList(driver)
    create.ShowAddView_fl()
    driver.switch_to_default_content()
    create.StockIfram_fl()
    create.FiltrationWare_fl()
    create.FiltrationSales_fl()
    create.WareCode_fl('999332')
    create.Query_fl()









