# 和风天气 API 接口自动化测试

## 项目简介
基于 Python + Requests + Pytest + Allure 的和风天气 API 接口自动化测试框架。

## 技术栈
- Python 3.8+
- Requests（HTTP 请求封装）
- Pytest（测试框架 + 参数化）
- YAML（数据驱动）
- Allure（可视化测试报告）

## 项目结构
weather_api_auto/
├── config/             # 配置文件
├── utils/              # 工具类（请求封装、日志）
├── test_data/          # YAML 测试数据
├── test_cases/         # Pytest 测试用例
├── reports/            # Allure 报告输出
├── postman/            # Postman 集合文件
├── run.py              # 一键运行入口
└── requirements.txt    # 依赖清单

## 快速开始

### 1. 克隆项目
git clone https://github.com/hejiji70-ux/weather-api-auto.git
cd weather-api-auto

### 2. 安装依赖
pip install -r requirements.txt

### 3. 配置 API Key
将 config/config.yaml.example 重命名为 config/config.yaml，
并填入你的和风天气 API Key。

### 4. 运行测试
python run.py

### 5. 查看报告
allure serve ./reports

## 测试覆盖
- 实况天气查询（正常/异常参数）
- 7天预报查询（正常场景）
- 城市搜索（正常场景）
- API Key 校验（错误 Key）
- 必填参数校验（空值）

## 用例数据
测试数据统一管理在 test_data/weather_cases.yaml 中，
通过 Pytest @parametrize 实现数据驱动，新增用例只需添加 YAML 配置。