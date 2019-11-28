# coding=utf-8

# 目的: 参数化, pytest list

# 1. 验证文件是否存在,存在读取,不存在错报
# 2. 读取sheet方式, 名称,索引
# 3. 读取sheet内容
    # 返回list, 字典
    # 格式: [{'a':"a1",'b':" b1"}, {'a':"a2",'b':"b2"}]
# 4. 结果返回

import os
import xlrd


# 自定义异常
class  SheetTypeError(object):
    pass

class ExcelReader():
    def __init__(self, excel_file, sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self.data_list = []
        else:
            raise FileNotFoundError("文件不存在")

    def data(self):
        if self.data_list:
            return self.data_list

        workbook = xlrd.open_workbook(self.excel_file)

        if type(self.sheet_by) not in [str,int]:
            raise SheetTypeError("参数错误")
        elif type(self.sheet_by) == int:
            sheet = workbook.sheet_by_index(self.sheet_by)
        elif type(self.sheet_by) == str:
            sheet = workbook.sheet_by_name(self.sheet_by)

        # 获取首行信息
        title = sheet.row_values(0)
        for r in range(1, sheet.nrows):
            self.data_list.append(dict(zip(title,sheet.row_values(r))))
        # print(self.data_list)
        return self.data_list

if __name__ == "__main__":
    excel_reader = ExcelReader('../data/testdata.xlsx',"美多商城接口测试")
    print(excel_reader.data())
