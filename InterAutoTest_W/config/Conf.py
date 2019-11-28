# coding=utf-8
import os
import sys
sys.path.append('../')
from utils.YamlUtil import YamlReader
# 1. 获取项目基本目录
# 1.2 获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(current, BASE_DIR)
# 1.3 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"
_data_path = BASE_DIR + os.sep + "data"
# 1.4 定义conf.yml的文件路径
_config_file = _config_path + os.sep + 'conf.yml'

# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"

# 定义db_conf.yml文件路径
_db_config_file = _config_path + os.sep + 'db_conf.yml'

# 配置report路径
_report_path = BASE_DIR + os.sep + "report"

def get_report_path():
    return _ewport_path

def get_config_path():
    return _config_path

def get_data_path():
    return _data_path

def get_config_file():
    return _config_file

def get_log_path():
    """
    获取log文件路径
    """
    return _log_path

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

    def get_excel_file(self):
        """
        获取excel测试用例文件名称
        """
        return self.config['BASE']['test']['case_file']

    
    def get_excel_sheet(self):
        """
        获取excel测试用例文件sheet名称
        """
        return self.config['BASE']['test']['case_sheet']

    # 获取需要的信息
    def get_config_url(self):
        return self.config['BASE']['test']['url']

    def get_conf_log(self):
        """
        获取日志级别
        """
        return self.config['BASE']['log_level']
    
    def get_conf_log_extension(self):
        return self.config['BASE']['log_extension']
    
    def get_db_conf_info(self, db_alias):
        """
        根据db_alias获取数据库相关参数
        """
        return self.db_config[db_alias]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    print(conf_read)
    print(conf_read.get_conf_log())
    print(conf_read.get_conf_log_extension())
    print(conf_read.get_db_conf_info('db_1'))
    # print(conf_read.get_excel_file())
    # print(conf_read.get_excel_sheet())
    