import xlrd

rb = xlrd.open_workbook(r"C:\Users\24299\Desktop\test.xlsx")
x = rb.sheet_by_index(0)
# 打印行数和列数
print(x.nrows)
print(x.ncols)
# 读取第一行、第一列内容
print(x.row_values(0))
print(x.col_values(0))

