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
from kadselenium_drp import Kad_MoreBuyMoreGiftList_drp
from kadselenium_model import Kad_Connect_db


class Meail(unittest.TestCase):

    def setUp(self):
        self.pp=[];
        time.sleep(2)




    #
    # def test_MgQueryss(self):
    #     mm = Kad_Connect_db.KadModel()
    #     self.pp = mm.WaerQuery()
    #     for var in self.pp:
    #         print var









    def tearDown(self):
        time.sleep(2)





if __name__ == "__main__":
    unittest.main()













