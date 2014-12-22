#-*- coding: utf-8 -*-
__author__ = 'tsbc'

import BasePage
from selenium.webdriver.common.by import By
import xlrd
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
#继承BasePage类
class LoginPage(BasePage.Action):
	"""
	LoginPage 对象库组件
	"""
	fpath = "..\\data\\case_data.xls"
	#定位器，通过元素属性定位元素对象
	# username_loc = (By.ID, "idInput")
	# password_loc = (By.ID, "pwdInput")
	# submit_loc = (By.ID, "loginBtn")
	# span_loc = (By.CSS_SELECTOR, "div.error-tt>p")
	# dynpw_loc = (By.ID, "lbDynPw")
	# userid_loc = (By.ID, "spnUid")
	loc = BasePage.Action
	username_loc = loc.locate("ele_0001")
	password_loc = loc.locate("ele_0002")
	submit_loc = loc.locate("ele_0003")
	span_loc = loc.locate("ele_0004")
	dynpw_loc = loc.locate("ele_0005")
	userid_loc = loc.locate("ele_0006")

	#Action
	def open(self):
		#调用page中的_open打开连接
		self._open(self.base_url, self.pagetitle)

	#调用send_keys，输入用户名
	def input_username(self, username):
		#print self.username_loc
		self.send_keys(self.username_loc, username)
	#调用send_keys，输入密码
	def input_password(self, password):
		self.send_keys(self.password_loc, password)

	#调用click，点击登录
	def click_submit(self):
		self.find_element(*self.submit_loc).click()

	#用户名或密码不合理是Tip框内容展示
	def show_span(self):
		return self.find_element(*self.span_loc).text

	#切换登录模式为动态密码登录（IE下有效）
	def swich_DynPw(self):
		self.find_element(*self.dynpw_loc).click()

	#登录成功页面中的用户ID查找
	def show_userid(self):
		return self.find_element(*self.userid_loc).text

	#获取Excel中Sheet表格对象
	@staticmethod
	def casedata(filepath, sheetno):
		return LoginPage.readxls(filepath, sheetno)