# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from kadselenium_code import Kad_Page,Kad_Login,Kad_Common
from selenium.webdriver.common.by import By


#证照列表
class LicenseDefinitions(Kad_Page.Page):

    #列表全局变量
    LicenseIframe='40b08b24-610c-4984-b7a6-88aeaac63109'
    License=(By.XPATH,'//*[@id="main_menu_tree"]/li[2]/ul/li[4]/div/span')
    LicenseCode=(By.XPATH,'//*[@id="search_form|0"]/div/input')
    LicenseName=(By.XPATH,'//*[@id="search_form|1"]/div/input')
    Undefined = (By.XPATH, '//*[@id="search_form|2"]/div/div/input')
    Yes = (By.XPATH, '/html/body/div[5]/div[1]/table/tbody/tr[1]/td')
    Create=(By.XPATH, '//*[@id="main_grid"]/div[3]/div/div[1]/span')
    Start = (By.XPATH, '//*[@id="main_grid"]/div[3]/div/div[3]/span')
    Stop = (By.XPATH, '//*[@id="main_grid"]/div[3]/div/div[5]/span')
    EditAttr = (By.XPATH, '//*[@id="main_grid|1|r1001|c110"]/div/a[1]')
    Modify= (By.XPATH, '//*[@id="main_grid|1|r1001|c110"]/div/a[2]')
    Classify= (By.XPATH, '//*[@id="main_grid|1|r1001|c110"]/div/a[3]')
    Query=(By.XPATH,'//*[@id="search_form"]/ul/li[1]/div/span')
    Reset=(By.XPATH,'//*[@id="search_form"]/ul/li[2]/div/span')

    # 新增页面全局变量
    CreateIframe='single_dialog'
    LicenseNameAdd=(By.XPATH,'//*[@id="main_form|1"]/div/input')
    LicenseType = (By.XPATH, '//*[@id="main_form|2"]/div/div/input')
    SupplierLicense = (By.XPATH, '/html/body/div[1]/div[1]/table/tbody/tr[1]/td')
    EditAttrAdd = (By.XPATH, '//*[@id="main_form|3"]/div/div/input')
    YesAdd = (By.XPATH, '/html/body/div[2]/div[1]/table/tbody/tr[2]/td')
    Confirm = (By.XPATH, '//*[@id="single_dialog"]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/div[3]')






    # region 列表
    def LicenseIframe_ml(self):
        self.frame(self.LicenseIframe)

    # 证照列表
    def License_ml(self):
        self.find_element(*self.License).click()

    # 证照编码查询文本框
    def LicenseCode_ml(self,text):
        self.find_element(*self.LicenseCode).send_keys(text)


    # 证照名称查询文本框
    def LicenseName_ml(self, text):
        self.find_element(*self.LicenseName).send_keys(text)

    # 是否停用查询文本框
    def Undefined_ml(self, text):
        self.find_element(*self.Undefined).click()
    def Yes_ml(self, text):
        self.find_element(*self.Yes).click()



    # 新增按钮
    def Create_ml(self):
        self.find_element(*self.Create).click()

    # 启用按钮
    def Start_ml(self):
        self.find_element(*self.Start).click()

    #停用按钮
    def Stop_ml(self):
        self.find_element(*self.Stop).click()

    #编辑证照属性
    def EditAttr_ml(self):
        self.find_element(*self.EditAttr).click()


    #修改
    def Modify_ml(self):
        self.find_element(*self.Modify).click()

    #分类
    def Classify_ml(self):
        self.find_element(*self.Classify).click()
    # endregion

    # 查询按钮
    def Query_ml(self):
        self.find_element(*self.Query).click()


    #重置按钮
    def Reset_ml(self):
        self.find_element(*self.Reset).click()




#新增页面
    # 新增框架
    def CreateIframeAdd_ml(self):
        self.frame(self.CreateIframe)

    # 证照名称
    def LicenseNameAdd_ml(self,text):
        self.find_element(*self.LicenseNameAdd).send_keys(text)

    # 证照类型
    def LicenseTypeAdd_ml(self):
        self.find_element(*self.LicenseType).click()
    def SupplierLicenseAdd_ml(self):
        self.find_element(*self.SupplierLicense).click()

    # 是否停用
    def EditAttrAdd_ml(self):
        self.find_element(*self.EditAttrAdd).click()
    def YesAdd_ml(self):
        self.find_element(*self.YesAdd).click()


    #确认
    def Confirm_ml(self):
        self.find_element(*self.Confirm).click()







def CommonLicense(driver):
    query=LicenseDefinitions(driver)
    query.License_ml()
    query.LicenseIframe_ml()
    return  query



#证照查询
def LicenseCodeQuery(driver,text):
    query= CommonLicense(driver)
    query.LicenseCode_ml(text)
    query.Query_ml()

#新增证照
def LicenseAdd(driver,text):
    query= CommonLicense(driver)
    query.Create_ml()
    query.CreateIframeAdd_ml()
    query.LicenseNameAdd_ml(text)
    query.LicenseTypeAdd_ml()
    query.SupplierLicenseAdd_ml()
    query.EditAttrAdd_ml()
    query.YesAdd_ml()
    Kad_Common.RetrunContent(driver)
    query.LicenseIframe_ml()
    query.Confirm_ml()
