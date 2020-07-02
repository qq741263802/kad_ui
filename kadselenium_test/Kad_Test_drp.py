# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
sys.path.append('D:/rj/pycharm/untitled/kadselenium_code')
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email,Kad_Common
from kadselenium_drp import Kad_MoreBuyMoreGiftList_drp,Kad_MealSetting_drp



class Meail(unittest.TestCase):

    def setUp(self):
        self.driver = Kad_Common.BrowserDrive()
        self.driver.implicitly_wait(30)
        logins=Kad_Login.ManageLogin()
        logins.DrpLogin(self.driver)



    #
    # def test_MgQuery(self):
    #     u"""多买多送商品编码查询"""
    #     driver=self.driver
    #     Kad_MoreBuyMoreGiftList_drp.test_user_Query2(driver)


    def test_MgCreate(self):
        u"""新增多买多送活动"""
        driver=self.driver
        Kad_MoreBuyMoreGiftList_drp.test_user_create(driver)
        self




    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
    unittest.main()













