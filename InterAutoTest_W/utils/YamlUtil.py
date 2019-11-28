# coding=utf-8

# 1. 创建类
# 2. 初始化,文件是否存在
# 3. yaml读取

import os
import yaml

class YamlReader():
    def __init__(self, yaml_p):
        if os.path.exists(yaml_p):
             self.yaml_p = yaml_p
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None

    def data(self):
        # 读取单个文档
        if not self._data:
            with open(self.yaml_p, 'r') as f:
                self._data = yaml.safe_load(f)
        return self._data

    def data_all(self):
        # 读取单个文档
        if not self._data:
            with open(self.yaml_p, 'r') as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all


        