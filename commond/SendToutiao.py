# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import sys
import Encryption
import Getnews
reload(sys)
sys.setdefaultencoding('utf-8')

class Sendweibo(unittest.TestCase):
	"""新闻捕捉"""
	#脚本初始化
	def setUp(self):
		print "staring"
		self.driver = webdriver.PhantomJS()
		self.driver.implicitly_wait(30)
		self.ennum = Encryption.Encryption()
		self.news = Getnews.News()
	#测试用例
	def test_send_news(self):
		"""
		测试Demo
		"""
		self.toutiao_url = "http://toutiao.com"
		self.huati_url = "http://www.qq.com"
		self.weibo_url = "http://d.weibo.com"
		self.username = "tsbc@qq.com"
		self.password = self.ennum.decryption(458680)
		driver = self.driver

		#获取头条新闻事件内容
		event = self.news.get_toutiao(driver,self.toutiao_url)

		#获取今日话题新闻事件内容
		#event_ = self.news.get_huati(driver, self.huati_url)
		
		#登录微博准备发布
		print u"进行登录新浪微博！"
		self.news.loginweibo(driver, self.username, self.password, self.weibo_url, event)

	#脚本退出
	def tearDown(self):
		print "finshed"
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
