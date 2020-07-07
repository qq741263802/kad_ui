# -*- coding: utf-8 -*-
import smtplib,os,sys
from kadselenium_code import Kad_Login,Kad_Page
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart



class EmailSet:
    #HTML文本邮件含附件
    def SendEmailHtml(self,receiver,subject,path,username,password,smtpserver):
            # 发送邮箱服务器
            #smtpserver ='mail.360kad.com'
            smtpserver = smtpserver
            # 定义正文
            f = open(path, 'rb')
            mm_body = f.read()
            f.close()
            #构造附件,发送邮件
            msg=MIMEMultipart()
            msg.attach(MIMEText(mm_body,'html','utf-8'))
            att1 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="repost.html"'
            msg.attach(att1)
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = username
            msg['To'] = ",".join(receiver)
            smm = smtplib.SMTP_SSL(smtpserver,465)
            smm.login(username, password)
            smm.sendmail(username, receiver, msg.as_string())
            smm.quit()

    #普通文本邮件
    def SendEmailText(self, receiver, subject, mailbody,username,password,smtpserver):
            # 发送邮箱服务器
            smtpserver = smtpserver
            # 发送邮件
            msg = MIMEText(mailbody,'html','utf-8')
            msg['Subject'] = Header(subject,'utf-8')
            msg['From'] = username
            msg['To'] = ",".join(receiver)
            smm = smtplib.SMTP_SSL(smtpserver,465)
            smm.login(username,password)
            smm.sendmail(username, receiver, msg.as_string())
            smm.quit()



