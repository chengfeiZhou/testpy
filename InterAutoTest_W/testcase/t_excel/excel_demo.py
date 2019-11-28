# coding=utf-8

"""
1. 导入包, xlrd(python自带)
2. 创建workbook对象
3. sheet对象
4. 获取行数和列数
5. 读取每行的内容
6. 读取每列的内容
7. 读取固定列的内容
"""
import xlrd
book = xlrd.open_workbook('./testdata.xlsx')
# 获取表的两种方式: 
# 索引
# sheet = book.sheet_by_index(0)
# 名称
sheet = book.sheet_by_name('美多商城接口测试')

rows = sheet.nrows  # 行数
cols = sheet.ncols  # 列数
print(f"rows:{rows}, cols:{cols}")

# 获取每行数据
for r in range(rows):
    r_values = sheet.row_values(r)
    print(r_values)

# 获取每列数据
for c in range(cols):
    c_values = sheet.col_values(c)
    print(c_values)

# 读取固定列的内容
v = sheet.cell(1,2)
print(v)