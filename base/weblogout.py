#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
from basepage.weblogin import login
from selenium import webdriver

login()

def logout():
    browser = webdriver.Ie()
    browser.get('http://10.246.109.17/fss/index.action')
    browser.find_element_by_id('logout').click()
    browser.close()

if __name__ =="__main__":
    logout()