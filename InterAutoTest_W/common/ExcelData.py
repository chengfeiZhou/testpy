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

    def get_run_data(self):
        """
        根据"是否运行"列,获取执行测试用例
        """
        run_list = []
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == 'y':
                run_list.append(line)
        return run_list

    def get_case_list(self):
        """
        获取全部的测试用例
        """
        run_list = [line for line in self.reader.data()]
        return run_list

    def get_case_pre(self, pre):
        """
        根据前置条件,从全部测试用例中返回前置用例
        """
        # 获取前部测试用例
        # 判断需前置执行的用例
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None





