# coding=utf-8
import sys

sys.path.append('../')
import pytest
import requests
from utils.RequestsUtil import Request, r_get,r_post
from common.Base import init_db

request = Request(url='http://211.103.136.242:8064')

def test_login():
    """
    登录
    """
    conn = init_db('db_1')
    res_db = conn.fetch_one('select id from tb_user where username="python"')
    print(f"数据库查询数据:{res_db}")

    url = 'http://211.103.136.242:8064/authorizations/'
    data = {'username':'python', 'password':'12345678'}

    r = r_post(url, json=data)
    print(r)
    '''
    {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1NzM1NzE3ODAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.CDnyS9thrPFk40Z7PX4vbBTJnzQT582xlsaFZbkRnMs', 
        'username': 'python', 
        'user_id': 1
    }
    '''

def info():
    url = 'http://211.103.136.242:8064/user/'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1NzM1NzE3ODAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.CDnyS9thrPFk40Z7PX4vbBTJnzQT582xlsaFZbkRnMs'
    headers = {
        'Authorization':'JWT ' + token
    }

    r = r_get(url, headers=headers)

    print(r)

def goods_list():
    url = 'http://211.103.136.242:8064/categories/115/skus/'
    data = {
        'page':"1",
        'page_size':"10",
        'ordering':"create_time"
    }

    r = r_get(url,json=data)
    print(r)

def cart():
    url = 'http://211.103.136.242:8064/cart/'
    data = {
        'sku_id':"3",
        'count':"1",
        'selected':True
    }
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1NzM1NzE3ODAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.CDnyS9thrPFk40Z7PX4vbBTJnzQT582xlsaFZbkRnMs'
    headers = {
        'Authorization':'JWT ' + token
    }

    r = r_post(url, json=data, headers=headers)

    print(r)


def order():
    url = 'http://211.103.136.242:8064/orders/'
    data = {
        'address':"1",
        'pay_method':"1"
    }
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1NzM1NzE3ODAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.CDnyS9thrPFk40Z7PX4vbBTJnzQT582xlsaFZbkRnMs'
    headers = {
        'Authorization':'JWT ' + token
    }
    r = r_post(url, json=data, headers=headers)

    print(r)

if __name__ == "__main__":
    # login()
    # info()
    # goods_list()
    # cart()
    # order()
    pytest.main(['-s'])

    


"""
1. 根据默认运行原则,调整py文件命名,函数命名
2. pytest.main()运行,或者命令行直接运行
"""


