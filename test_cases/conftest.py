"""
Pytest 配置文件
定义全局 fixture（测试夹具），供所有测试用例共享
"""

import pytest
from utils.request_util import RequestUtil

@pytest.fixture(scope="class")
def api():
    # 创建一个 RequestUtil 实例对象，作为测试夹具
    # 测试方法的参数里写上 api，Pytest 会自动传入这个实例对象
    return RequestUtil()