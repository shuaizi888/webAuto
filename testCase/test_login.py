#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os
import unittest
from time import sleep

from selenium import webdriver

from base import gl
from base import replacedata
from page.loginpage import Loginpage
from script.image import getImage


class FYBX(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        self.url = self.config['LOGIN']['Login_url']

    def test_login(self):
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        self.username = self.config['LOGIN']['Login_uername']
        self.password = self.config['LOGIN']['Login_password']
        login = Loginpage(self.url,self.driver,u'财务共享自助服务门户')
        login.open()
        login.inputUserName(self.username)
        login.inputPassword(self.password)
        login.cboxUser
        login.btnClick

        sleep(5)
        getImage()
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

