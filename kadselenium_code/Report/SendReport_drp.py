# -*- coding: utf-8 -*-
from kadselenium_code import Kad_Email,Kad_Page
from kadselenium_code.Report import Sendservices

def drpsendrep():
    reportpath = 'D:\jemterager\\report\drp\html'
    receiver = ['lihuaming@360kad.com']
    subject = '分销系统接口自动化测试报告'
    user='lihuaming@360kad.com'
    pwd='qq123456'
    Sendservices.SendReport(reportpath,receiver,subject,user,pwd)

drpsendrep()




