#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
import sys, time, os
import caseLogin126mail_PO
import caseCreateContacts
import case_Login126mail
import caseSearchBaidu
import caseSearchBaiduAction

sys.path.append("public")
from public import HTMLTestRunner

#定义单元测试容器
testunit = unittest.TestSuite()


#将测试用例加入测试容器中
#testunit.addTest(unittest.makeSuite(caseLogin126mail_PO.Caselogin126mail))
#testunit.addTest(unittest.makeSuite(caseCreateContacts.CaseContact126mail))
testunit.addTest(unittest.makeSuite(case_Login126mail.Login126Mail))
#testunit.addTest(unittest.makeSuite(caseSearchBaidu.Baidu))
#testunit.addTest(unittest.makeSuite(caseSearchBaiduAction.CaseSearchbaidu))

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。。。
result = "../result/"

tdresult = result + day
if os.path.exists(tdresult):
	filename = tdresult + "/" + now + "_result.html"
	fp = file(filename, 'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

	#运行测试用例
	runner.run(testunit)
	fp.close()  #关闭报告文件
else:
	os.mkdir(tdresult)
	#os.mkdir(tdresult+"/image")
	filename = tdresult + "/" + now + "_result.html"
	fp = file(filename, 'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

	#运行测试用例
	runner.run(testunit)
	fp.close()  #关闭报告文件