#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
# coding=utf-8

'''
#python+selenniu+unittest
#Version 1.0
#实现自动创建其他费用销售订单
'''
from time import sleep

from selenium import webdriver


def login():
    browser = webdriver.Ie()
    browser.maximize_window()
    #登陆页面
    browser.get('http://10.246.109.17/fss')
    #输入用户名密码数据
    browser.find_element_by_id('loginname').send_keys('chenminghui.lube')
    browser.find_element_by_id('password').send_keys('1')
    #勾选记住密码
    checkbox = browser.find_element_by_id('remenberUser')
    if not checkbox.is_selected():
        checkbox.click()
    #点击登陆
    browser.find_element_by_class_name('button').click()
    sleep(5)

    #新建其他费用报销单
    lframe = browser.find_element_by_id('leftFrame')
    browser.switch_to.frame(lframe)
    browser.find_element_by_xpath('html/body/div[1]/div[2]/table/tbody/tr/td/div/div/div[5]/div[2]').click()
    #点击新建
    browser.find_element_by_xpath('html/body/div[1]/div[2]/table/tbody/tr/td/div/div/div[6]/div/ul/li[1]/div/span[2]').click()
    #选择其他费用报销
    browser.switch_to.default_content()
    mframe = browser.find_element_by_name('mainFrame')
    browser.switch_to.frame(mframe)
    browser.find_element_by_xpath('html/body/div[1]/div/table/tbody/tr/td/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[4]/td/a/img').click()

    browser.find_element_by_id('invoiceNum').send_keys('1')#附件张数
    browser.find_element_by_id('billNumber').send_keys('1')#附件页数
    browser.find_element_by_id('remark').send_keys(u'自动化测试')#申请事由
    # browser.find_element_by_id('businessType').click()# 业务种类
    #处理业务种类
    # mframe = browser.find_element_by_xpath('.//*[@id="comboxDiv0"]/iframe')
    # browser.switch_to.frame(mframe)
    # browser.find_element_by_id('txtName').send_keys('002')#业务种类选择
    # browser.find_element_by_id('btQuery').click()#搜索
    # sleep(3)
    # browser.find_element_by_xpath('//table[@id="cbTable"]/tbody/tr[2]/td[2]').click()#选择业务种类
    # sleep(3)
    #发票总金额
    browser.switch_to.default_content()
    mframe = browser.find_element_by_name('mainFrame')
    browser.switch_to.frame(mframe)
    browser.find_element_by_id('expBCurAmount_1').clear()
    browser.find_element_by_id('expBCurAmount_1').send_keys('100')
    #点击费用项目
    browser.find_element_by_id('expTree_1').click()
    mframe = browser.find_element_by_xpath('.//*[@id="comboxDiv0"]/iframe')
    browser.switch_to.frame(mframe)
    #常用勾选框
    checkbox = browser.find_element_by_id('moreExp')
    if checkbox.is_selected():
        checkbox.click()
    #费用项目
    browser.find_element_by_id('txtExpense').send_keys(u'项目培训费')
    browser.find_element_by_id('btQuery').click()
    browser.find_element_by_id("treeDemo_4_span").click()

    #保存
    browser.switch_to.default_content()
    mframe = browser.find_element_by_name('mainFrame')
    browser.switch_to.frame(mframe)
    browser.find_element_by_id('save_cr').click()#保存
    #处理确定按钮
    sleep(3)
    browser.switch_to.parent_frame()
    browser.find_element_by_css_selector(".xubox_yes.xubox_botton1").click()
    sleep(3)
    #获取单号
    browser.switch_to.default_content()
    mframe = browser.find_element_by_name('mainFrame')
    browser.switch_to.frame(mframe)
    QIBX = browser.find_element_by_id('billCode').get_attribute('value')
    print QIBX
    #提交
    browser.find_element_by_id('submit_cr').click()
    sleep(5)
    browser.switch_to.parent_frame()
    browser.find_element_by_css_selector(".xubox_yes.xubox_botton1").click()
    sleep(5)


if __name__ == '__main__':
    login()





