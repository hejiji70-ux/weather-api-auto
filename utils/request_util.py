import requests
from config.env import config
from utils.logger import log


class RequestUtil:
    def __init__(self):
        self.base_url = config['base_url']
        self.geo_url = config['geo_url']
        self.api_key = config['api_key']

    def get(self, path, params=None, use_geo=False):
        if params is None:
            params = {}
        params['key'] = self.api_key

        if use_geo:
            url = self.geo_url + path
        else:
            url = self.base_url + path

        log.info(f"请求URL: {url}")
        log.info(f"请求参数: {params}")

        resp = requests.get(url, params=params)

        log.info(f"响应状态码: {resp.status_code}")
        log.info(f"响应体前200字符: {resp.text[:200]}")

        return resp