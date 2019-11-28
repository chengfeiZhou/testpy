# coding=utf-8

# 1. 获取测试用例的列表
    # 获取testlogin.yml文件路径
    # 使用工具类来读取多个文档的内容
# 2. 参数化执行测试用例

import os
import sys
sys.path.append("../")
import pytest
from config import Conf
from config.Conf import ConfigYaml
from utils.YamlUtil import YamlReader
from utils.RequestsUtil import Request

test_file = os.path.join(Conf.get_data_path(), 'testlogin.yml')
print(test_file)

data_list = YamlReader(test_file).data_all()
print(data_list)

@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    """
    执行测试用例
    """
    uri = login['url']
    print(uri)
    data = login['data']
    print(data)
    request = Request(ConfigYaml().get_config_url())
    res = request.post(uri, json=data)
    print(res)


if __name__ == "__main__":
    pytest.main(['test_login.py'])
