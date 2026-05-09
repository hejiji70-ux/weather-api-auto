"""
和风天气 API 接口测试用例
采用数据驱动模式：YAML 文件定义用例数据，Pytest 自动循环执行
"""

import pytest
import allure
import yaml
import os

def load_cases():
    """
    从 YAML 文件加载测试数据
    返回一个列表，列表中每个元素是一条用例的字典
    """
    # 获取 test_data/weather_cases.yaml 的完整路径
    case_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'test_data', 'weather_cases.yaml'
    )
    # 读取并解析 YAML 文件
    with open(case_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@allure.feature("和风天气 API 接口测试")
class TestWeatherAPI:
    # @pytest.mark.parametrize：Pytest 的参数化装饰器
    @pytest.mark.parametrize(
        "case",         # 参数名，对应测试方法的 case 参数
        load_cases(),   # 加载 YAML 中的所有用例数据
        # 列表推导式，从每个用例中提取 case_id 作为标识
        ids=[c['case_id'] for c in load_cases()]
    )
    def test_weather_api(self, api, case):
        """
            接口测试用例模板（每条 YAML 数据都会跑一次这个方法）
            参数：
                api：conftest.py 定义的 RequestUtil 实例（Pytest 自动注入）
                case：YAML 中的一条用例数据（Pytest 自动注入）
        """
        # 设置 Allure 报告中显示的用例标题和描述
        allure.dynamic.title(case['case_name'])
        allure.dynamic.description(f"用例ID: {case['case_id']}")
        # ===== 步骤1：发送请求 =====
        with allure.step(f"发送 GET 请求到 {case['path']}"):
            resp = api.get(
                case['path'],               # 接口路径
                case.get('params'),         # 请求参数
                case.get('use_geo', False)  # 是否使用城市搜索域名
            )

        # ===== 步骤2：验证 HTTP 状态码 =====
        with allure.step("验证 HTTP 状态码为 200"):
            expected_http_status = case.get('expect_http_status', 200)
            assert resp.status_code == expected_http_status, \
                f"期望HTTP状态码 {expected_http_status}，实际 {resp.status_code}"

        # ===== 步骤3：验证返回的是 JSON 格式 =====
        with allure.step("验证返回 JSON 格式"):
            data = resp.json()
            assert isinstance(data, dict), "返回不是 JSON 对象"

        # ===== 步骤4：验证业务状态码（code 字段） =====
        with allure.step(f"验证返回 code 为 '{case['expect_code']}'"):
            # 适配不同响应结构：成功时 code 在顶层，失败时嵌套在 error.status 中
            if 'code' in data:
                actual_code = str(data['code'])
            elif 'error' in data and isinstance(data['error'], dict):
                actual_code = str(data['error'].get('status', ''))
            else:
                actual_code = ''
            assert actual_code == case['expect_code'], \
                f"期望 code={case['expect_code']}，实际 code={actual_code}"

        # ===== 步骤5：验证关键字段存在（仅部分正常用例有此要求） =====
        if 'expect_key' in case:
            with allure.step(f"验证返回包含字段 '{case['expect_key']}'"):
                assert case['expect_key'] in data, \
                    f"返回 JSON 中缺少字段 '{case['expect_key']}'"

        # 把完整的响应 JSON 附加到 Allure 报告中（失败时可以直接查看）
        allure.attach(
            str(resp.json()),
            "响应内容",
            allure.attachment_type.JSON
        )