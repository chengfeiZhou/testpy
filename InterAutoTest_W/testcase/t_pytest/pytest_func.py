#coding=utf-8

"""
1.定义类;
2.创建测试方法test开头
3.创建setup, teardown
4.运行查看结果
"""
import pytest

class TestFcun():
    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def setup(self):
        print('------setup------')

    def teardown(self):
        print('------teardown------')

if __name__ == "__main__":
    pytest.main(['-s', 'pytest_func.py'])

"""
PS E:\学习\测试\InterAutoTest_W\testcase\t_pytest> python pytest_func.py
=========================================================================== test session starts =========================================================================== 
platform win32 -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: E:\学习\测试\InterAutoTest_W, inifile: pytest.ini
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 2 items                                                                                                                                                           

pytest_func.py ------setup------
test_a
.------teardown------
------setup------
test_b
.------teardown------


======================================================================== 2 passed in 0.08 seconds ========================================================================= 


"""



