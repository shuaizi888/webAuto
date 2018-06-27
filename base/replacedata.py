#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import time

import json
import yaml

from base.log import LogDebug


def replacePayload(old,field,val):
    field_location = old.find(field)
    if field_location != -1:
        leftstr = old[:field_location]
        rightstr = old[field_location:]
        rightdou = rightstr.find(',')
        LogDebug().info('查找字段:%s'%field)
        ret = r'%s%s":%d%s' % (leftstr,field,int(val), rightstr[rightdou:])
        LogDebug().info('字段找到并替换:%s'%ret)
        return ret
    else:
        LogDebug().error('%s:字段未找到.'%field)
        return old


'''
#日期时间串
'''
def rndTimeStr():
    curTimeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime()).encode('utf-8'))
    LogDebug().info('生成日期时间串%s'%curTimeStr)
    return curTimeStr.decode('utf-8')

'''
写yaml内容
'''
def writeYmal(yamlPath,data):
    fp = open(yamlPath,'w')
    yaml.dump(data,fp)
    fp.close()



'''
读yaml文件
'''
def getYamlfield(yamlpath):
    f = open(yamlpath,'r')
    cont = f.read()
    ret = yaml.load(cont)
    f.close()
    return ret


def loadTestData(payload,paydic):
    left_location = payload.find('{')
    right_location = payload.rfind('}')

    leftstr = payload[:left_location]
    rightstr = payload[right_location+1:]

    newPayload = leftstr + json.dumps(paydic) + rightstr
    return newPayload

#raw multipart form-data #格式不可动
def MultipartFormData(data):
    data = json.dumps(data).decode('unicode-escape')
    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--' % data

    return payload

