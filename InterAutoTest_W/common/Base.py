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

