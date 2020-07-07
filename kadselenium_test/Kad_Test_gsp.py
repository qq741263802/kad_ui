# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email,Kad_Common
from kadselenium_gsp import Kad_FirstOperationGoodFile_gsp,Kad_LicenseDefinitions_gsp
from kadselenium_model import Kad_Connect_db


class First(unittest.TestCase):

    def setUp(self):
        self.driver = Kad_Common.BrowserDrive()
        self.driver.implicitly_wait(30)
        logins=Kad_Login.ManageLogin()
        logins.GspLogin(self.driver)


    # def test_ApprovalNoQuery(self):
    #     u"""首营商品档案批准文号查询"""
    #     driver=self.driver
    #     FirstOperationGoodFile_gsp.ApprovalNoQuery(driver,u"国药准字Z44021940")
    #
    #
    # def test_WareCodeQuery(self):
    #     u"""商品编码查询"""
    #     driver=self.driver
    #     FirstOperationGoodFile_gsp.WareCodeQuery(driver,"478")


    # def test_WareCodeQuery(self):
    #      u"""证照查询"""
    #     driver=self.driver
    #     LicenseDefinitions_gsp.LicenseCodeQuery(driver,"44480018")


    # def test_LicenseAdd(self):
    #     u"""新增证照"""
    #     driver = self.driver
    #     Kad_LicenseDefinitions_gsp.LicenseAdd(driver, u"证照测试")




    def tearDown(self):
        time.sleep(3)
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()













