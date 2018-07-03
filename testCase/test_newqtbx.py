#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os
import unittest

from selenium import webdriver

from base import gl
from base import replacedata
from page.loginpage import Loginpage
from page.newqtbx import NewQtbx


class FYNewQtbx(unittest.TestCase):
    def setUp(self):
        # Login()
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        self.url = self.config['LOGIN']['Login_url']
        self.username = self.config['LOGIN']['Login_uername']
        self.password = self.config['LOGIN']['Login_password']
        login = Loginpage(self.url, self.driver, u'财务共享自助服务门户')
        login.open()
        login.inputUserName(self.username)
        login.inputPassword(self.password)
        login.cboxUser
        login.btnClick

    def test_newqtbx(self):
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        self.url = self.config['NEWQTBX']['New_url']
        qtbx = NewQtbx(self.url, self.driver, u'财务共享费用报销系统')
        qtbx.leftFrame()
        qtbx.bxsq_button
        qtbx.xjbx_button
        qtbx.frame()
        qtbx.switch_frame3('mainFrame')
        qtbx.qtbx_button
        qtbx.inputdata('1', '1', u'自动化测试', '100')
        # qtbx.ywzl_button
        # qtbx.frame()
        # qtbx.switch_frame3('.//*[@id="comboxDiv0"]/iframe')
        # qtbx.inputywzl('002')
        # qtbx.new_ssuo
        # sleep(3)
        # qtbx.ywzlxz
        # sleep(3)
        # qtbx.frame()
        # qtbx.switch_frame3('mainFrame')
        qtbx.fyxm_button
        qtbx.xmframe()
        qtbx.cybox_select
        qtbx.inputxmfy(u'项目培训费')
        qtbx.new_ssuo
        qtbx.fyxm_gl
        qtbx.frame()
        qtbx.switch_frame3('mainFrame')
        qtbx.save
        qtbx.switch_parent_frame()
        qtbx.QDbutton
        qtbx.frame()
        qtbx.switch_frame3('mainFrame')
        qtbx.outputhqdh
        qtbx.tjbutton
        qtbx.switch_parent_frame()
        qtbx.QDbutton


    def tearDown(self):
        pass
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
