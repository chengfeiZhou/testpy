# coding=utf-8

import pytest
import allure

@allure.feature('接口测试, 这是一个一级标签')
class TestAllure():
    # 定义测试方法
    @allure.title('测试用例标题1')
    @allure.description('执行测试用例1的结果是:test_1')
    @allure.stroy("这是一个二级标签:test1")
    @allure.severity(allure.severity.CRITICAL)
    def test_1(self):
        print("test_1")

    @allure.title('测试用例标题2')
    @allure.description('执行测试用例2的结果是:test_2')
    @allure.stroy("这是一个二级标签:test1")
    @allure.severity(allure.severity.BLOCKER)
    def test_2(self):
        print("test_2")

    @allure.title('测试用例标题3')
    @allure.description('执行测试用例3的结果是:test_3')
    @allure.stroy("这是一个二级标签:test3")
    def test_3(self):
        print("test_3")

    @pytest.mark.parametrize("case",['case1', 'case2', 'case3'])
    def test_4(self, case):
        print(f"test4: {case}")
        allure.dynamic.title(case)


if __name__ == "__main__":
    pytest.main(['allure_demo.py'])

