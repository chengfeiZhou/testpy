#coding=utf-8

# 1. 创建简单的测试方法
# 2. pytest运行
    # 2.1 idea中直接执行
    # 2.2 命令行执行
import pytest

# 创建普通的方法
def func(x):
    return x+1


# 创建pytest断言的方法
def test_a():
    print("---test_a---")
    assert func(3) == 5 # 断言失败

# 使用装饰器,控制单个测试用例的运行情况
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_b():
    print('---test_b---')
    assert func(3) == 4 # 断言成功

# 代码直接执行
if __name__ == "__main__":
    pytest.main(["pytest_demo.py"])


# 命令行执行:
# pytest pytest_demo.py
