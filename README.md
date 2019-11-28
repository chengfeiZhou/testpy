[TOC]
# 自动化接口测试
# 第一章
## 一、项目相关：
### 1.项目信息：
#### 1.1 项目介绍：
- 项目名称: 美多商城
- 项目访问访问网站： http://211.103.136.242:8062/
### 2.接口信息：
#### 2.1 接口介绍:
- 登录；
- 个人信息；
- 获取商品信息；
- 购物车；
- 订单；

#### 2.2 登录接口文档:
- 后端接口设计:
    - 请求方式: POST /authorizations/
    - 请求参数:

|参数名|类型|说明|
|-|-|-|
|username|str|用户名|
|password|str|密码|

返回数据

|返回值|类型|说明 |
|-|-|-|
|username|str|用户名|
|user_id|int|用户id|
|token|str|身份认证|
#### 2.3 用户中心个人信息:
访问必须要求用户已通过认证(即登录之后)
认证:
```shell
headers:{
    'Authorization': 'JWT '+ this.token
}
```
- 后端接口设计:
    - 请求方法: GET /user/
    - 返回数据:

|返回值|类型|是否必须|说明|
|-|-|-|-|
|id|int|是|用户id|
|username|str|是|用户名|
|mobile|str|是|手机号|
|email|str|是|email邮箱|
|email_active|bool|是|邮箱是否通过验证|
#### 2.4 获取商品列表数据:
- 业务需求:
需要对商品数量进行分页支持,并且可以按照时间(默认)、价格、销量(人气)进行排序
- 后端接口设计:
    - 请求方法: GET   /categories/(?P<category_id>\d+)/skus>page=xxx&page_size=xxx&ordering=xxx
    - 请求参数:

|参数|类型|是否必须|说明|
|-|-|-|-|
|category_id|int|是|类别id(第三级类别)|
|page|int|是|页数|
|page_size|int|是|每页数量|
|ordering|str|是|排序关键字(create_time, price, sales)

返回数据:

|返回值|类型|是否必须|说明|
|-|-|-|-|
|id|int|是|商品sku编号|
|name|str|是|商品名称|
|price|decimal|是|单价|
|default_image_url|str|是|默认图片|
|comments|int|是|评论数量|

#### 2.5 添加到购物车:
- 后端接口:
    - 请求方法: POST /cart/
    - 请求参数:

|参数|类型|是否必须|说明|
|-|-|-|-|
|sku_id|int|是|商品sku_id|
|count|int|是|数量|
|selected|bool|否|是否勾选,默认勾选|

返回数据:

|参数|类型| 是否必须|说明|
|-|-|-|-|
|sku_id|int|是|商品sku_id|
|count|int|是|数量|
|selected|bool|否|是否勾选,默认勾选|

访问此接口, 无论用户是否登录,前端请求都需要带请求头Authorization, 由后端判断是否登录.

#### 2.6 保存订单:
- 后端接口设计:
    - 请求方式: POST  /orders/
    - 请求参数:

|参数|类型| 是否必须|说明|
|-|-|-|-|
|address|int|是|收货地址id|
|pat_method|int|是|支付方式|

返回数据:

|参数|类型| 是否必须|说明|
|-|-|-|-|
|order_id|char|是|订单编号|

## 二、接口测试框架：
### 1.介绍：
#### 1.1 框架对比:
- Unittest:
    - 不支持失败自动重新执行;
    - 参数化需依赖三方库;
    - HTMLTestRunner三方报告不够美观

- pytest:
    - 兼容unittest
    - 支持失败自动重新执行;
    - 参数化使用自带装饰器;
    - 兼容主流allure框架,报告美观功能强大;

### 2.流程：
#### 2.1 代码运行:
```flow
op1=>operation: 主程序运行(pytest框架)
op2=>operation: Excel用例(数据驱动)
op3=>operation: 配置文件(Yaml)
op4=>operation: Requests
op5=>operation: 断言(结果断言、数据库断言)
op6=>operation: 报告(Allure插件)
op7=>operation: 邮件

op1->op2->op3->op4->op5->op6->op7
```
#### 2.2 jenkins运行:
```flow
op1=>operation: Jenkins/Docker
op2=>operation: Job运行
op3=>operation: git
op4=>operation: Allure
op5=>operation: 邮件

op1->op2->op3->op4->op5
```
![代码测试结构](./image/代码测试结构.jpg)

# 第二章 接口自动化框架编写
## 一、项目及框架的搭建:
### 1.工具：
#### 1.1 python:
- 下载地址: https://www.python.org/download

#### 1.2 pycharm:
- 下载地址: https://www.jetbrains.com/pycharm

#### 1.3 git:
- 下载地址: https://git-scm.com/download

### 2.框架目录：
#### 2.1 创建目录:
```shell
InterAutoTest_W
```
![代码测试结构](./image/代码测试结构.jpg)
### 3.配置(pycharm)：
- 配置python环境:
```shell
Setting ->Project ->Project Interpreter
```
- 配置git:
```shell
Setting ->Version Control ->Git
```
- 配置github: 
```shell
Setting -> Version Control ->Github
```
- 建立远程仓库并提交代码: 
```shell
Vcs ->import into version control ->Share Project on Github
```
## 二、接口用例编写:
### 1.被测试的接口:
- 登录；
- 获取个人信息；
- 获取商品信息；
- 添加到购物车；
- 保存订单；

### 2. 使用excel编写测试用例:
#### 2.1 表结构:
- 用例ID;
- 模块;
- 接口名称;
- 请求URL;
- 前置条件;
- 请求类型;
- 请求参数类型
- 请求参数;
- 预期结果;
- 实际结果;
- 备注;

## 三、Requests使用:
### 1. 介绍及使用:
- 介绍:流行的接口http(s)请求工具, 功能强大,简单方便,容易上手;
- 官网: http://cn.python-requests.org/zh_CN/latest/

### 2. 用例代码编写:
```python
# coding=utf-8
import requests
r = requests.get('http://www.baidu.com')
print(r) # <Response [200]>
```
- 请求返回介绍:

|属性/方法|说明|
|-|-|
|r.status_code|响应状态码|
|r.content|字节方式的响应体,会自动解码gzip和deflate压缩|
|r.headers|以字典对象存储服务器响应头,若键不存在则返回None|
|r.json()|Requests中内置的JSON|
|r.url|获取url|
|r.encoding|编码格式|
|r.cookies|获取cookie|
|r.raw|获取原始响应体|
|r.text|字符串方式的响应体,会自动根据响应头部的字符编码进行编码|
|r.raise_for_status()|失败请求(非200响应)抛出异常|

### 3. 方法封装:  
- 1.创建封装方法
- 2.发送requests请求
- 3.获取结果相应内容
- 4.内容存储到字典
- 5.字典返回
utils/Request.py
```python
import requests

class Request():
    def __init__(self,url):
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
    def get(self, uri,**kwargs):
        return self.request_api(uri,**kwargs)

    def post(self, uri,**kwargs):
        return self.request_api(uri,method='post',**kwargs)   
```

## 四、配置文件:
使用YAML语言编写配置文件 
### 1. yaml的介绍与安装:
#### 1.1 Yaml介绍:
- yaml是一种所有编程语言可用的友好的数据序列化标准, 语法和其他高阶语言类似,并且可以简单表达字典、列表和其他基本数据类型的形态.
- yaml格式作为文件的配置格式:
    - yaml支持注释;
    - 不必强求逗号、括号等符号;
    - 通过缩进来区分,视觉上清晰
- yaml官网: https://yaml.org/

#### 1.2 Yaml安装:
```shell
pip install PyYaml
```
#### 1.3 快速体验:
- 字典:字典里的键值对用':'分隔;
data.yml
```yaml
name: "test_yaml"
result: "success"
```
```python
import yaml

with open('./data.yml', 'r') as f:
    r = yaml.safe_load(f)

print(r)
# {'name': 'test_yaml', 'result': 'success'}
```

### 2. 基本操作:
#### 2.1 字典:
- 字典里的键值对用':'分隔;
- 字典直接写key: value, 每个键值对占一行;
- key: 后要跟空格
#### 2.2 列表:
- 一组按序列排列的值(简称"序列或列表");
- 数组前加有"-"符号,符号与值之间需要用空格分隔;
```yaml
- 12
- 32
- 33
# [12, 32, 33]
``` 
#### 2.3 相互嵌套:
- 字典嵌套字典:
```yaml
person1:
  name: xiaoming
  age: 18
person2:
  name: xiaohong
  age: 16

# person1': {'name': 'xiaoming', 'age': 18}, 'person2': {'name': 'xiaohong', 'age': 16}}
```
- 字典嵌套列表:
```yaml
person:
  - "a"
  - "b"
  - c

# {'person': ['a', 'b', 'c']}
```

- 列表嵌套列表:
```yaml
- 
  - 1
  - 2
  - 3
- "b"
- c
- 
  - 6
  - 7
  - 8

# [[1, 2, 3], 'b', 'c', [6, 7, 8]]  
```
- 列表嵌套字典: 
```yaml
- 
  name: xiaoming
  age: 18
- 2
- 3
-
  name: xiaohong
  age: 16

#  [{'name': 'xiaoming', 'age': 18}, 2, 3, {'name': 'xiaohong', 'age': 16}]
```

### 3.读取文件:
#### 3.1 单个文件:
* 中文乱码: open指定encoding*

data.yml
```yaml
name: "test_yaml"
result: "success"
```
```python
import yaml

with open('./data.yml', 'r') as f:
    r = yaml.safe_load(f)

print(r)
# {'name': 'test_yaml', 'result': 'success'}
```

#### 3.2 多个文件:
data.yml
```yaml
---
name: "test_yaml"
result: "success"

---
# 用'---'分隔,说明是多个文档
"用户名称1": "test123"
"密码":"123456"
```
```python
import yaml

with open('./data.yml', 'r') as f:
    r = yaml.safe_load_all(f)
for i in r:
    print(r)
# {'name': 'test_yaml', 'result': 'success'}
# {"用户名称1": "test123","密码":"123456"}
```

### 4.配置文件设置:
- yaml封装:
./utils/YamlUtil.py
```python
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
```
- 配置文件conf.yaml
./config/conf.yml
```yaml
BASE:
  test:
    url: "http://211.103.136.242:8064"

```


./config/Conf.py
```python
# coding=utf-8
import os
from utils.YamlUtil import YamlReader
# 1. 获取项目基本目录
# 1.2 获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
print(current, BASE_DIR)
# 1.3 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"

def get_config_path():
    return _config_path
# 1.4 定义conf.yml的文件路径
_config_file = _config_path + os.sep + 'conf.yml'
def get_config_file():
    return _config_file

# 2. 读取配置文件
class ConfigYaml():
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

        # 获取需要的信息
        def get_config_url(self):
            return self.config['BASE']['test']['url']

if __name__ == "__main__":
    conf_read = ConfigYaml()
    print(conf_read)

```
- 基本目录配置:

- 配置文件读取及使用:

## 五、日志文件:
### 1.介绍:
#### 1.1 简介:
logging模块是python内置的标准模块,主要用于输出运行日志, 可以设置输出日志等级、日志保存路径等.

#### 1.2 快速使用:
log_demo.py
```python
# coding=utf-8
# 1.导入logging包
import logging
# 2.设置配置信息
logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")
# 3. 定义日志名称:get_logger
logger = logging.getLogger('log_demo')
# 4. info,debug
logger.info('info')
logger.debug('debug')
logger.warning('warning')

# 2019-11-20 23:06:09,957-log_demo-INFO-info
# 2019-11-20 23:06:09,958-log_demo-WARNING-warning

```

### 2.基本使用:
#### 2.1 日志输出到控制台或文件:
- 1. 设置logger名称
- 2. 设置log级别
- 3. 创建handler, 用于输出控制台或写入文件
- 4. 设置日志级别
- 5. 定义handler的输出格式
- 6. 添加handler
 
```python
# coding=utf-8
import logging

# 1. 设置logger名称
logger = logging.getLogger('log_file_demo')
# 2. 设置log级别
logger.setLevel(logging.INFO)
# 3. 创建handler, 用于输出控制台或写入文件
# 输出到控制台
fh_stream = logging.StreamHandler()
# 写入文件
fh_file = logging.FileHandler('./test.log')
# 4. 设置日志级别
fh_stream.setLevel(logging.INFO)

fh_file.setLevel(logging.INFO)
# 5. 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
fh_stream.setFormatter(formatter)

fh_file.setFormatter(formatter)
# 6. 添加handler
logger.addHandler(fh_stream)

logger.addHandler(fh_file)

# 7. 运行
logger.info('this is a info')
logger.debug('this is a debug')

# 2019-11-20 23:29:13,977 log_file_demo INFO this is a info
# 因为debug的级别小于info,所以不输出debug

```

#### 2.2 log级别:

#### 2.3 输出格式:
Format格式说明:
|格式|说明|
|-|-|
|%(levelno)s    |打印日志级别的数值|
|%(levelname)s  |打印日志级别名称|
|%(pathname)s   |打印当前执行程序的路径,其实是sys.argv[0]|
|%(filename)s   |打印当前执行程序名|
|%(funcName)s   |打印日志的当前函数|
|%(lineno)d     |打印诶之的当前行号|
|%(asctime)s    |打印日志的时间|
|%(thread)d     |打印线程ID|
|%(threadName)s |打印线程名称|
|%(process)d    |打印线程ID|
|%(message)s    |打印日志信息|

### 3.封装工具类:
#### 3.1 封装Log工具类:
utils/LogUtil.py
```python
# coding=utf-8

# 封装工具类
# 1.创建类
# 2.定义参数
    # 输出文件名称,Loggername,日志级别
# 3.编写输出到控制台或文件

import logging

log_l = {
    "info": logging.INFO, 
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}

class logger():
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file    # 扩展名, 配置文件
        self.log_name = log_name    # 
        self.log_level = log_level

        # 设置log名称
        self.logger = logging.getLogger(self.log_nam)
        # 设置log级别
        self.logger.setLevel(log_l[self.log_level])
        # 判断handler是否存在
        if not self.logger.handlers:
            # 输出到控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
            fh_stream.setFormatter(formatter)
            # 输出到文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            # 添加到handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
```

#### 3.2 重构配置文件:
config/conf.yml
```yaml
BASE:
  # log等级
  log_level: 'debug'
  # 扩展名
  log_extension: '.log'

  test:
    url: "http://211.103.136.242:8064"
```
#### 3.3 日志工具类应用
config/Conf.py
```python
# coding=utf-8
import os
from utils.YamlUtil import YamlReader
# 1. 获取项目基本目录
# 1.2 获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
print(current, BASE_DIR)
# 1.3 定义config目录的路径
_config_path =  
# 1.4 定义conf.yml的文件路径
_config_file = _config_path + os.sep + 'conf.yml'

# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"

def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

def get_log_path():
    """
    获取log文件路径
    """
    return _log_path

# 2. 读取配置文件
class ConfigYaml():
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

        # 获取需要的信息
        def get_config_url(self):
            return self.config['BASE']['test']['url']

        def get_conf_log(self):
            """
            获取日志级别
            """
            return self.config['BASE_DIR']['log_level']
        
        def get_conf_log_extension(self):
            return self.config['BASE_DIR']['log_extension']

if __name__ == "__main__":
    conf_read = ConfigYaml()
    print(conf_read)
    print(conf_read.get_conf_log())
    print(conf_read.get_conf_log_extension())
```

utils/LogUtil.py
```python
# 1.初始化参数数据
# 日志文件名称
log_path = Conf.get_log_path()
current_time = datetime.datetime.now().strftime('%Y-%m-%d')
log_extension = ConfigYaml().get_conf_log_extension()
logfile = os.path.join(log_path,current_time+log_extension)
print(logfile)

# 日志文件级别
loglevel = ConfigYaml().get_conf_log()
print(loglevel)

# 2. 对外方法: 初始化log工具类, 提供其他类使用
def my_log(log_name = __file__):
    return Logger(log_file=logfile, log_name=log_name, log_level=loglevel)

if __name__ == "__main__":
    my_log().debug("this is a debug")

```

## 六、pytesy框架：
### 1.安装与入门:
#### 1.1 介绍:
- 简单灵活;
- 容易上手;
- 文档丰富;
- 支持参数化 
### 2.基础使用:
```python
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

def test_b():
    print('---test_b---')
    assert func(3) == 4 # 断言成功

# 代码直接执行
if __name__ == "__main__":
    pytest.main(["pytest_demo.py"])
```
使用命令行直接执行测试脚本:
```shell
pytest pytest_demo.py
```

#### 2.1 函数级别方法: 
- 运行于*测试*方法的始末;
- 运行一次测试函数会运行一次setup和teardown;

```python
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
================================== test session starts ================================ 
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


================= 2 passed in 0.08 seconds ==================
"""
```

#### 2.2 类级别方法: 
- 运行于测试*类*的始末;
- 一个测试内只运行一次setup_class和teardown_class,不关心测试类内有多少测试函数
```python
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


"""
PS E:\学习\测试\InterAutoTest_W\testcase\t_pytest> python pytest_class.py
=============== test session starts ================= 
platform win32 -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: E:\学习\测试\InterAutoTest_W, inifile: pytest.ini
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 2 items                                                                                                                                                           

pytest_class.py ------setup_class------
test_a
.test_b
.------teardown_class------

============================ 2 passed in 0.04 seconds ==============================
"""
```
   

### 3. 常用插件:
- 常用插件: https://plugincompat.herokuapp.com
#### 3.1 测试报告:
- 应用场景:
    -  自动化测试脚本最终是通过还是不通过,需要通过测试报告进行提现.
- 安装:
```shell
pip install pytest-html
```
- 使用
    - 在配置文件中的命令行参数中增加 --html=用户路径/report.html

```ini
./pytest.ini
[pytest]
addopts = --html=./report/report.html
```
执行测试脚本,生成测试脚本
 
#### 3.2 失败重试: 
- 应用场景:
    - 当失败后尝试再次运行
- 安装:
```shell
pip install pytest-rerunfailures
```
- 使用:
    - 在配置文件中的命令行参数中增加 --reruns n  (n表示重试的次数)
    - 如果期望加上出错重试等待的时间, --rerun-delay

```ini
./pytest.ini

[pytest]
addopts = --html=./report/report.html --reruns 3 --reruns-delay=2
```


```python
# 使用装饰器,控制单个测试用例的运行情况
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_b():
    print('---test_b---')
    assert func(3) == 4 # 断言成功
```
在单个测试用例中设置运行控制,则不需要在配置文件中进行配置.

### 4. 数据参数化:
#### 4.1 传入单个参数:
@pytest.mark.parametrize(argnames, argvalues)
- argnames: 参数名;
- argvalues:参数对应值,类型必须为可迭代类型,一般为list
```python
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

'''
PS E:\学习\测试\InterAutoTest_W\testcase\t_pytest> python .\pytest_one.py
============== test session starts =================================
platform win32 -- Python 3.7.3, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: E:\学习\测试\InterAutoTest_W, inifile: pytest.ini
plugins: arraydiff-0.3, doctestplus-0.3.0, html-2.0.1, metadata-1.8.0, openfiles-0.3.2, remotedata-0.3.1, rerunfailures-8.0
collected 2 items                                                                                                                                                           

pytest_one.py test_a
xiaoming
.test_a
xiaohong
.

--------- generated html file: file://E:\学习\测试\InterAutoTest_W\testcase\t_pytest\report\report.html ---------
=================== 2 passed in 0.05s =================
'''
```


#### 4.2 传入多个参数:
@pytest.mark.parametrize(('参数1','参数2'), ([参数1_list], [参数2_list]))
- list的每个元素都是一个元组,元组里的每个元素和参数是按顺序一一对应的

```python
# coding=utf-8
"""
1. 创建类和测试方法
2. 创建数据
3. 创建参数化
4.运行
"""
import pytest

class TestClass():
    data_list = [('xiaoming', '12345'),('xiaohong', '56789')]

    @pytest.mark.parametrize(('name','psw'),data_list)
    def test_a(self, name,psw):
        print('test_a')
        print(name,psw)
        assert 1


if __name__ == "__main__":
    pytest.main(['-s','pytest_more.py'])


'''
PS E:\学习\测试\InterAutoTest_W\testcase\t_pytest> python .\pytest_more.py
======================= test session starts ====================== 
platform win32 -- Python 3.7.3, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: E:\学习\测试\InterAutoTest_W, inifile: pytest.ini
plugins: arraydiff-0.3, doctestplus-0.3.0, html-2.0.1, metadata-1.8.0, openfiles-0.3.2, remotedata-0.3.1, rerunfailures-8.0
collected 2 items                                                                                                                                                           

pytest_more.py test_a
xiaoming 12345
.test_a
xiaohong 56789
.

------- generated html file: file://E:\学习\测试\InterAutoTest_W\testcase\t_pytest\report\report.html ----------------
===================== 2 passed in 0.06s ============================
'''
```

### 5.应用接口用例:
- 登录；
- 个人信息；
- 获取商品信息；
- 购物车；
- 订单； 

#### 5.1 pytest运行原则:
##### 5.2.1 默认规则:
- 在不指定运行目录,运行文件,运行函数等参数的默认情况下, pytest会执行当前目录下所有的以test为前缀(test*.py)或以_test为后缀(_test.py)的文件中以test为前缀的函数.

```python
# coding=utf-8

"""
1. 根据默认运行原则,调整py文件命名,函数命名
2. pytest.main()运行,或者命令行直接运行
"""

import sys

sys.path.append('../')
import pytest
import requests
from utils.RequestsUtil import Request, r_get,r_post

request = Request(url='http://211.103.136.242:8064')

def test_login():
    """
    登录
    """
    url = 'http://211.103.136.242:8064/authorizations/'
    data = {'username':'python', 'password':'12345678'}

    r = r_post(url, json=data)
    print(r)

"""
PS E:\学习\测试\InterAutoTest_W\testcase> python .\test_mall.py
============================ test session starts ======================================== 
platform win32 -- Python 3.7.3, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: E:\学习\测试\InterAutoTest_W, inifile: pytest.ini
plugins: arraydiff-0.3, doctestplus-0.3.0, html-2.0.1, metadata-1.8.0, openfiles-0.3.2, remotedata-0.3.1, rerunfailures-8.0
collected 1 item                                                                                                                                                            

test_mall.py {'code': 200, 'body': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1NzQ4NTAyMzIsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.GLoT8ncQu9Pd74x0EoVjiXdnKED6JsB4WkasS8d6aPw', 'username': 'python', 'user_id': 1}}
.

--------- generated html file: file://E:\学习\测试\InterAutoTest_W\testcase\report\report.html -------------
========================= 1 passed in 2.34s =========================
"""

```

##### 5.2.2 自定义规则运行:
使用pytest.ini文件配置:
```ini
./pytest.ini
addopts = -s
# 运行参数

testpaths = testcases
# 当前目录下的script文件夹, -可自定义

python_files = test_*.py
# 当前目录下的script文件夹下,以test_开头,以.py结尾的所有文件

python_classes = Test_*
# 当前目录下的script文件夹下,以test_开头,以.py结尾的所有文件, 以Test_开头的类 -可自定义

python_functions = test_*
# 当前目录下的script文件夹下,以test_开头,以.py结尾的所有文件, 以Test_开头的类, 以test_开头的方法 -可自定义
```

## 七、结果断言:
### 1.结果断言验证:
#### 1.1 常用断言:
- 介绍:
    - 断言是自动化最终的目的,一个用例没有断言,就失去了自动化测试的意义了;
    - 断言用到的是assert关键字;
    - 预期结果和实际结果做对比;
- 常用断言:

|情况|语句|
|-|-|
|判断x为真|assert x|
|判断x不为真|assert not x|
|判断b包含a| assert a in b|
|判断a等于b|assert a == b|
|判断a不等于b|assert a != b|

#### 1.2断言应用接口用例:
- 返回状态码:
- 结果验证:

#### 1.3断言封装

```python
./utils/AssertUtil.py
# coding=utf-8
"""
1. 定义封装类;
2. 初始化数据,日志
3. code相等
4. body相等
5.body包含
"""
import json
from utils.LogUItil import my_log

class AssertUtil():

    def __init__(self):
        self.log = my_log('AssertUtil')

    def assert_code(self, code, expected_code):
        """
        验证返回状态码
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except Exception as e:
            self.log.error(f'code error, code is {code}, expected_code is {expected_code}')
            raise
    
    def assert_body(self, body, expected_body):
        """
        验证返回结果内容相等
        """
        try:
            assert body == expected_body
            return True
        except Exception as e:
            self.log.error(f'body error, body is {body}, expected_body is {expected_body}')
            raise

    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含期望的结果
        """
        try:
            assert json.dumps(body) in json.dumps(expected_body)
            return True
        except Exception as e:
            self.log.error(f'body error, body not in expected_body, body is {body}, expected_body is {expected_body}')
            raise
```

### 2. 数据库结果断言验证:
#### 2.1 pymysql安装及简单实用:
- 安装:
```shell
pip install pymysql
```
- 简单实用:
```python
# coding=utf-8
"""
1. 导入pymysql
2. 链接database
3. 获取执行sql的光标对象
4. 执行sql
5. 关闭对象
"""
import pymysql

cnn = pymysql.connect(
    host='211.103.136.242',
    port=7090, 
    user='test',
    password='test123456',
    database='meiduo',
    charset='utf8',
    )

with cnn.cursor() as cursor:
    sql_str = 'select * from tb_users'
    cursor.execute(sql_str)
    res = cursor.fetchall()
    print(res)

cnn.close()
```
#### 2.2 工具类封装及使用:
- pymysql工具类封装:

```python
./utils/Mysqlutil.py
# coding=utf-8
"""
1. 创建封装类
2.初始化数据,连接数据库,光标对象
3. 创建查询,执行方法
4. 关闭对象
"""
import pymysql
import functools

from utils.LogUItil import my_log

class Mysql():
    def __init__(self,host,user,password,database,port=3306,charset='utf8'):
        self.cnn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        self.cursor = self.cnn.cursor()
        self.log = my_log()

    def __del__(self):
        try:
            self.cnn.close()
        except Exception as e:
            pass

        try:
            self.cursor.close()
        except Exception as e:
            pass

    def fetch_one(self, sql):
        """
        查询一个对象
        """
        self.cursor.execute(sql)
        return self.fetchone()

    def fetch_all(self, sql):
        """
        查询全部对象
        """
        self.cursor.execute(sql)
        return self.fetchall()

    def exec(self,sql):
        """
        执行操作
        """
        try:
            self.cursor.execute(sql)
            self.cursor.commit()
        except Exception as e:
            self.cnn.rollback()
            self.log.error(e)
            return False
        return True

if __name__ == "__main__":
    mysql = Mysql(
        host='211.103.136.242',
        port=7090, 
        user='test',
        password='test123456',
        database='meiduo',
        charset='utf8',
    )
    res = mysql.fetch_all('select * from tb_uders')
    print(res)
```

- 配置文件:

```yml
# ./config/db_conf.yml
db_1:
  db_host: "211.103.136.242"
  db_port: 7090
  db_user: "test"
  db_password: "test123456"
  db_database: "meiduo"
  db_charset: "utf8"

```

```python
./config/Conf.py
"""
1. 创建db_conf.yml
2. 编写数据库基本信息
3. 重构Conf.py
4. 执行
"""

...

# 定义db_conf.yml文件路径
_db_config_file = _config_path + os.sep + 'db_conf.yml'

def get_db_conf_file():
    """
    获取db_conf文件路径
    """
    return _db_config_file


# 2. 读取配置文件
class ConfigYaml():
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_conf_file()).data()

    def get_db_conf_info(self, db_alias):
        """
        根据db_alias获取数据库相关参数
        """
        return self.db_config[db_alias]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    ......
    print(conf_read.get_db_conf_info('db_1'))
```

- 数据库结果验证:
    - 1. 初始化数据库信息,Base.py, init_db
    - 2. 接口用例返回结果内容进数据库验证
```python
# ./common/Base.py

# coding=utf-8
# 1.定义一个方法init_db
# 2.初始化数据库信息, 通过配置文件来完成
# 3.初始化mysql对象

from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql


def init_db(db_alias):
    db_init = ConfigYaml().get_db_conf_info(db_alias)
    host = db_init.get('host', '127.0.0.1')
    port = int(db_init.get('port', 3306))
    user = db_init.get('user')
    database = db_init.get('database')
    password = db_init.get('password')
    charset = db_init.get('charset', 'utf8')

    conn = Mysql(host=host,port=port,user=user,password=password,database=database,charset=charset)
    return conn

if __name__ == "__main__":
    conn = init_db('db_1')
    print(conn)
```

## 八、数据驱动：
### 1. yaml数据驱动:
#### 1.1 yaml测试用例:
```yml
#./data/testlogin.yml
# 登录的测试用例:

# 测试名称:
# url地址
# data
# 期望结果
---
'case_name':"登陆成功用例"
'url': 'http://211.103.136.242:8064/authorizations/'
'data': 
  'username': "python"
  'password': "12345678"
'expect': "'username': 'python', 'user_id': 1"
---
'case_name':"登陆失败用例"
'url': 'http://211.103.136.242:8064/authorizations/'
'data': 
  'username': "test123456"
  'password': "1231111"
'expect': "'username': 'python', 'user_id': 1"

```

#### 1.2 参数化:
```python
# ./testcase/test_login.py

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
```

### 2. Excel数据驱动
#### 2.1 excel用例设计:
(./data/testdata.xlsx)
#### 2.2 excel读取:
```python
# coding=utf-8

"""
1. 导入包, xlrd(python自带)
2. 创建workbook对象
3. sheet对象
4. 获取行数和列数
5. 读取每行的内容
6. 读取每列的内容
7. 读取固定列的内容
"""
import xlrd
book = xlrd.open_workbook('./testdata.xlsx')
# 获取表的两种方式: 
# 索引
# sheet = book.sheet_by_index(0)
# 名称
sheet = book.sheet_by_name('美多商城接口测试')

rows = sheet.nrows  # 行数
cols = sheet.ncols  # 列数
print(f"rows:{rows}, cols:{cols}")

# 获取每行数据
for r in range(rows):
    r_values = sheet.row_values(r)
    print(r_values)

# 获取每列数据
for c in range(cols):
    c_values = sheet.col_values(c)
    print(c_values)

# 读取固定列的内容
v = sheet.cell(1,2)
print(v)
```
#### 2.3 封装excel工具类:

```python
# ./utils/ExcelUtil.py

# coding=utf-8
# 目的: 参数化, pytest list

# 1. 验证文件是否存在,存在读取,不存在错报
# 2. 读取sheet方式, 名称,索引
# 3. 读取sheet内容
    # 返回list, 字典
    # 格式: [{'a':"a1",'b':" b1"}, {'a':"a2",'b':"b2"}]
# 4. 结果返回

import os
import xlrd

# 自定义异常
class  SheetTypeError(object):
    pass

class ExcelReader():
    def __init__(self, excel_file, sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self.data_list = []
        else:
            raise FileNotFoundError("文件不存在")

    def data(self):
        if self.data_list:
            return self.data_list

        workbook = xlrd.open_workbook(self.excel_file)

        if type(self.sheet_by) not in [str,int]:
            raise SheetTypeError("参数错误")
        elif type(self.sheet_by) == int:
            sheet = workbook.sheet_by_index(self.sheet_by)
        elif type(self.sheet_by) == str:
            sheet = workbook.sheet_by_name(self.sheet_by)

        # 获取首行信息
        title = sheet.row_values(0)
        for r in range(1, sheet.nrows):
            self.data_list.append(dict(zip(title,sheet.row_values(r))))
        # print(self.data_list)
        return self.data_list

if __name__ == "__main__":
    excel_reader = ExcelReader('../data/testdata.xlsx',"美多商城接口测试")
    print(excel_reader.data())

```


#### 2.4 excel参数化运行:
- 获取是否运行;
- 参数化;
- 结果断言;

```python
# ./common/ExcelConfig.py
# coding=utf-8

# 定义类
# 定义列属性
# 定义excel的映射

class DataConfig():
    # 用例属性:
    case_id = "用例ID"
    case_model = "模块"
    case_name = "接口名称"	
    url = "请求URL"	
    pre_exec = "前置条件"	
    method = "请求类型"	
    params_type = "请求参数类型"	
    params = "请求参数"	
    expect_result = "预期结果"	
    actual_result = "实际结果"	
    beizhu = "备注"	
    is_run = "是否运行"	
    headers = "headers"	
    cookies = "cookies"	
    code = "status_code" 	
    db_verify = "数据库验证"
```

```python
# ./config/ExcelData.py
# coding=utf-8

# 1. 使用excel工具类, 获取结果list
# 2. 列"是否运行内容", y
# 3. 保存要执行结果, 放到新的列表中
import sys
sys.path.append('../')
from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig

class Data():
    def __init__(self, excel_file, sheet_by):
        self.reader = ExcelReader(excel_file, sheet_by)
        self.run_list = []

    def get_run_data(self):
        """
        根据"是否运行"列,获取执行测试用例
        """
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == 'y':
                self.run_list.append(line)
        return self.run_list
```
#### 2,4 动态的headers请求
- 1) 判断header是否存在? json转义: 无需
- 2) 增加Headers
- 3) 增加cookies
- 4) 发送请求

## 九、Allure报告：

## 十、邮件配置：

## 十一、本章总结







