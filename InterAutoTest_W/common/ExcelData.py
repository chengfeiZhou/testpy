# coding=utf-8

# 1. 使用excel工具类, 获取结果list
# 2. 列"是否运行内容", y
# 3. 保存要执行结果, 放到新的列表中
import sys
sys.path.append('../')
from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig

class Data():
    def __init__(self, excel_file, sheet_by):
        self.reader = ExcelReader(excel_file, sheet_by)
        self.run_list = []

    def get_run_data(self):
        """
        根据"是否运行"列,获取执行测试用例
        """
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == 'y':
                self.run_list.append(line)
        return self.run_list