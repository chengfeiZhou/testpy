# coding=utf-8
"""
1. 创建yaml文件
2. 读取yaml文件
3. 输出yaml文件
"""
import yaml

with open('./data.yml', 'r') as f:
    r = yaml.safe_load(f)

print(r)





