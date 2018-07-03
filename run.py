#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import time
import unittest

from base.log import LogDebug
from script import result
from script.HTMLTESTRunnerCN import HTMLTestRunner
from testCase.test_login import FYBX
from testCase.test_newqtbx import FYNewQtbx

if __name__=="__main__":

    suite = unittest.TestSuite()
    # 给套件中添加用例，并且可以指定用例的执行顺序
    suite.addTest(FYBX('test_login'))
    suite.addTest(FYNewQtbx('test_newqtbx'))
    # 后续增加测试集
    filename = 'D:\\web\\report\\' + 'test_login' + time.strftime("%Y_%m_%d_%H_%M_%S") + '.html'  # 拼接出测试报告名
    with file(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='费用报销系统自动化测试报告',
                                description='执行结果：',
                                tester = u'Autotester')
        runner.run(suite)
        fp.close()
    LogDebug()
    result.EmailClass().send
