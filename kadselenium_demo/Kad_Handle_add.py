# -*- coding: utf-8 -*-
from selenium import webdriver
import sys,time, urllib, urllib2, json,requests,re,datetime,uuid,os,HTMLTestRunner,unittest,thread,cookielib
sys.path.append('D:\\rj\pycharm\untitled\kadselenium_test')
sys.path.append('D:\\rj\pycharm\untitled\kadselenium_code')
from kadselenium_code import Kad_Login,Kad_Page,Kad_Common
from kadselenium_drp import Kad_MealSetting_drp
from kadselenium_po import Kad_NewFlowList_po
from selenium.webdriver.common.by import By
from kadselenium_model import Kad_Connect_db,Kad_Oracle_db,Kad_TsetDbService

url='http://rcunion.360kad.com/Khy/GetWare?wareCode=478&key=khy123'
text=Kad_Common.Httpcclientapi(url)
print text






#driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# driver=webdriver.Ie()
# driver.get("http://www.baidu.com")
# time.sleep(10)
# print driver.title
# driver.quit()



# driver=webdriver.Chrome()
# driver.get('http://tsteweixin.360kad.com/Store/Home/GetShopHotSaleTopWare')
#token = '%2b3pUnzufGxI%2fPMBSmfkyCiQWuN1x0y0XR%2b73MuLUs%2fdyCpbPlOt%2bsEXQH0DV11EK%2frkphRtTTxQE3n0aBr15lJ3YPUehlHD7BcwmaGcSbyi6s1x5Tjj%2fnA7d%2ba63Bz1PbBTn6zet7XM9yYzixTRoCvTjMFWbz3JHBmlWG5iARKNr3oZfDax7cfs%2b%2b1VDVA4Hm7%2feENGmP7hmR1158wnXNArGedk5gVmaaGrSZQgx58NeH9N3U5S1FRjj%2beiDIHU9hzYglCX3KvdP9VXyzqhtpN7GvtGP5lIXrTOygEnDU6LSHNjpFUQmcR65GVK5XtHulaigzB2INZWCq1f1uOZCRVkO2cIhSzHxX7PAMOt4rvUnOCt43y7%2fMw%3d%3d'
# user='13535485194'
# unionid='opeeCv7qsFfGvfoXR4k9uO1jrShM'
# kad_e_openid='oZMPOt99k9ND-7Ufq_Y8E6IK6KqY'
# driver.add_cookie({'name': 'k_e_m_token', 'value': token})
# driver.add_cookie({'name': 'k_e_m_user', 'value': user})
# driver.add_cookie({'name': 'kad_e_unionid', 'value': unionid})
# driver.add_cookie({'name': 'kad_e_openid', 'value': kad_e_openid})
# driver.get("http://tsteweixin.360kad.com/Store/Home/GetShopHotSaleTopWare")
# title=driver.page_source
# print title

#
# url_list = re.findall('href=\"(.*?)\"', title, re.S)
# url_all = []
# for url in url_list:
#     if "http" in url:
#         print url
#     url_all.append(url)
#     # 最终的 url 集合
#     print url_all









#
# kadtoken='3EA20Zdm0TmOyneUPY3Jl51rBacGamwcB7DHlh0Sn%2fjjT5x1s6iybP1zB36a%2bd7AbBzYy9MX7tez6nWFMjTvCoRTxiTbRAi5GWlmBHJ3KE9Po%2f%2bAkuPKzcTlbzJ1%2bE%2bip8JO%2f22k6BChGEnYak%2b45kyQcivLZ3ugGUgNHwTFJrGeLuPYMPekc1RfrhUfGW6YS9x0Purp6FFECxVuyv5hLVwpyXkKPBDqNlfM1kAPqOZXXe97NMEJxc49bx1WZVl%2bfilg5NrD9q0HBnwq8suQspbkKwV%2bkXEC0Jmn4nVxnWmrChBle%2fGDXJoCxP%2b1ygn1tiyX0SDfec%2bDpNK3KmNY87VGEKsCsTdch%2fXTdUmXPWBJyETdEA4UTQ%3d%3d'
# username='18924260022'
# nowtime=Kad_Common.ObtainNowTime()
# mm=Kad_Oracle_db.UpdateToken(kadtoken,nowtime,username)

# nowtime=Kad_Common.ObtainNowTime()
#print type(nowtime)
#print Kad_Common.GetGuid()




# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# logins = Kad_Login.LoginSet()
# logins.ManageLogin(driver)
# NewFlowList_po.Createtestpl(driver)
# ss = (By.XPATH, '//*[@id="新建请求【库存分析转计划申请】"]')
# frame = driver.find_element(ss)
# driver.switch_to_frame(frame)

#
# re=open("E:\quesly.txt")
# value=re.readlines()
# for seach in value:
#     print seach

# a='60e1546e-2f18-11e7-83de-b083fe8877ed'
# b='lihuaming'
# web=webdriver.Chrome()
# ll=Kad_Login.LoginSet()
# v=ll.ManageLogin(web)
# db=Connect_db.kadmodel()
# db.UpdateToken(v,b)
#db.mgcookies(a,b,v)
# print uuid.uuid3(a,b)
# print uuid.uuid1()


# reust=os.listdir('D:\\rj\pycharm\\untitled')
# for a in reust:
#     try:
#         s = a.split('.')[1]
#         if s=='py':
#             os.system('D:\\rj\pycharm\\untitled\\%s 1>>log.txt 2>&1'%a)
#     except Exception as e:
#         print e


# po=Kad_Page.PublicMethod()
# po.AllRun('D:\\rj\pycharm\\untitled')
#
# class tets():
#     def po(self):
#         driver = Kad_Page.BrowserDrive()
#         driver.implicitly_wait(30)
#         logins = Kad_Login.LoginSet()
#         logins.ManageLogin(driver)
#         MealSetting_po.test_user_Query1(driver)
#         driver.quit()
#
#
#
# sui=unittest.TestSuite()
# sui.addTest(tets("po"))
# report = Kad_Page.PublicMethod()
# report.CreatedReport(sui)




#
#
#
# def InterfaceCookies(url,name,token):
# #变量
#     argsdata = {"filters":[{"whereType":"Equal","field":"ProviceCode","value":"440000"}],"sorts":[],"dbKey":None,"entityType":None,"page":1,"pageSize":20}
#     dataurlencode = urllib.urlencode(argsdata)
#     posturl = url
#     if name=='18924260022':
#         cookies = 'k_e_m_user=' + name + ';k_e_m_token=' + token
#     else:
#         cookies = 'Kad_LoginName=' + name + ';Kad_Token=' + token
#
#     cookie_headers = {"Cookie": cookies}
#     tokenvalue=None
#
#
# #请求接口
#     req = urllib2.Request(url=posturl,data=dataurlencode,headers=cookie_headers)
#     res_data = urllib2.urlopen(req)
#     page = res_data.read()
#     print page
#
#
#
#
# #刷新2.0后台token
# url='http://tstmanage.360kad.com/WSS/Customer/GetCusQuerySQL'
# name='lihuaming'
# token=Kad_Oracle_db.QueryToken(name)
# InterfaceCookies(url,name,token)

