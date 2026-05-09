"""
日志模块
配置全局日志格式，同时输出到文件和控制台
"""

import logging
import os

# 获取项目根目录下 reports/ 文件夹的路径
log_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
# 如果 reports/ 文件夹不存在，就创建它
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
# 配置日志的基本设置
logging.basicConfig(
    level=logging.INFO,    # 日志级别：INFO（普通信息）、WARNING（警告）、ERROR（错误）
    # 日志格式：时间 - 级别 - 消息内容
    format='%(asctime)s - %(levelname)s - %(message)s',
    # 两个处理器（handler）：一个写文件，一个输出到屏幕
    handlers=[
        # 文件处理器：把日志写入 reports/test.log 文件，编码 UTF-8
        logging.FileHandler(os.path.join(log_dir, 'test.log'), encoding='utf-8'),
        # 流处理器：同时把日志输出到终端（屏幕）
        logging.StreamHandler()
    ]
)
# 创建一个全局的 log 对象，其他文件直接 from utils.logger import log 使用
log = logging.getLogger()