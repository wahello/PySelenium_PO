#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time

def savePngName(name):
    #import time
    tm = saveTime()
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    type = ".png"
    fp = "..\\result\\" + day + "\\image"
    if os.path.exists(fp):
        filename = str(fp)+"\\" + str(tm)+str("_")+str(name)+str(type)
        print filename
        return filename
    else:
        os.makedirs(fp)
        filename = str(fp)+ "\\" + str(tm)+str("_")+str(name)+str(type)
        print filename
        return filename

def saveTime():
    #import time
    #返回当前系统时间以括号中（2014-08-29-15_21_55）展示
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

def saveScreenshot(driver, name):
    image = driver.save_screenshot(savePngName(name))
    return image