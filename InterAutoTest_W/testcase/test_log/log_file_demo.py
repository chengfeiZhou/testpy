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



