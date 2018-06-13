#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
from testCase.test_login import FYBX
import unittest
from script.HTMLTESTRunnerCN import HTMLTestRunner
import time
from script.result import EmailClass
from base.log import LogDebug

if __name__=="__main__":

    suite = unittest.TestSuite()
    # 给套件中添加用例，并且可以指定用例的执行顺序
    suite.addTest(FYBX('test_login'))
    filename = 'D:\\web\\report\\' + 'test_login' + time.strftime("%Y_%m_%d_%H_%M_%S") + '.html'  # 拼接出测试报告名
    with file(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='费用报销系统自动化测试报告',
                                description='执行结果：',
                                tester = u'Autotester')
        runner.run(suite)
        fp.close()
    LogDebug()
    EmailClass().send