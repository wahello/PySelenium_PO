# -*- coding:utf-8 -*-
__author__ = 'Ray'

from selenium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
	"""
	this is My Test!
	"""
	def setUp(self):
		self.driver = webdriver.PhantomJS()

	def tearDown(self):
		self.driver.quit()

	def test_something(self):
		self.driver.get("http://mail.126.com")
		# css = self.driver.find_elements_by_css_selector("input")	#查找所有使用 input 标签的元素
		# css = self.driver.find_elements_by_css_selector("#username")	#id选择器，所有id属性等于username的元素
		# css = self.driver.find_elements_by_css_selector(".btn")	#class 选择器，所有class属性中包含 btn的元素
		# css = self.driver.find_elements_by_css_selector("input , span")	#查找所有使用 input 或者 span标签的元素
		# css = self.driver.find_elements_by_css_selector("form  div#idInputLine input")	#form元素之后中 div的id是idInputLine的元素 之后的所有input元素
		# css = self.driver.find_elements_by_css_selector("form[name='login126'] > input") #查找form元素下的所有标签是input的子元素
		# css = self.driver.find_elements_by_css_selector("input[name='username'] ~ input") #查找input之后的所有同级input标签元素
		# css = self.driver.find_elements_by_css_selector("label[class='placeholder']")  #使用元素标签的属性进行定位
		# css = self.driver.find_elements_by_css_selector("label[class^='plac']")	#查找标签属性以‘plac’开头的元素
		# css = self.driver.find_elements_by_css_selector("label[class$='lder']")	#查找标签属性以‘lder’结尾的元素
		#css = self.driver.find_elements_by_css_selector("label[class*='acehol']")	#查找标签属性包含‘acehol’的元素
		# css = self.driver.find_elements_by_css_selector("label[for='idInput'][class*='acehol']")  #使用两个标签属性
		css = self.driver.find_elements_by_css_selector("div > span:contains('126')")

		for i  in css:
			print i.get_attribute("id")

		self.assertEqual(True, True)


if __name__ == '__main__':
	unittest.main()
