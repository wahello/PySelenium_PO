#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import sys, time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("PO")
from PO import LoginPage
from PO import ContactsPage
from selenium import webdriver
import ConfigParser

class CaseContact126mail(unittest.TestCase):
	"""登录126邮箱联系人管理测试用例"""
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		#载入ini配置文件
		cf = ConfigParser.ConfigParser()
		cf.read("../data/login_126mail_data.ini")
		#读取配置数据 url地址
		self.url = cf.get("urlconf", "url")
		login_page = LoginPage.LoginPage(self.driver, self.url, u"网易")
		login_page.open()
		#调用用户名输入组件
		login_page.input_username("auto_tester")
		login_page.input_password("123qwe")
		#login_page.saveScreenshot(self.driver, "login")
		login_page.click_submit()
	#用例执行体
	def test_createContact(self):
		#进入邮箱页面
		managercontact = ContactsPage.ContactManager(self.driver, self.url, u"网易")
		#点击通讯录菜单
		managercontact.click_Contactmenu()
		#点击新建联系人按钮
		managercontact.click_Newcontact()
		time.sleep(3)
		#print self.driver.find_elements_by_tag_name("input")[0]
		#输入联系人姓名
		managercontact.intput_contactname("tsbc1")
		#输入联系人邮箱
		managercontact.intput_contactmail("tsbc1@vip.com")
		#输入联系人电话
		managercontact.intput_contactphone("13800138000")
		managercontact.saveScreenshot(self.driver, "mgtcontact")
		#点击确定提交
		managercontact.click_Submitbtn()

	def tearDown(self):
		time.sleep(5)
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()