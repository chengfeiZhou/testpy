# coding=utf-8
# 1.定义一个方法init_db
# 2.初始化数据库信息, 通过配置文件来完成
# 3.初始化mysql对象
import sys
sys.path.append('../')
import json
import re
from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log


p_data = r'\${(.*)}\$'
log = my_log()
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

def assert_db(db_name, res_body, db_verify):
    """
    数据库验证
    """
    assert_util = AssertUtil()
    sql = init_db(db_name)
    db_res = sql.fetch_one(db_verify)
    log.debug(f"数据库查询结果:{str(db_res)}")
    for db_k,db_v in db_res.items():
        res_line = res_body[db_k]
        assert_util.assert_body(res_line, db_v)

def json_parse(data):
    """
    格式化数据
    """
    return json.loads(data) if data else data

def res_find(data, pattern_data=p_data):
    """
    查询匹配
    """
    pattern = re.compile(pattern_data)
    res = pattern.findall(data)
    return res


def res_sub(data, replace, pattern_data=p_data):
    """
    请求参数替换
    :param data: 源字符串
    :param replace: 替换内容 
    :param pattern_data: 匹配规则
    """
    pattern = re.compile(pattern_data)
    res = pattern.findall(data)
    if res:
        return re.sub(pattern_data,replace, data)
    else:
        return res

def params_find(headers, cookies):
    """
    验证请求中是否有${}$需要结果关联
    
    """
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    
    return headers, cookies

if __name__ == "__main__":
    # conn = init_db('db_1')
    # print(conn)

    print(res_find('{"Authorization": "JWT ${token}$"}', r'\${(.*)}\$'))
    print(res_sub('{"Authorization": "JWT ${token}$"}', '123'))
