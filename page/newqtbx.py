# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os

from selenium.webdriver.common.by import By

from base import basepage
from base import gl
from script.output import outputdata


class NewQtbx(basepage.BasePage):
    """
    创建其他费用报销单
    """
    new_lframe = (By.ID, 'leftFrame')
    new_bxsqbutton = (By.XPATH, 'html/body/div[1]/div[2]/table/tbody/tr/td/div/div/div[5]/div[2]')
    new_xjbxbutton = (By.XPATH, 'html/body/div[1]/div[2]/table/tbody/tr/td/div/div/div[6]/div/ul/li[1]/div/span[2]')
    new_lframe2 = (By.ID, 'mainFrame')
    new_qtbxbutton = (By.XPATH,
                      'html/body/div[1]/div/table/tbody/tr/td/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[4]/td/a/img')
    new_fjzs = (By.ID, 'invoiceNum')
    new_fjys = (By.ID, 'billNumber')
    new_sqsy = (By.ID, 'remark')
    new_ywzlbutton = (By.ID, 'businessType')
    new_lframe3 = (By.XPATH, './/*[@id="comboxDiv0"]/iframe')
    new_ywzl = (By.XPATH, 'txtName')
    new_ssuobutton = (By.ID, 'btQuery')
    new_ywzlbutton2 = (By.XPATH, '//table[@id="cbTable"]/tbody/tr[2]/td[2]')
    new_fpje = (By.ID, 'expBCurAmount_1')
    new_fyxm = (By.ID, 'expTree_1')
    new_lframe4 = (By.XPATH, './/*[@id="comboxDiv0"]/iframe')
    new_cybox = (By.ID, 'moreExp')
    new_xmfy = (By.ID, 'txtExpense')
    new_fyxmbutton = (By.ID, 'treeDemo_4_span')
    new_save = (By.ID, 'save_cr')
    new_QDbutton = (By.CSS_SELECTOR, '.xubox_yes.xubox_botton1')
    new_hqdh = (By.ID, 'billCode')
    new_tjbutton = (By.ID, 'submit_cr')

    def leftFrame(self):
        self.switch_frame(*(self.new_lframe))

    def mFrame(self):
        self.switch_frame(*(self.new_lframe2))

    def yezlFrame(self):
        self.switch_frame(*(self.new_lframe3))

    def fyzlFrame(self):
        self.switch_frame(*(self.new_lframe4))

    def qdFrame(self):
        self.switch_parent_frame()

    def xmframe(self):
        self.switch_frame3(self.findElement(*(self.new_lframe4)))

    def frame(self):
        self.switch_frame2()

    # 点击报销申请
    @property
    def bxsq_button(self):
        self.findElement(*(self.new_bxsqbutton)).click()

    # 点击新建报销申请
    @property
    def xjbx_button(self):
        self.findElement(*(self.new_xjbxbutton)).click()

    # 点击其他费用报销
    @property
    def qtbx_button(self):
        self.findElement(*(self.new_qtbxbutton)).click()

    # 输入附件页数，附件张数，申请事由
    def inputdata(self, fjzs, fjys, sqsy, fpje):
        self.findElement(*(self.new_fjzs)).send_keys(fjzs)
        self.findElement(*(self.new_fjys)).send_keys(fjys)
        self.findElement(*(self.new_sqsy)).send_keys(sqsy)
        self.findElement(*(self.new_fpje)).clear()
        self.findElement(*(self.new_fpje)).send_keys(fpje)

    #点击选择业务种类
    @property
    def ywzl_button(self):
        self.findElement(*(self.new_ywzlbutton)).click()

    # 输入过滤业务种类
    def inputywzl(self, ywzl):
        self.findElement(*(self.new_ywzl)).send_keys(ywzl)

    #点击搜索
    @property
    def new_ssuo(self):
        self.findElement(*(self.new_ssuobutton)).click()

    #选择过滤后的业务种类
    @property
    def ywzlxz(self):
        self.findElement(*(self.new_ywzlbutton2)).click()

    # 点击费用项目
    @property
    def fyxm_button(self):
        self.findElement(*(self.new_fyxm)).click()

    #勾选常用复选框
    @property
    def cybox_select(self):
        self.findElement(*(self.new_cybox)).click()
        # if self.is_selected():

        # else:
        #     pass

    # 输入过滤项目费用
    def inputxmfy(self, smfy):
        self.findElement(*(self.new_xmfy)).send_keys(smfy)

    #选择过滤后的项目费用
    @property
    def fyxm_gl(self):
        self.findElement(*(self.new_fyxmbutton)).click()

    #点击保存
    @property
    def save(self):
        self.findElement(*(self.new_save)).click()

    #处理弹出提示框
    @property
    def QDbutton(self):
        self.findElement(*(self.new_QDbutton)).click()

    @property
    def outputhqdh(self):
        values = self.findElement(*(self.new_hqdh)).get_attribute('value')
        filepath = os.path.join(gl.dataPath, 'outputdata.txt').decode('utf-8')
        outputdata(filepath, values)
        #print values

    @property
    def tjbutton(self):
        self.findElement(*(self.new_tjbutton)).click()
