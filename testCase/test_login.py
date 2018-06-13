#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from page.loginpage import Loginpage
class FYBX(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.url = 'http://10.246.109.17/fss'

    def test_login(self):
        login = Loginpage(self.url,self.driver,u'财务共享自助服务门户')
        login.open()
        login.inputUserName('chenminghui.lube')
        login.inputPassword('1')
        login.cboxUser
        login.btnClick
        # driver = self.driver
        # driver.get(self.url)
        # driver.find_element_by_id('loginname').send_keys('chenminghui.lube')
        # driver.find_element_by_id('password').send_keys('1')
        # checkbox = driver.find_element_by_id('remenberUser')
        # if not checkbox.is_selected():
        #     checkbox.click()
        # driver.find_element_by_class_name('button').click()
        #driver.get_screenshot_as_file('D:\\web\\report\\123.jpg')



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()

