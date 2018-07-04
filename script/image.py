# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os
import time

from base import gl


def getImage(self):
    '''
    截取图片,并保存在images文件夹
    :return: 无
    '''
    timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
    imgPath = os.path.join(gl.imgPath, '%s.png' % str(timestrmap))

    self.driver.save_screenshot(imgPath)
    print  'screenshot:', timestrmap, '.png'
