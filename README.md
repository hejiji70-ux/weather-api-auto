# 和风天气 API 接口自动化测试

## 项目简介
基于 Python + Requests + Pytest + Allure 的和风天气 API 接口自动化测试框架。
采用 YAML 数据驱动实现测试数据与代码分离，通过 GitHub Actions 实现代码推送后自动触发测试。

## 技术栈
- **Python 3.11**：主编程语言
- **Requests**：HTTP 请求封装
- **Pytest**：测试框架，支持参数化和 fixture
- **YAML**：测试数据驱动，数据与代码分离
- **Allure**：可视化测试报告
- **GitHub Actions**：持续集成（CI），推送代码自动运行测试

## 项目结构
weather_api_auto/
├── .github/workflows/ # GitHub Actions CI 配置
│ └── test.yml # 自动测试工作流定义
├── config/ # 配置文件目录
│ ├── config.yaml # 环境配置（API Key、域名）
│ └── env.py # 配置加载模块
├── utils/ # 工具类目录
│ ├── request_util.py # RequestUtil 封装类（统一请求 + 断言）
│ └── logger.py # 日志模块
├── test_data/ # 测试数据目录
│ └── weather_cases.yaml # YAML 数据驱动用例
├── test_cases/ # 测试用例目录
│ ├── conftest.py # Pytest fixture 定义
│ └── test_weather_api.py # 接口测试用例
├── reports/ # Allure 原始数据输出目录
├── postman/ # Postman 集合文件（备份）
├── run.py # 一键运行入口
├── requirements.txt # Python 依赖清单
└── README.md # 本文件

## 快速开始

### 1. 克隆项目
git clone https://github.com/hejiji70-ux/weather-api-auto.git
cd weather-api-auto

### 2. 安装依赖
pip install -r requirements.txt

### 3. 配置 API Key
将 config/config.yaml.example 重命名为 config/config.yaml，并完成以下配置：
base_url: "https://nj65np8ukv.re.qweatherapi.com/v7"
geo_url: "https://nj65np8ukv.re.qweatherapi.com"
api_key: "a19b5082a277449186531343580ae182"

### 4. 运行测试
python run.py

### 5. 查看报告
allure serve ./reports
如果只想生成报告不自动打开浏览器：
allure generate ./reports -o ./allure-report --clean

## 测试覆盖
- 实况天气查询（正常/异常参数）
- 7天预报查询（正常场景）
- 城市搜索（正常场景）
- API Key 校验（错误 Key）
- 必填参数校验（空值）
共 10 条 自动化用例，覆盖 3 个接口的正常与异常场景。

## 用例数据
测试数据统一管理在 test_data/weather_cases.yaml 中，
通过 Pytest @parametrize 实现数据驱动，新增用例只需添加 YAML 配置。

## GitHub Actions 持续集成

本项目配置了 GitHub Actions，每次推送代码到 `main` 分支时，自动触发测试流程。

### CI 工作流程

| 步骤 | 说明 |
|:---|:---|
| 检出代码 | 将仓库代码下载到 GitHub 云服务器 |
| 安装 Python | 安装 Python 3.10 环境 |
| 安装依赖 | 执行 `pip install -r requirements.txt` |
| 创建配置文件 | 从 GitHub Secrets 读取 `QWEATHER_API_KEY`，动态生成 `config.yaml` |
| 运行测试 | 执行 `pytest -v` 运行全部用例 |
| 上传报告 | 将 Allure 测试结果打包，可在 Actions 页面下载 |

### 如何配置 GitHub Secrets

1. 打开你的 GitHub 仓库 → **Settings**
2. 左侧菜单 → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. Name 填：`QWEATHER_API_KEY`
5. Secret 填：你的和风天气 API Key
6. 点击 **Add secret**

### 查看 CI 运行状态

1. 打开仓库 → 点击 **Actions** 选项卡
2. 查看最新工作流运行记录
3. 绿色 ✅ = 全部通过 | 红色 ❌ = 有失败，点进去查看日志

## 项目亮点

- **数据驱动**：测试数据统一管理在 YAML 文件中，新增用例只需添加配置，无需修改代码
- **工具类封装**：`RequestUtil` 统一管理请求发送、参数拼接、日志记录，减少重复代码
- **多接口适配**：通过 `use_geo` 标志位自动切换两套 URL 体系（城市搜索 vs 天气接口）
- **CI/CD 集成**：GitHub Actions 实现代码推送自动触发测试，保证每次提交都经过验证
- **可视化报告**：Allure 报告包含步骤详情和响应附件，失败用例可快速定位