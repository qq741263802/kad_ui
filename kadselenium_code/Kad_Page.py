# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os,HTMLTestRunner
from kadselenium_code import Kad_Common
#基础类，用于所有页面类继承
class Page(object):

    login_url = 'http://tstmanage.360kad.com'

    def __init__(self, selenium_driver, base_url=login_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def frame(self,loc):
        return self.driver.switch_to_frame(loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print ('%s page does not have "%s" locator' % (self, loc))


#文件、报告操作类
class PublicMethod():

    #运行测试用例，生成测试报告
    def CreatedReport(self, testunit):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 定义个报告存放路径
        filename = 'E:\\report\\' + now + 'report.html'
        fp = file(filename, 'wb')
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'2.0后台自动化测试报告',
            description=u'用例执行情况：')
        # 运行测试用例
        runner.run(testunit)
        # 关闭报告文件
        fp.close()


    # 按生成时间排序获取文件路径
    def CreatedReportPath(self,pathdir):
        result_dir = pathdir
        lists = os.listdir(result_dir)
        # 重新按时间对目录下的文件进行排列
        lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
        print ('最新的文件为： ' + lists[-1])
        path = os.path.join(result_dir, lists[-1])
        return path


    #根据文件路径获取文本内容
    def AchieveTextContent(self,files):
        self.files=files
        try:
            txtfiles = open(files, 'rb')
            mb_body = txtfiles.read()
            return mb_body
        except Exception as e:
            print(e)
        finally:
            txtfiles.close()



    # 浏览屏幕截图
    def ScreenshotPng(self,driver):
        nowtime = time.strftime("%Y-%m-%d %H_%M_%S")
        filepng='D:\\rj\pycharm\png\\'+nowtime+'end.png'
        driver.get_screenshot_as_file(filepng)


    #批量执行后缀为py的文件
    def AllRun(self,path):
        reust = os.listdir(path)
        for a in reust:
            try:
                s = a.split('.')[1]
                if s == 'py':
                    os.system(''+path+'\\%s 1>>log.txt 2>&1' % a)
            except Exception as e:
                print (e)


    # 批量添加测试套件
    def CreatSuitel(self,path):
        resuite=unittest.TestSuite()
        # discover 方法定义
        discover = unittest.defaultTestLoader.discover(path,
                                                       pattern='Kad_Test*.py',
                                                       top_level_dir=None)
        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                resuite.addTests(test_case)

        return resuite







#测试类
class PlTest(unittest.TestCase):

    def setUp(self):
        self.driver = Kad_Common.BrowserDrive()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()






