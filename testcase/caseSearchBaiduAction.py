#-*- coding: utf-8 -*-
__author__ = 'tsbc'

import unittest
import xlrd
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from test import test_support
from public import saveScreenshot


class CaseSearchbaidu(unittest.TestCase):
	"""百度搜索用例"""
		#加载浏览器驱动
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.url = "http://www.baidu.com/"
	# def setUp(self):
	# 	pass
	# def tearDown(self):
	# 	pass

	def action(self, case_id, search_summary):
			self.driver.get(self.url)
			self.assertIn('百度', self.driver.title, "打开页面失败！")
			#最大化浏览器
			self.driver.maximize_window()
			#调用封装的登录方法进行登录
			print u"========【" + case_id + u"】搜索：" + search_summary + u"============="
			print search_summary
			self.driver.find_element_by_id("kw").clear()
			self.driver.find_element_by_id("kw").send_keys(search_summary)
			self.driver.find_element_by_id("su").click()
			time.sleep(1)
			saveScreenshot.saveScreenshot(self.driver, "search")
			print self.driver.title

	@staticmethod
	def getTestFunc(case_id, search_summary):
		def func(self):
			#执行acation 真正测试用例的执行方法
			self.action(case_id, search_summary)
		return func

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

def __generateTestCases():
	data = xlrd.open_workbook(u"../data/SearchBaidu.xls")
	#通过索引顺序获取Excel数据
	table = data.sheets()[0]
	#通过for循环生产多个 test_login_ 函数
	for args in range(1, 4):
		txt = table.row_values(args)
		#生成test_login函数后，调用 getTestFunc 进行传参
		setattr(CaseSearchbaidu, 'test_searchebaidu_%s' % txt[0], CaseSearchbaidu.getTestFunc(*txt))
__generateTestCases()

def test_main():
	test_support.run_unittest(CaseSearchbaidu)
