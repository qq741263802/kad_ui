# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email



class Meail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://tstmanage.360kad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
#
    def test_Meailadd(self):
        action=Kad_Login.LoginSet()
        action.ManageLogin(self.driver)
        driver=self.driver
        # 进入对应关系列表
        driver.find_element_by_xpath(".//*[@id='main_menu_tree']/li[3]/ul/li[1]/div/span").click()
        # 切换到对应关系表单点击新增按钮
        try:
            driver.switch_to_frame("d5dd7cde-3cc1-4a05-9354-0e7e63650ae4")
            driver.find_element_by_name("Mealitemcode").send_keys("t_69811bc3")
            driver.find_element_by_xpath('//*[@id="search_form"]/ul/li[1]/div').click()
            driver.find_element_by_xpath('//*[@id="main_grid|2|r1001|c102"]/div/a[2]').click()
            driver.find_element_by_xpath('/html/body/div[12]/table/tbody/tr[2]/td[2]/div/div[3]/div/div[2]/div[3]').click()
            driver.find_element_by_xpath('/html/body/div[12]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]').click()
        except RuntimeError as e:
            print (e)
        finally:
        # 切换到对应关系新增页面表单输入对应关系信息
            driver.find_element_by_xpath(".//*[@id='main_menu']/div[1]/span").click()
            driver.switch_to_frame("add")
            driver.find_element_by_name("Mealitemcode").clear()
            driver.find_element_by_name("Mealitemcode").send_keys("t_69811bc3")
            driver.find_element_by_name("Mealtitle").clear()
            driver.find_element_by_name("Mealtitle").send_keys("t_69811bc3")
            # 选择商品
            driver.find_element_by_xpath(".//*[@id='edit_grid']/div[3]/div/div[1]/span").click()
            driver.switch_to_frame("single_dialog")
            driver.find_element_by_name("WareSkuCode").send_keys("478")
            driver.find_element_by_class_name("l-button").click()
            driver.find_element_by_class_name("l-grid-row-cell-btn-checkbox").click()
            # 再次跳入add表单点击确定保存
            driver.switch_to_default_content()
            driver.switch_to_frame("d5dd7cde-3cc1-4a05-9354-0e7e63650ae4")
            driver.switch_to_frame("add")
            driver.find_element_by_xpath('//*[@id="single_dialog"]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/div[3]').click()
            driver.find_element_by_xpath('//*[@id="main_menu"]/div/span').click()
            time.sleep(10)
            driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[2]/td[2]/div/div[3]/div[1]/div[2]/div[3]").click()
            driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]").click()

    def test_Query(self):

        action=Kad_Login.LoginSet()
        action.ManageLogin(self.driver)
        driver=self.driver
        driver.find_element_by_xpath(".//*[@id='main_menu_tree']/li[3]/ul/li[1]/div/span").click()
        driver.switch_to_frame("d5dd7cde-3cc1-4a05-9354-0e7e63650ae4")
        driver.find_element_by_name("Mealitemcode").send_keys("t_69762hk")
        driver.find_element_by_xpath('//*[@id="search_form"]/ul/li[1]/div').click()
        texts=driver.find_element_by_xpath('//*[@id="main_grid|2|r1001|c104"]/div').text
        self.assertEquals(texts,'t_69762hk')
        print (texts)
        time.sleep(10)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


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
    testunit.addTest(Meail("test_Meailadd"))
    # #生成测试报告
    # rep=Kad_Page.PublicMethod()
    # rep.CreatedReport(testunit)
    # #发送测试报告邮件
    # file=rep.CreatedReportPath()
    # ema=Kad_Email.EmailSet()
    # ema.SendEmailHtml('741263802@qq.com','2.0测试报告',file)