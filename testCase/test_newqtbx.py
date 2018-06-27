#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os
import unittest
from time import sleep

from selenium import webdriver

from base import gl
from base import replacedata
from page.newqtbx import NewQtbx
from testCase.test_login import FYBX


class FYBX(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        self.url = self.config['LOGIN']['Login_url']
        FYBX.test_login()
        # self.username = self.config['LOGIN']['Login_uername']
        # self.password = self.config['LOGIN']['Login_password']
        # login = Loginpage(self.url,self.driver,u'财务共享自助服务门户')
        # login.open()
        # login.inputUserName(self.username)
        # login.inputPassword(self.password)
        # login.cboxUser
        # login.btnClick

    def test_newqtbx(self):
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        self.url = self.config['NEWQTBX']['New_url']
        qtbx = NewQtbx(self.url, self.driver, u'财务共享费用报销系统')
        qtbx.leftFrame()
        qtbx.new_bxsqbutton
        qtbx.new_xjbxbutton
        qtbx.mainFrame()
        qtbx.new_qtbxbutton
        qtbx.inputdata('1', '1', u'自动化测试', '100')
        qtbx.new_ywzlbutton
        qtbx.yezlFrame
        qtbx.new_ywzl('002')
        qtbx.new_ssuo
        sleep(3)
        qtbx.ywzlxz
        sleep(3)
        qtbx.mainFrame()
        qtbx.new_fyxm
        qtbx.fyzlFrame
        qtbx.new_cybox
        qtbx.new_xmfy(u'项目培训费')
        qtbx.new_ssuo
        qtbx.new_fyxmbutton
        qtbx.mainFrame()
        qtbx.save
        qtbx.new_hqdh

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
