import xlrd
from xlutils.copy import copy
rb = xlrd.open_workbook('test.xlsx')
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(0,7,'本地路径')		#坐标从0,0开始
for i in range(len(a[1]) - 3):
	ws.write(1 + i, 7, str(a[0] + '\\' + a[1][i]))
wb.save('final.xls')

