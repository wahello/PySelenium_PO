# -*- coding: utf-8 -*-
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("public")
from public import location
from public import saveScreenshot
from public import plogin126mail
from test import test_support
import unittest
import xlrd
import ConfigParser

class Login126Mail(unittest.TestCase):
	"""126邮箱登录测试用例"""
	@classmethod
	def setUpClass(cls):
		print "start"
		cls.driver = webdriver.Firefox()
		cls.driver.implicitly_wait(30)
		#声明find_element方法
		cls.fd = location
		cls.savepng = saveScreenshot
		cls.verificationErrors = []
		#载入ini配置文件
		cf = ConfigParser.ConfigParser()
		cf.read("..\\data\\login_126mail_data.ini")
		#读取配置数据
		cls.base_url = cf.get("urlconf", "url")
		#定义用户名密码变量
		# self.username = "auto_tester"
		# self.password = "123qwe"
		#定位关键字变量
		cls.userinput = cf.get("keywords", "userinput")
		cls.passinput = cf.get("keywords", "passinput")
		cls.btnsubmit = cf.get("keywords", "btnsubmit")
		cls.errorwords = cf.get("keywords", "errorwords")
		cls.useridwords = cf.get("keywords", "useridwords")
		cls.lg = plogin126mail.PubLogin("login")
		cls.css = "css"

	def action(self, case_id, case_summary, username, password):
		"""
		caseid:用例标识id
		case_summary: 用例描述
		username：用户名参数
		password：密码参数
		"""
		self.driver.get(self.base_url)
		self.driver.maximize_window()
		print u"========【" + case_id + u"】" + case_summary + u"============="
		print username
		print password
		self.lg.login(username, password, self.driver, self.userinput, self.passinput, self.btnsubmit)
		spanTF = True
		try:
			errortxt = self.fd.find_Element(self.driver, self.css, self.errorwords).text
			spanTF = True
		except:
			spanTF = False
		if spanTF:
			print errortxt
		else:
			print self.driver.title
			self.savepng.saveScreenshot(self.driver, "faild")
			self.assertTrue(self.fd.findId(self.driver, self.useridwords).text, u"登录失败!")

	@staticmethod
	def getTestFunc(case_id, case_summary, username, password):
		def func(self):
			self.action(case_id, case_summary, username, password)
		return func

	@classmethod
	def tearDownClass(cls):
		print "finished"
		cls.driver.quit()

def __generateTestCases():
	data = xlrd.open_workbook("..\\data\\case_data.xls")
	#通过索引顺序获取Excel表
	table = data.sheets()[1]
	for args in range(1, table.nrows):
		txt = table.row_values(args)
		print (txt)
		setattr(Login126Mail, 'test_login126mail_%s' % (txt[0]), Login126Mail.getTestFunc(*txt))
__generateTestCases()


def test_main():
	test_support.run_unittest(Login126Mail)
