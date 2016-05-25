# -*- coding:utf-8 -*-
__author__ = 'Ray'

from selenium import webdriver
from test import test_support
import unittest
import logging
import xlrd,xlsxwriter


class WxlsDemo(unittest.TestCase):
	"""
	Excel文件写入demo
	针对不同结果写入不同的数据
	"""
	@classmethod
	def setUpClass(cls):
		print "starting"
		logging.basicConfig(level=logging.DEBUG,
							format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
							datefmt='%a, %d %b %Y %H:%M:%S',
							filename='myapp.log',
							filemode='w')
				#xlsxwriter写入excel表格数据
		cls.book = xlsxwriter.Workbook(r'wxlsdemo.xls')
		cls.sheet = cls.book.add_worksheet()
	@classmethod
	def tearDownClass(cls):
		cls.book.close()
		print "finishing"

	def action(self, i, *txt):

		username = txt[2]
		password = txt[4]

		self.sheet.set_column(0,5,20)
		self.sheet.set_row(0,25)
		"""
		border：边框
		align:对齐方式
		bg_color：背景颜色
		font_size：字体大小
		bold：字体加粗
		font_name:字体
		font_color:字体颜色
		"""
		#标题字体格式
		top = self.book.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':13,'bold':True})
		#成功
		green = self.book.add_format({'border':1,'align':'center','bg_color':'green','font_size':12,"font_color":"yellow"})
		#失败
		red = self.book.add_format({'border':2,'align':'center','bg_color':'red','font_size':12,"font_color":"yellow"})
		#奇数行字体格式
		odd = self.book.add_format({'border':3,'font_name':u'微软雅黑','bg_color':'C2DDF8'})
		#偶数行字体格式
		even  = self.book.add_format({'border':3,'font_name':u'微软雅黑','bg_color':'D6EAF1'})

		if i == 0:	#第0行是标题
			self.sheet.write_row(0,0,txt,top)#重写标题整行数据
			return
		#重新写入当前的 *txt 数据，根据奇偶行分别用不同的背景色
		elif (i+1)%2 == 0:#奇数
			self.sheet.write_row(i,0,txt,odd) #写入奇数行数据
			#成功或者失败，在最后一列填写结果
			if txt[2] == "auto_tester05" or txt[2] == "auto_tester08":
				print txt
				print u"失败"
				self.sheet.write(i,len(txt)-1,u"失败",red)#在当前行，最后一列写入
			else:
				print txt
				print u"成功"
				self.sheet.write(i,len(txt)-1,u"成功",green)
		else:#偶数
			self.sheet.write_row(i,0,txt,even) #写入偶数行数据
			#成功或者失败，在最后一列填写结果
			if txt[2] == "auto_tester05" or txt[2] == "auto_tester08":
				print txt
				print u"失败"
				self.sheet.write(i,len(txt)-1,u"失败",red)
			else:
				print txt
				print u"成功"
				self.sheet.write(i,len(txt)-1,u"成功",green)

	@staticmethod
	def getTestFunc(i, *txt):
		def func(self):
			self.action(i, *txt)
		return func

def __generateTestCases():

	#xlrd读取excel表格数据
	data = xlrd.open_workbook("wxlsdemo.xls")
	table = data.sheet_by_index(0)
	nrows = table.nrows
	for i in xrange(nrows):
			txt = table.row_values(i)
			setattr(WxlsDemo, 'test_wxls_%s' % (txt[0]), WxlsDemo.getTestFunc(i, *txt))

__generateTestCases()

if __name__ == "__main__":
	test_support.run_unittest(WxlsDemo)