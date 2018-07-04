#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os

global globalPath #global包路径
global configPath #config包路径
global dataPath #Data路径
global dataScenarioPath #场景路径
global reportPath #报告路径
global imgPath  # 截图

PATH =lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

globalPath = os.path.abspath(os.path.dirname(__file__)) #不可以加\\，否则取上一级会出错
configPath = os.path.join(os.path.dirname(globalPath),'config') +'\\'
dataPath = os.path.join(PATH(os.path.dirname(globalPath)),'data') +'\\'
reportPath = os.path.join(os.path.dirname(globalPath),'report')+'\\'
imgPath = os.path.join(os.path.dirname(globalPath), 'image') + '\\'

if __name__=="__main__":
    print globalPath
    print configPath
    print dataPath
    print reportPath
    print imgPath
