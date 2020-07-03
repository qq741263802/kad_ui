# -*- coding: utf-8 -*-
from kadselenium_code import Kad_Email,Kad_Page
from kadselenium_code.Report import Sendservices



def posendrep():
    #附件路径
    reportpath = 'D:\jemterager\\report\po\html'
    # 接收邮箱,多个收件人用逗号隔开
    receiver = ['lihuaming@360kad.com']
    #邮件标题
    subject = 'po系统接口自动化测试报告'
    # 发送邮箱用户/密码
    user='lihuaming@360kad.com'
    pwd='qq123456'
    Sendservices.SendReport(reportpath,receiver,subject,user,pwd)

posendrep()

