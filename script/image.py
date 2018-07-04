# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os
import time

from selenium import webdriver

from base import gl


def getImage(self):
    '''
    截取图片,并保存在images文件夹
    :return: 无
    '''

    timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
    imgPath = os.path.join(gl.imgPath, '%s.png' % str(timestrmap))
    print imgPath
    self.driver.save_screenshot(imgPath)
    print  'screenshot:', timestrmap, '.png'


def insert_img(driver, Actual, Expect):
    if Actual != Expect:
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(gl.imgPath, '%s.png' % str(timestrmap))
        driver.get_screenshot_as_file(imgPath)
    else:
        pass


if __name__ == '__main__':
    # getImage()
    driver = webdriver.Ie()
    driver.maximize_window()
    # 登陆页面
    driver.get('http://10.246.109.17/fss')
    insert_img(driver, "1", "2")
