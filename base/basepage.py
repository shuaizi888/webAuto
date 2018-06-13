#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
class Base(object):

    def __init__(self,base_url,driver,pagetitle):
        self.base_url = base_url
        self.driver = driver
        self.pagetitle = pagetitle

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url,pagetitle):
        self.driver.get(url)
        print 'hello'
        self.driver.maximize_window()
        assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    def open(self):
        self._open(self.base_url, self.pagetitle)

    def findElement(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver: self.driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except NoSuchElementException as ex:
            assert False, u'未能找到页面{0}元素'.format(ex)


    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)


if __name__ == '__main':
    Base().open()