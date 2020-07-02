# -*- coding: utf-8 -*-
from kadselenium_code import Kad_Email,Kad_Page
import Sendservices

def emsendrep():
    reportpath = 'D:\jemterager\\report\e+\html'
    receiver = ['lihuaming@360kad.com']
    subject = 'E+微信端接口自动化测试报告'
    user='lihuaming@360kad.com'
    pwd='qq123456'
    Sendservices.SendReport(reportpath,receiver,subject,user,pwd)

emsendrep()



