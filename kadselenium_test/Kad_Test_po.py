# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email,Kad_Common
from kadselenium_drp import Kad_MoreBuyMoreGiftList_drp,Kad_MealSetting_drp
from kadselenium_po import Kad_NewFlowList_po




class CreateProcess(unittest.TestCase):

    def setUp(self):
        self.driver = Kad_Common.BrowserDrive()
        self.driver.implicitly_wait(30)
        logins=Kad_Login.ManageLogin()
        logins.PoLogin(self.driver)



    #
    # def test_PurchasePlan(self):
    #     u"""新建采购计划"""
    #     driver=self.driver
    #     Kad_NewFlowList_po.ShowAddViewAdd(driver)




    def tearDown(self):
        self.driver.quit()









if __name__ == "__main__":
    unittest.main()



