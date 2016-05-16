# -*- coding: utf-8 -*-
__author__ = 'tsbc'
import re
import urllib
import random
import time

"""循环定时随机访问招聘网站"""

def getHtml(url):
    page = urllib.urlopen(url)
    page.read()
    page.close


zpurl = ['https://www.liepin.com','http://www.yingjiesheng.com','http://www.lagou.com',
         'http://www.chinahr.com','http://www.jobcn.com','http://www.job5156.com',
         'http://www.cjol.com','http://xa.ganji.com/zhaopin','http://xa.58.com/job.shtml?PGTID=0d203675-001e-349f-4725-a1a3ebf9fe4f&ClickID=1',
         'http://www.kanzhun.com','http://www.job9151.com','http://www.guolairen.com',
         'http://www.gaoxiaojob.com','http://www.myjob.com','http://cv.qiaobutang.com',
         'http://www.zbj.com','http://www.taskcn.com','http://www.haitou.cc',
         'http://www.chinalao.com','http://z.paidai.com','http://www.680.com',
         'http://www.quanzhi.com','http://www.dajie.com','http://www.zhaopin.com',
         'http://www.job1001.com','http://www.bohaohr.com','http://www.51job.com'
         ]
#page = getHtml('http://www.zhaopin.com')

print u"执行Url访问开始：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
while True:
    for i in xrange(5):
        time.sleep(0.5)        
        url = random.choice(zpurl)
        try:
            getHtml(url)
            print url
        except:
            print '** ' + url + ' is error!'
    time.sleep(15)
print u"脚本执行完成：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
