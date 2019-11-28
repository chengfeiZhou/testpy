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
        self.cursor = self.cnn.cursor(cursor=pymysql.cursor.DictCursor) # 结果使用dict返回
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


"""
1. 创建db_conf.yml
2. 编写数据库基本信息
3. 重构Conf.py
4. 执行
"""


# cnn = pymysql.connect(
#     host='211.103.136.242',
#     port=7090, 
#     user='test',
#     password='test123456',
#     database='meiduo',
#     charset='utf8',
#     )

# with cnn.cursor() as cursor:
#     sql_str = 'select * from tb_users'
#     cursor.execute(sql_str)
#     res = cursor.fetchall()
#     print(res)

# cnn.close()





