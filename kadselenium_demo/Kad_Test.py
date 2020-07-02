# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
sys.path.append('D:/rj/pycharm/untitled/kadselenium_code')
from selenium.webdriver.common.action_chains import ActionChains
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email



class Meail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Meailadd(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u'设置').click()
        driver.find_element_by_link_text(u'搜索设置').click()
        time.sleep(5)
        driver.find_element_by_link_text(u'保存设置').click()
        time.sleep(5)






    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

