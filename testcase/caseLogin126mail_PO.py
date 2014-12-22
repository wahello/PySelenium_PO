#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import sys
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("PO")
from PO import LoginPage
from selenium import webdriver
from test import test_support
import ConfigParser
class Caselogin126mail(unittest.TestCase):
	"""
	126邮箱登录的case
	"""
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.driver.implicitly_wait(30)
		#使用ini配置文件读取要访问的url
		cf = ConfigParser.ConfigParser()
		cf.read("..\\data\\login_126mail_data.ini")

		cls.url = cf.get("urlconf", "url")
	#测试用例执行体
	def action(self, case_id, case_summary, username, password):
		login_page = LoginPage.LoginPage(self.driver, self.url, u"网易")
		login_page.open()
		print u"========【" + case_id + u"】" + case_summary + "============="
		print username
		print password
		#调用PO组件
		login_page.input_username(username)
		login_page.input_password(password)
		login_page.saveScreenshot(self.driver, "login")
		login_page.click_submit()
		spanTF = True
		try:
			login_page.show_span()
			spanTF = True
		except:
			spanTF = False
		if spanTF:
			print login_page.show_span()
		else:
			print self.driver.title
			login_page.saveScreenshot(self.driver, "faild")
			self.assertTrue(login_page.show_userid(), u"登录失败")

	@staticmethod
	def getTestFunc(case_id, case_summary, username, password):
		def func(self):
			self.action(case_id, case_summary, username, password)
		return func

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

def __generateTestCases():
	login_page = LoginPage.LoginPage
	table = login_page.casedata("..\\data\\case_data.xls", 1)
	for txt in table:
		print txt
		setattr(Caselogin126mail, 'test_login126mail_%s_%s' % (txt[0],txt[1]), Caselogin126mail.getTestFunc(*txt))
__generateTestCases()


def test_main():
	test_support.run_unittest(Caselogin126mail)