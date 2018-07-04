# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os

from base import gl


def outputdata(filepath, data):
    filedata = open(filepath, 'a+')
    filedata.write(data + '\n')
    filedata.close()


if __name__ == "__main__":
    filepath = os.path.join(gl.dataPath, 'outputdata.txt').decode('utf-8')
    outputdata(filepath, '333')
