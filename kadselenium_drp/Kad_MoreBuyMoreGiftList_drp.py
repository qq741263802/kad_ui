# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from kadselenium_code import Kad_Page,Kad_Login
from selenium.webdriver.common.by import By

#多买多送列表页面
class MoreListPage(Kad_Page.Page):

    # 常量区
    url=''
    MoreList_loc=(By.XPATH,'//*[@id="main_menu_tree"]/li[3]/ul/li[2]/div/span')
    ListiFrame_loc='e149dcf9-9452-44dd-8f34-f3ca3f9e8e09'
    NewlyButton=(By.XPATH,'//*[@id="main_menu"]/div')
    Mbmgoutercode = (By.NAME, 'Mbmgoutercode')
    WareSkuCode = (By.NAME, 'WareSkuCode')
    WareName = (By.NAME, 'WareName')
    Platformname = (By.NAME, 'Platformname')
    Storeid = (By.NAME, 'Storeid')
    undefined=(By.NAME, 'undefined')
    Query=(By.XPATH, '//*[@id="search_form"]/ul/li[1]/div/span')
    ResetTing=(By.XPATH, '//*[@id="search_form"]/ul/li[2]/div/span')

    #列表框架切换
    def ListiFrame_ml(self):
        self.frame(self.ListiFrame_loc)


    #多买多送列表点击
    def morelist_ml(self):
        self.find_element(*self.MoreList_loc).click()

    # 新增按钮
    def NewlyButton_ml(self):
        self.find_element(*self.NewlyButton).click()

    # 商家编码文本框
    def Mbmgoutercode_ml(self,text):
        self.find_element(*self.Mbmgoutercode).send_keys(text)

    # 商品编码文本框
    def WareSkuCode_ml(self,text):
        self.find_element(*self.WareSkuCode).send_keys(text)

    # 商品名称文本框
    def WareName_ml(self,text):
        self.find_element(*self.WareName).send_keys(text)

    # 外部平台下拉框
    def Platformname_ml(self):
        self.find_element(*self.Platformname)


    # 选择店铺下拉框
    def Storeid_ml(self):
        self.find_element(*self.Storeid)


    # 状态下拉框
    def undefined_ml(self):
        self.find_element(*self.undefined)


    # 查询按钮
    def Query_ml(self):
        self.find_element(*self.Query).click()


    # 重置按钮
    def ResetTing_ml(self):
        self.find_element(*self.ResetTing).click()

     #请求首页
    def open(self):
        self._open(self.url)


#多买多送详情页面
class MoreEditPage(Kad_Page.Page):

    # 常量区
    url=''
    EditiFrame='add'
    PreserveButton=(By.XPATH,'//*[@id="main_menu"]/div/span')
    Platformname = (By.NAME, 'Platformname')
    Mbmgoutercode= (By.NAME, 'Mbmgoutercode')
    Storeid = (By.NAME, 'Storeid')
    Mbmgquantity = (By.NAME, 'Mbmgquantity')
    CheckBox = (By.XPATH, '//*[@id="edit_form|8"]/div/a')
    WareButton=(By.XPATH, '//*[@id="edit_grid"]/div[3]/div/div[1]/span')
    Platformnametb = (By.XPATH, '/html/body/div[6]/div[1]/table/tbody/tr[1]/td')
    Storeidkad = (By.XPATH, '/html/body/div[7]/div[1]/table/tbody/tr[1]')
    CfPrompt=(By.XPATH,'/html/body/div[8]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]')







 #把每一个元素封装成一个方法

    #编辑页面框架
    def EditiFrame_md(self):
        self.frame(self.EditiFrame)

    #保存按钮
    def PreserveButton_md(self):
        self.find_element(*self.PreserveButton).click()

    # 选择平台下拉框
    def Platformname_md(self):
        self.find_element(*self.Platformname).click()

    # 选择淘宝平台
    def Platformnametb_md(self):
        self.find_element(*self.Platformnametb).click()

    # 选择店铺下拉框
    def Storeid_md(self):
        self.find_element(*self.Storeid).click()

    # 选择康爱多店铺
    def Storeidkad_md(self):
        self.find_element(*self.Storeidkad).click()


    # 商家编码文本框
    def Mdcode_md(self,text):
        self.find_element(*self.Mbmgoutercode).send_keys(text)

    # 购买数量文本框
    def Mbmgquantity_md(self,text):
        self.find_element(*self.Mbmgquantity).send_keys(text)


     # 累加数量多选框
    def CheckBox_md(self):
        self.find_element(*self.Storeid).click()


    # 选择商品按钮
    def WareButton_md(self):
        self.find_element(*self.WareButton).click()

    # 确认提示框
    def CfPrompt_md(self):
        self.find_element(*self.CfPrompt).click()



#多买多送选择商品页面
class ChSkuPage(Kad_Page.Page):

    #常量区
    WareFrame = 'single_dialog'
    WareName=(By.NAME,'WareName')
    SellerCode=(By.NAME,'SellerCode')
    undefined=(By.NAME,'undefined')
    Query=(By.XPATH,'//*[@id="search_form"]/ul/li[1]/div/span')
    ResetTing=(By.XPATH,'//*[@id="search_form"]/ul/li[2]/div/span')
    CheckBoxes=(By.XPATH,'//*[@id="sku_grid|hcell|c102"]/div/div')
    ConFirm=(By.XPATH,'//*[@id="single_dialog"]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/div[3]')
    WareSkuCode=(By.NAME,'WareSkuCode')







    #选择商品框架
    def WareFrame_cs(self):
        self.frame(self.WareFrame)

    # 商品编码文本框
    def WareSkuCode_cs(self,text):
        self.find_element(*self.WareSkuCode).send_keys(text)
    # 商品名称文本框
    def WareName_cs(self,text):
        self.find_element(*self.WareName).send_keys(text)
    # 卖家编号文本框
    def SellerCode_cs(self,text):
        self.find_element(*self.SellerCode).send_keys(text)
    # 虚拟商品文本框
    def undefined_cs(self,text):
        self.find_element(*self.undefined).send_keys(text)

    # 查询按钮
    def Query_cs(self):
        self.find_element(*self.Query).click()

    # 重置按钮
    def ResetTing_cs(self):
        self.find_element(*self.ResetTing).click()

    # 勾选商品复选框
    def CheckBoxes_cs(self):
        self.find_element(*self.CheckBoxes).click()

    # 确认按钮
    def ConFirm_cs(self):
        self.find_element(*self.ConFirm).click()








def test_user_Query1(driver):
    re = open("E:\quesly.txt")
    value = re.readlines()
    more_page = MoreListPage(driver)
    more_page.morelist_ml()
    more_page.ListiFrame_ml()
    for seach in value:
        more_page.Mbmgoutercode_ml(seach)
        more_page.Query_ml()
        more_page.ResetTing_ml()
    time.sleep(5)


def test_user_Query2(driver):
    more_page = MoreListPage(driver)
    more_page.morelist_ml()
    more_page.ListiFrame_ml()
    more_page.WareSkuCode_ml('478')
    more_page.Query_ml()



def test_user_create(driver):
    more_page = MoreListPage(driver)
    edit_page = MoreEditPage(driver)
    ware_page = ChSkuPage(driver)
    more_page.morelist_ml()
    more_page.ListiFrame_ml()
    more_page.NewlyButton_ml()
    edit_page.EditiFrame_md()
    edit_page.Platformname_md()
    edit_page.Platformnametb_md()
    edit_page.Storeid_md()
    edit_page.Storeidkad_md()
    edit_page.Mdcode_md('8955')
    edit_page.Mbmgquantity_md('1')
    edit_page.WareButton_md()
    ware_page.WareFrame_cs()
    ware_page.WareSkuCode_cs('478')
    ware_page.Query_cs()
    time.sleep(5)
    ware_page.CheckBoxes_cs()
    driver.switch_to_default_content()
    more_page.ListiFrame_ml()
    edit_page.EditiFrame_md()
    ware_page.ConFirm_cs()
    edit_page.PreserveButton_md()
    edit_page.CfPrompt_md()






























