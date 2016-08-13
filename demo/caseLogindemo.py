# -*- coding:utf-8 -*-
__author__ = 'Ray'

from selenium import webdriver
from test import test_support
import unittest
import xlrd
import time
import logging

class Login126Mail(unittest.TestCase):
	"""126邮箱登录测试用例"""
	@classmethod
	def setUpClass(cls):
		print ("start")
		cls.driver = webdriver.Firefox()
		cls.driver.implicitly_wait(30)

		logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
#日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET #
		console = logging.StreamHandler()
		console.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
		console.setFormatter(formatter)
		logging.getLogger('').addHandler(console)
#################################################################################################

	@classmethod
	def tearDownClass(cls):
		print ("finished")
		# cls.driver.quit()

	def action(self,username, passwd, context):
		self.driver.get("https://gdscas.e-u.cn/login?service=http://gdsportal.e-u.cn:8180/Authentication")
		self.driver.maximize_window()
		# self.driver.get("https://www.baidu.com")
		# print self.driver.page_source
		self.driver.find_element_by_name("username").clear()
		self.driver.find_element_by_name("username").send_keys(username)
		self.driver.find_element_by_name("password").clear()
		self.driver.find_element_by_name("password").send_keys(passwd)
		self.driver.find_element_by_name("Submit").click()
		self.driver.get("http://mail.e-u.cn:8880/jira/browse/NTR-229?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel")
		time.sleep(0.5)
		lastdate = self.driver.find_element_by_xpath("//div[@class='actionContainer'][last()]/div[@class='action-details']//span[@class='date']").text
		ldatelist = lastdate.split(' ')
		ldate = ldatelist[0][3:]
		tday = time.strftime('%m-%d', time.localtime(time.time()))
		print tday

		if ldate == tday:
			return 0
		else:
			self.driver.get("http://mail.e-u.cn:8880/jira/secure/CreateWorklog!default.jspa?id=131471")
			self.driver.find_element_by_name("timeLogged").clear()
			self.driver.find_element_by_name("timeLogged").send_keys("8h")
			now = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))

			self.driver.find_element_by_name("startDate").clear()
			self.driver.find_element_by_name("startDate").send_keys(now)
			self.driver.find_element_by_name("comment").clear()
			self.driver.find_element_by_name("comment").send_keys(context)
			self.driver.find_element_by_name(u"日志").click()
	@staticmethod
	def getTestFunc(username, passwd, context):
		def func(self):
			#执行acation 真正测试用例的执行方法
			self.action(username, passwd, context)
		return func

def __generateTestCases():
	data = xlrd.open_workbook(u"./login.xls")
	#通过索引顺序获取Excel数据
	table = data.sheets()[0]
	#通过for循环生产多个 test_login_ 函数
	for args in range(1, table.nrows):
		txt = table.row_values(args)
		#生成test_login函数后，调用 getTestFunc 进行传参
		setattr(Login126Mail, 'test_login', Login126Mail.getTestFunc(txt[1], txt[2], txt[3]))
__generateTestCases()

if __name__ == "__main__":
	test_support.run_unittest(Login126Mail)