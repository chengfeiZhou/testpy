# coding=utf-8

# 1. 初始化信息
    # 1) 初始化测试用例文件
    # 2) 测试用例sheet名称
    # 3) 获取运行测试用例列表
    # 4) 日志
# 2. 测试用例方法,参数化运行

import os
import sys
sys.path.append('../')
import pytest
import json
from config.Conf import ConfigYaml
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from common import Base
from utils.RequestsUtil import Request

case_file = os.path.join('../data', ConfigYaml().get_excel_file())
sheet_name = ConfigYaml().get_excel_sheet()
data_init = Data(case_file, sheet_name)
run_list = data_init.get_run_data()

log = my_log()

# 初始化dataconfig
data_key = ExcelConfig.DataConfig

# 一个用例运行
# 1)初始化信息, url, data
# 2) 接口请求
class TestExcel():
    # 1. 增加pytest
    # 2. 修改方法参数
    # 3. 重构函数内容
    # 4. pytest.main

    def run_pre(self, pre_case):
        url = pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]

        # 增加headers
        header = Base.json_parse(headers)
        # 增加cookies
        cookie = Base.json_parse(cookies)
        res = self.run_api(url, params, method, header, cookie)
        print(res)
        
    
    def run_api(self,url, params, method ='get', header=None, cookie=None):
        """
        发送请求
        """
        request = Request(ConfigYaml().get_config_url())
        if not len(str(params).strip()):
            return
        params = json.loads(params)
        if str(method).lower() == "get":
            res = request.get(url,json=params,headers=header,cookies=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=params,headers=header,cookies=cookie)
        else:
            log.error(f"错误的请求方法:{method}")
        return res


    @pytest.mark.parametrize('case', run_list)
    def test_run(self,case):
        # data_key = ExcelConfig.DataConfig
        url = case[data_key.url]
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        beizhu = case[data_key.beizhu]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]

        if pre_exec:
            # 前置用例
            pre_case = data_init.get_case_pre(pre_exec)
            print(f"前置条件信息为:{pre_case}")
            self.run_pre(pre_case)

        # 增加headers
        header = Base.json_parse(headers)
        # 增加cookies
        cookie = Base.json_parse(cookies)
        request = Request(ConfigYaml().get_config_url())
        # params转义json
        # 验证params有没有内容
        res = self.run_api(url, params, method, header, cookie)
        print(res)


if __name__ == "__main__":
    pytest.main(['-s', 'test_excel_case.py'])
    # TestExcel().test_run()

    





