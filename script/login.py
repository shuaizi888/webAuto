# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os

from selenium import webdriver

from base import gl
from base import replacedata
from page.loginpage import Loginpage


def Login():
    driver = webdriver.Ie()
    driver.maximize_window()
    config = replacedata.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
    url = config['LOGIN']['Login_url']
    username = config['LOGIN']['Login_uername']
    password = config['LOGIN']['Login_password']
    login = Loginpage(url, driver, u'财务共享自助服务门户')
    login.open()
    login.inputUserName(username)
    login.inputPassword(password)
    login.cboxUser
    login.btnClick


if __name__ == '__main__':
    Login()
