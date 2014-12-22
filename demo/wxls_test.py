#coding:utf-8

import xlwt

a = [1,8,3,4,7,9]
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet', cell_overwrite_ok=True)
j = 0
for i in a:
	worksheet.write(j, 0, label = i)
	j = j + 1 
workbook.save('Excel_Workbook.xls')