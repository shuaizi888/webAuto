#__author__ = 'shuai'
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
import time
from base import replacedata
from base import gl
import yaml,os,base64


class EmailClass(object):
    def __init__(self):
        self.curDateTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #当前日期时间
        self.config = replacedata.getYamlfield(os.path.join(gl.configPath,'config.yaml')) #配置文件路径
        self.sender = self.config['EMAIL']['Smtp_Sender'] # 从配置文件获取，发件人
        self.receivers = self.config['EMAIL']['Receivers']  # 从配置文件获取，接收人
        self.msg_title = self.config['EMAIL']['Msg_Title'] #从配置文件获取，邮件标题
        self.sender_server = self.config['EMAIL']['Smtp_Server'] #从配置文件获取，发送服务器
        self.From = self.config['EMAIL']['From']
        self.To = self.config['EMAIL']['To']

    '''
    配置邮件内容
    '''
    @property
    def setMailContent(self):
        print self.receivers
        msg = MIMEMultipart()
        msg['From'] = Header(self.From,'utf-8')
        msg['To'] = self.To
        msg['Subject'] = Header('%s%s'%(self.msg_title,self.curDateTime),'utf-8')

        testReport = 'D:\\web\\report'
        lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
        lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
        file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
        #print file_new
        list = file_new.split('\\')
        name = list[3]
        #reportfile = os.path.join(gl.reportPath, 'Report.html')
        fp = open(file_new, 'rb')
        reportHtmlText = fp.read()
        msg.attach(MIMEText(reportHtmlText,'html','utf-8'))

        ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)

        # 附件-文件
        file = MIMEBase(maintype, subtype)
        file.set_payload(reportHtmlText)
        file.add_header('Content-Disposition', 'attachment', filename=name)
        encoders.encode_base64(file)
        msg.attach(file)
        file_log = MIMEBase(maintype, subtype)
        file_log.set_payload(reportHtmlText)
        file_log.add_header('Content-Disposition', 'attachment', filename='logging.log')
        encoders.encode_base64(file_log)
        msg.attach(file_log)
        fp.close()
        return msg


    '''
    发送电子邮件
    '''
    def sendEmail(self,message):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.sender_server,25)
            smtpObj.login(self.config['EMAIL']['Username'],self.config['EMAIL']['Password'])
            smtpObj.sendmail(self.sender,self.receivers , message.as_string())
            smtpObj.quit()
            print "邮件发送成功"
        except smtplib.SMTPException as ex:
            print "Error: 无法发送邮件.%s"%ex

    #发送调用
    @property
    def send(self):
        self.sendEmail(self.setMailContent)

if __name__=="__main__":
    EmailClass().send
