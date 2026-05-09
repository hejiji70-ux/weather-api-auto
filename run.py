import pytest
import os
import shutil   # Python 的高级文件操作模块（shell utility）

if __name__ == '__main__':
    # 1.清空上次的报告数据
    # reports/ 目录存放 Allure 原始数据（JSON、TXT 等中间文件）
    report_dir = './reports'
    # 如果 reports 文件夹已存在，递归删除里面的所有文件和子文件夹
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
    # 重新创建一个空的 reports 文件夹
    os.makedirs(report_dir)

    # 2.重新创建 .gitkeep，保证空目录能被 Git 追踪（Git 默认不追踪空文件夹，加了这个文件就能被提交到仓库）
    with open(os.path.join(report_dir, '.gitkeep'), 'w', encoding='utf-8') as f:
        pass   # 不写入任何内容，只创建一个空文件

    # 3.运行 Pytest 测试（-v：详细模式，--alluredir=./reports：把测试结果（步骤、断言、附件）保存到 reports/ 目录）
    pytest.main(['-v', '--alluredir=./reports', './test_cases/'])

    # 4.提示用户如何查看报告
    print("\n✅ 测试完成！运行以下命令查看 Allure 报告：")
    print("   allure serve ./reports")