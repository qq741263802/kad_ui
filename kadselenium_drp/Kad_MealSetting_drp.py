# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from kadselenium_code import Kad_Page,Kad_Login
from selenium.webdriver.common.by import By



#商品对应关系页面
class MealSetPage(Kad_Page.Page):

    # 常量区
    url=''
    MealList=(By.XPATH,'//*[@id="main_menu_tree"]/li[3]/ul/li[1]/div/span')
    MealiFrame='d5dd7cde-3cc1-4a05-9354-0e7e63650ae4'
    ExportBt=(By.XPATH,'//*[@id="main_menu"]/div[4]/span')
    ExportFrame='single_dialog'
    SWFUpload=(By.ID,'SWFUpload_0')
    ConFirm=(By.XPATH,'//*[@id="single_dialog"]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/div[3]')







    #列表框架切换
    def MealiFrame_ml(self):
        self.frame(self.MealiFrame)


    #详情页框架切换
    def ExportFrame_ml(self):
        self.frame(self.ExportFrame)


    #商品对应关系列表点击
    def MealList_ml(self):
        self.find_element(*self.MealList).click()

    #导出按钮
    def ExportBt_ml(self):
        self.find_element(*self.ExportBt).click()

    #导入页面选择文件
    def SWFUpload_ml(self,text):
        self.find_element(*self.SWFUpload).send_keys(text)

    #导入确认按钮
    def ConFirm_ml(self):
        self.find_element(*self.ConFirm).click()





#对应关系导入
def test_MealImport(driver):
    more_page = MealSetPage(driver)
    more_page.MealList_ml()
    more_page.MealiFrame_ml()
    more_page.ExportBt_ml()
    more_page.ExportFrame_ml()



