# coding=utf-8
"""
1. 创建类和测试方法
2. 创建数据
3. 创建参数化
4.运行
"""
import pytest

class TestClass():
    data_list = ['xiaoming', 'xiaohong']

    @pytest.mark.parametrize('name',data_list)
    def test_a(self, name):
        print('test_a')
        print(name)
        assert 1


if __name__ == "__main__":
    pytest.main(['-s','pytest_one.py'])
