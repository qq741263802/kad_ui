# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
sys.path.append('D:/rj/pycharm/untitled/kadselenium_code')
from kadselenium_code import Kad_Login,Kad_Page,Kad_Email
from kadselenium_drp import Kad_MoreBuyMoreGiftList_drp
from kadselenium_test import Kad_Test_drp,Kad_Test_po




#全局变量
path='D:\\rj\\pycharm\\untitled\\kadselenium_test'
receiver='741263802@qq.com'
subject='自动化测试报告'
reportph='E:\\report'
#执行测试并生成测试报告
alltets=Kad_Page.PublicMethod()
repo=alltets.CreatSuitel(path)
alltets.CreatedReport(repo)



#发送测试报告邮件
reportpath=alltets.CreatedReportPath(reportph)
email=Kad_Email.EmailSet()
email.SendEmailHtml(receiver,subject,reportpath)



