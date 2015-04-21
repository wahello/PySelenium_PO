# -*- coding:utf-8 -*-
__author__ = 'Ray'

import sys
import time
import Encryption
reload(sys)
sys.setdefaultencoding('utf-8')

class News:

    def get_toutiao(self, driver, url):
        """获取进入头条页面中的前6个标题"""
        self.driver = driver
		self.base_url = url
		self.ennum = Encryption.Encryption()
		driver.get(self.base_url + "/")
		driver.maximize_window()
		title = u"#今日头条#"

		event = ""
		event += title
		driver.find_element_by_xpath("//a[@ga_event='feed_refresh']").click()
		menulink = driver.find_elements_by_xpath("//ul[@data-node='listBox']/li[position()<7]//a[@ga_event='feed_title']")
		for i in menulink:
			event += i.text + " "
		print event
		return event

	def get_huati(self, driver, url):
        """获取腾讯新闻今日话题中的标题"""
		self.driver = driver
		self.base_url = url
		self.ennum = Encryption.Encryption()
		driver.get(self.base_url + "/")
		driver.maximize_window()
		title = u"#今日话题#"

		event = ""
		event += title

		div_src = driver.find_element_by_id("today")
		toptitle = driver.find_element_by_id("todaytop")
		event += toptitle.text

		menulink = div_src.find_elements_by_xpath("//div[@id='today']//li/a[1]")
		for i in menulink:
			event += i.text+"  "
		print event

	def loginweibo(self, driver, username, password, url, event):
        """登录新浪微博，并发布微博event事件"""
		driver.get(url+"/")
		time.sleep(5)
		print u"准备发布内容请稍候..."

		driver.find_element_by_xpath("//input[@node-type='username']").send_keys(username)
		#print u"输入用户名"
		driver.find_element_by_xpath("//input[@node-type='password']").send_keys(password)
		#print u"输入密码"
		driver.find_element_by_xpath("//div[@node-type='normal_form']//a[@node-type='submitBtn']").click()
		#print u"点击登录"
		time.sleep(5)
		driver.find_element_by_xpath("//a[@node-type='publish']").click()
		time.sleep(1)
		#print u"点击编辑框图标"
		driver.find_element_by_xpath("//textarea[@node-type='textEl']").send_keys(event)
		print u"填写发送内容"
		#print driver.page_source
		driver.find_element_by_xpath("//a[@node-type='submit']").click()
		print u"进行发布微博"
		time.sleep(0.5)