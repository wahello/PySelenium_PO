#-*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
__author__ = 'tsbc'

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd.sheet
import time, os

class Action(object):
	"""
	BasePage封装所有页面都公用的方法，例如driver, url
	"""
	driver = None
	#初始化driver、url、等
	def __init__(self, driver, base_url, pagetitle):
		self.base_url = base_url
		self.pagetitle = pagetitle
		self.driver = driver
		"""
		通过传参选择启动浏览器
		# self.browser = "Firefox" #传入浏览器对象
		# if Action.driver == None:
		# 	if self.browser.upper() == 'IE': Action.driver = webdriver.Ie()
		# 	elif self.browser.upper() == 'CHROME': Action.driver = webdriver.Chrome()
		# 	elif self.browser.upper() == 'FIREFOX': Action.driver = webdriver.Firefox()
		# 	elif self.browser.upper() == 'SAFARI': Action.driver = webdriver.Safari()
		# 	else: Action.driver = webdriver.Ie()
		# 	Action.driver.maximize_window()
		# #pass
		# 	#print u"加载浏览器驱动失败!"
		# self.driver = Action.driver
		self.verificationErrors = []
		"""
	#打开页面，校验页面链接是否加载正确
	def _open(self, url, pagetitle):
		#使用get打开访问链接地址
		self.driver.get(url)
		self.driver.maximize_window()
		#使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
		assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

	#重写元素定位方法
	def find_element(self, *loc):
		#return self.driver.find_element(*loc)
		try:
			WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print u"%s 页面中未能找到 %s 元素" % (self, loc)

	#重写一组元素定位方法
	def find_elements(self, *loc):
		#return self.driver.find_element(*loc)
		try:
			if len(self.driver.find_elements(*loc)):
				return self.driver.find_elements(*loc)
		except:
			print u"%s 页面中未能找到 %s 元素" % (self, loc)

	#重写switch_frame方法
	def switch_frame(self, loc):
		return self.driver.switch_to_frame(loc)
	#定义open方法，调用_open()进行打开链接

	def open(self):
		self._open(self.base_url, self.pagetitle)

	#使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
	def on_page(self, pagetitle):
		return pagetitle in self.driver.title

	#定义script方法，用于执行js脚本，范围执行结果
	def script(self, src):
		self.driver.execute_script(src)

	#重写定义send_keys方法
	def send_keys(self, loc, vaule, clear_first=True, click_first=True):
		try:
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
			self.find_element(*loc).send_keys(vaule)
		except AttributeError:
			print u"%s 页面中未能找到 %s 元素" % (self, loc)

	#读取excel文件的table
	@staticmethod
	def readtable(filepath, sheetno):
		"""
		filepath:文件路径
		sheetno：Sheet编号
		"""
		data = xlrd.open_workbook(filepath)
		#通过索引顺序获取Excel表
		table = data.sheets()[sheetno]
		return table

	#读取xls表格，使用生成器yield进行按行存储
	@staticmethod
	def readxls(filepath, sheetno):
		"""
		filepath:文件路径
		sheetno：Sheet编号
		"""
		table = Action.readtable(filepath, sheetno)
		for args in range(1, table.nrows):
			#使用生成器 yield
			yield table.row_values(args)

	#读取元素标签和元素唯一标识
	@staticmethod
	def locate(index, filepath="../data/case_data.xls", sheetno=0):
		"""
		filepath: 文件路径
		sheetno：Sheet编号
		index: 元素编号
		返回值内容为：("id","inputid")、("xpath","/html/body/header/div[1]/nav")格式
		"""
		table = Action.readtable(filepath, sheetno)
		for i in range(1, table.nrows):
			if index in table.row_values(i):
				return table.row_values(i)[1:3]

	#savePngName:生成图片的名称
	def savePngName(self, name):
		"""
		name：自定义图片的名称
		"""
		day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
		fp = "../result/" + day + "/image"
		tm = self.saveTime()
		type = ".png"
		if os.path.exists(fp):
			filename = str(fp)+"/" + str(tm)+str("_")+str(name)+str(type)
			print filename
			return filename
		else:
			os.makedirs(fp)
			filename = str(fp)+ "/" + str(tm)+str("_")+str(name)+str(type)
			print filename
			return filename

	#获取系统当前时间
	def saveTime(self):
		"""
		返回当前系统时间以括号中（2014-08-29-15_21_55）展示
		"""
		return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

	#saveScreenshot:通过图片名称，进行截图保存
	def saveScreenshot(self, driver, name):
		"""
		快照截图
		name:图片名称
		"""
		#获取当前路径
		#print os.getcwd()
		image = driver.save_screenshot(self.savePngName(name))
		return image