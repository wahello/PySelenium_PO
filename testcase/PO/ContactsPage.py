#-*- coding: utf-8 -*-
__author__ = 'tsbc'

from selenium.webdriver.common.by import By
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import BasePage

#继承BasePage类
class ContactManager(BasePage.Action):

	#定位器，通过元素属性定位元素对象
	contactmenu = (By.ID, "_mail_tabitem_1_37")
	#newcontatct = (By.CSS_SELECTOR, "[id^=_mail_button]")
	newcontatct = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div")
	name_loc = (By.XPATH, "/html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/dl[1]/dd/div/input")
	mail_loc = (By.XPATH, "/html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/div[1]/dl/dd/div/input")
	phoneno_loc = (By.XPATH, "/html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/div[2]/dl/dd/div/input")
	subbtn_loc = (By.XPATH, "/html/body/div[9]/div[3]/div[2]/div[1]")
	testclass = (By.TAG_NAME, "input")

	#Action
	#点击通讯录菜单
	def click_Contactmenu(self):
		self.find_element(*self.contactmenu).click()

	#点击新建联系人按钮
	def click_Newcontact(self):
		self.find_element(*self.newcontatct).click()
		#return self.find_element(*self.newcontatct)

	#调用send_keys对象，输入联系人姓名
	def intput_contactname(self, contactname):
		self.find_element(*self.name_loc).send_keys(contactname)

	#调用send_keys对象，输入联系人email地址
	def intput_contactmail(self, email):
		self.find_element(*self.mail_loc).send_keys(email)

	#调用send_keys对象，输入联系人联系电话
	def intput_contactphone(self, phoneno):
		self.find_element(*self.phoneno_loc).send_keys(phoneno)

	#点击新增联系人确定提交按钮
	def click_Submitbtn(self):
		self.find_element(*self.subbtn_loc).click()

	def re_class(self):
		return self.find_elements(*self.testclass)