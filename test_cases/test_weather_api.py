import pytest
import allure
import yaml
import os


def load_cases():
    case_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'test_data', 'weather_cases.yaml'
    )
    with open(case_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@allure.feature("和风天气 API 接口测试")
class TestWeatherAPI:

    @pytest.mark.parametrize(
        "case",
        load_cases(),
        ids=[c['case_id'] for c in load_cases()]
    )
    def test_weather_api(self, api, case):
        allure.dynamic.title(case['case_name'])
        allure.dynamic.description(f"用例ID: {case['case_id']}")

        with allure.step(f"发送 GET 请求到 {case['path']}"):
            resp = api.get(
                case['path'],
                case.get('params'),
                case.get('use_geo', False)
            )

        with allure.step("验证 HTTP 状态码为 200"):
            expected_http_status = case.get('expect_http_status', 200)
            assert resp.status_code == expected_http_status, \
                f"期望HTTP状态码 {expected_http_status}，实际 {resp.status_code}"

        with allure.step("验证返回 JSON 格式"):
            data = resp.json()
            assert isinstance(data, dict), "返回不是 JSON 对象"

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

        if 'expect_key' in case:
            with allure.step(f"验证返回包含字段 '{case['expect_key']}'"):
                assert case['expect_key'] in data, \
                    f"返回 JSON 中缺少字段 '{case['expect_key']}'"

        allure.attach(
            str(resp.json()),
            "响应内容",
            allure.attachment_type.JSON
        )