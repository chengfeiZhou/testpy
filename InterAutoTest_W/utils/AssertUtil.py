# coding=utf-8
"""
1. 定义封装类;
2. 初始化数据,日志
3. code相等
4. body相等
5.body包含
"""
import sys
sys.path.append('../')
import json
from utils.LogUtil import my_log

class AssertUtil():

    def __init__(self):
        self.log = my_log('AssertUtil')

    def assert_code(self, code, expected_code):
        """
        验证返回状态码
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except Exception as e:
            self.log.error(f'code error, code is {code}, expected_code is {expected_code}')
            raise
    
    def assert_body(self, body, expected_body):
        """
        验证返回结果内容相等
        """
        try:
            assert body == expected_body
            return True
        except Exception as e:
            self.log.error(f'body error, body is {body}, expected_body is {expected_body}')
            raise

    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含期望的结果
        """
        try:
            body = json.dumps(body)
            assert expected_body in body
            return True
        except Exception as e:
            self.log.error(f'body error, body not in expected_body, body is {body}, expected_body is {expected_body}')
            raise