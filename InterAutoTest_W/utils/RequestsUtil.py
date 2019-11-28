# coding=utf-8

# 1.创建封装方法
# 2.发送requests请求
# 3.获取结果相应内容
# 4.内容存储到字典
# 5.字典返回

import requests
from config.Conf import ConfigYaml

def r_get(url, json=None, headers=None):
    r = requests.get(url,json=json, headers=headers)

    code = r.status_code
    try:
        body = r.json()
    except:
        body = r.text
    
    res = {
        'code':code,
        'body':body
    }

    return res


def r_post(url, json=None, headers=None):
    r = requests.post(url,json=json, headers=headers)

    code = r.status_code
    try:
        body = r.json()
    except:
        body = r.text
    
    res = {
        'code':code,
        'body':body
    }

    return res

# 重构
class Request():
    def __init__(self,url=ConfigYaml().get_config_url() ):
        self.url = url

    # 定义公共方法:
    def request_api(self, uri, method='get', data=None,json=None, headers=None):
        if method == 'get':
            r = requests.get(self.url+uri, data=data, json=json, headers=headers)
        elif method == 'post':
            r = requests.post(self.url+uri, data=data, json=json, headers=headers)
        
        code = r.status_code
        try:
            body = r.json()
        except:
            body = r.text
        res = {
            'code':code,
            'body':body
        }
        return res

    # 重构get方法
    def get(self, url,**kwargs):
        return self.request_api(url,**kwargs)

    def post(self, url,**kwargs):
        return self.request_api(url,method='post',**kwargs)
        



