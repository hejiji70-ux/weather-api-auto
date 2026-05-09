"""
配置加载模块
负责读取 config.yaml 文件，并对外提供 config 字典
"""
import yaml
import os

def load_config():
    # 获取当前文件所在目录（即 config/ 文件夹），并且拼接出 config.yaml 的完整路径
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

    with open(config_path, 'r', encoding='utf-8') as f:
        # yaml.safe_load() 把 YAML 文本解析成 Python 字典
        return yaml.safe_load(f)
# 在模块被导入时，立即执行一次 load_config()
# 这样其他地方直接 from config.env import config 就能拿到配置,不用再调用函数，节省了调用（重复读取文件）的步骤
config = load_config()  # 存储load_config()函数执行后的结果（return yaml.safe_load(f)）