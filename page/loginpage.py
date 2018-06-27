#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from base import basepage


class Loginpage(basepage.BasePage):

    login_username = (By.ID,'loginname')
    login_password = (By.ID,'password')
    login_remenberUser = (By.ID, 'remenberUser')
    login_button = (By.CLASS_NAME, 'button')

    #@property
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)


    def inputUserName(self,username):
        self.findElement(*(self.login_username)).send_keys(username)

    def inputPassword(self,password):
        self.findElement(*(self.login_password)).send_keys(password)

    @property
    def cboxUser(self):
        self.findElement(*(self.login_remenberUser)).click()

    @property
    def btnClick(self):
        self.findElement(*(self.login_button)).click()
