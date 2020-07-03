# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email
from kadselenium_drp import Kad_MoreBuyMoreGiftList_drp,Kad_MealSetting_drp



class Meail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        logins=Kad_Login.LoginSet()
        logins.ManageLogin(self.driver)

#
    def test_Meailadd(self):
        driver=self.driver
        Kad_MoreBuyMoreGiftList_drp.test_user_create(driver)


    def test_Query(self):
        driver=self.driver
        Kad_MoreBuyMoreGiftList_drp.test_user_Query2(driver)


    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
    #unittest.main()



    # suite=unittest.TestSuite()
    # suite.addTest(Meail('test_Query'))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    #
    #测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例到测试套件中
    testunit.addTest(Meail("test_Query"))
    #testunit.addTest(Meail("test_Meailadd"))
    # #生成测试报告
    rep=Kad_Page.PublicMethod()
    rep.CreatedReport(testunit)
    # #发送测试报告邮件
    # path=rep.CreatedReportPath()
    # ema=Kad_Email.EmailSet()
    # ema.SendEmailHtml('741263802@qq.com','2.0测试报告',path)













