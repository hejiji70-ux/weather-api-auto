"""
HTTP 请求工具类
封装 Requests 库，统一处理 URL 拼接、参数追加、日志记录
"""

import requests
from config.env import config  # 导入配置字典（base_url, geo_url, api_key）
from utils.logger import log   # 导入全局日志对象


class RequestUtil:
    """请求工具类，封装 GET 请求的通用逻辑"""
    def __init__(self):
        self.base_url = config['base_url']   # 天气接口基础域名（如 https://xxx/v7）
        self.geo_url = config['geo_url']     # 城市搜索接口基础域名（如 https://xxx）
        self.api_key = config['api_key']     # API Key

    def get(self, path, params=None, use_geo=False):
        # 如果调用者没有传 params，初始化为空字典
        if params is None:
            params = {}
        # 把所有请求自动追加 api_key 参数
        params['key'] = self.api_key

        # use_geo (bool)：是否使用城市搜索的域名（True → geo_url，False → base_url）
        # path (str)：接口路径，如 "/weather/now"
        if use_geo:
            # 城市搜索：https://xxx.com + /geo/v2/city/lookup
            url = self.geo_url + path
        else:
            # 天气接口：https://xxx.com/v7 + /weather/now
            url = self.base_url + path

        # 打印请求信息到日志（方便调试）
        log.info(f"请求URL: {url}")
        log.info(f"请求参数: {params}")
        # 发送 GET 请求（params 会被 requests 自动拼接到 URL 后面）
        resp = requests.get(url, params=params)
        # 打印响应信息到日志
        log.info(f"响应状态码: {resp.status_code}")
        log.info(f"响应体前200字符: {resp.text[:200]}")
        # 返回的 Response 响应对象
        return resp