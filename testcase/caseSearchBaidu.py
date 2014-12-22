# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from public import saveScreenshot

class Demo(unittest.TestCase):
	"""百度首页搜索测试用例"""
	#脚本初始化
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.baidu.com"
		#self.js_ = 'document.getElementsByClassName("fore2")[6].getElementsByTagName("a")[2].click();'
		#self.loadstate = 'return document.readyState == "complete"'
	#测试用例
	def test_Demo(self):
		"""
		测试Demo
		"""
		driver = self.driver
		print u"========【case_0001】 测试Demo============="
		driver.get(self.base_url + "/")
		driver.maximize_window()
		driver.find_element_by_id("kw").clear()
		driver.find_element_by_id("kw").send_keys("Selenium")
		time.sleep(3)
		saveScreenshot.saveScreenshot(self.driver, "search")
		driver.find_element_by_id("su").click()
		time.sleep(3)
	
	#脚本退出
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

