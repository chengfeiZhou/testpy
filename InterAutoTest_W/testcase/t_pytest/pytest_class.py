#coding=utf-8

"""
1.定义类;
2.创建测试方法test开头
3.创建setup_class, teardown_class
4.运行查看结果
"""
import pytest

class TestClass():
    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def setup_class(self):
        print('------setup_class------')

    def teardown_class(self):
        print('------teardown_class------')
   
if __name__ == "__main__":
    pytest.main(['-s', 'pytest_class.py'])