# -*- coding: utf-8 -*-
from kadselenium_code import Kad_Email,Kad_Page


#QQ邮箱配置     smtpserver ='smtp.qq.com'，username = '2671459625@qq.com'， password = 'qlhykykzxuqwdjeh'
#企业邮箱配置   smtpserver ='mail.360kad.com'，username = 'lihuaming@360kad.com'， password = 'qq123456'
#发送测试报告
def SendReport(reportpath,receiver,subject,user,pwd):
    sp = Kad_Page.PublicMethod()
    path = sp.CreatedReportPath(reportpath)
    print path
    em = Kad_Email.EmailSet()
    if user=='2671459625@qq.com':
        smtpserver = 'smtp.qq.com'
    else:
        smtpserver = 'mail.360kad.com'

    em.SendEmailHtml(receiver, subject, path,user,pwd,smtpserver)



