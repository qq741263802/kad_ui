#coding=utf-8
from appium import webdriver

desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.2', 'deviceName': 'Android Emulator',
                'appPackage': 'com.android.calculator2', 'appActivity': '.Calculator'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()