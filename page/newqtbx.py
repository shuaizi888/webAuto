# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from base import basepage


class NewQtbx(basepage.BasePage):
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
    new_ssuobutton = (By.XPATH, 'btQuery')
    new_ywzlbutton2 = (By.XPATH, '//table[@id="cbTable"]/tbody/tr[2]/td[2]')
    new_fpje = (By.ID, 'expBCurAmount_1')
    new_fyxm = (By.ID, 'expTree_1')
    new_lframe4 = (By.ID, './/*[@id="comboxDiv1"]/iframe')
    new_cybox = (By.ID, 'moreExp')
    new_xmfy = (By.ID, 'txtExpense')
    new_fyxmbutton = (By.ID, 'treeDemo_4_span')
    new_save = (By.ID, 'save_cr')
    new_QDbutton = (By.ID, '.xubox_yes.xubox_botton1')
    new_hqdh = (By.ID, 'billCode')
    new_tjbutton = (By.ID, 'submit_cr')

    def leftFrame(self):
        self.switch_frame(self.new_lframe)

    def mainFrame(self):
        self.switch_frame(self.new_lframe2)

    def yezlFrame(self):
        self.switch_frame(self.new_lframe3)

    def fyzlFrame(self):
        self.switch_frame(self.new_lframe4)

    def qdFrame(self):
        self.switch_parent_frame(self.new_QDbutton)

    @property
    def new_bxsqbutton(self):
        self.findElement(*(self.new_bxsqbutton)).click()

    @property
    def new_xjbxbutton(self):
        self.findElement(*(self.new_xjbxbutton)).click()

    @property
    def new_qtbxbutton(self):
        self.findElement(*(self.new_qtbxbutton)).click()

    # 输入附件页数，附件张数，申请事由
    def inputdata(self, fjzs, fjys, sqsy, fpje):
        self.findElement(*(self.new_fjzs)).send_keys(fjzs)
        self.findElement(*(self.new_fjys)).send_keys(fjys)
        self.findElement(*(self.new_sqsy)).send_keys(sqsy)
        self.findElement(*(self.new_fpje)).clear()
        self.findElement(*(self.new_fpje)).send_keys(fpje)

    @property
    def new_ywzlbutton(self):
        self.findElement(*(self.new_ywzlbutton)).click()

    def new_ywzl(self, ywzl):
        self.findElement(*(self.new_ywzl)).send_keys(ywzl)

    @property
    def new_ssuo(self):
        self.findElement(*(self.new_ssuobutton)).click()

    @property
    def ywzlxz(self):
        self.findElement(*(self.new_ywzlbutton2)).click()

    # 点击费用项目
    @property
    def new_fyxm(self):
        self.findElement(*(self.new_fyxm)).click()

    @property
    def new_cybox(self):
        if self.is_selected():
            self.findElement(*(self.new_cybox)).click()

    def new_xmfy(self, smfy):
        self.findElement(*(self.new_xmfy)).send_keys(smfy)

    @property
    def new_fyxmbutton(self):
        self.findElement(*(self.new_fyxmbutton)).click()

    @property
    def save(self):
        self.findElement(*(self.new_save)).click()

    @property
    def QDbutton(self):
        self.findElement(*(self.new_QDbutton)).click()

    @property
    def new_hqdh(self):
        values = self.findElement(*(self.new_hqdh)).get_attribute('value')
        print values

    @property
    def new_tjbutton(self):
        self.findElement(*(self.new_tjbutton)).click()
