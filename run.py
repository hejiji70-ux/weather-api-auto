import pytest
import os
import shutil

if __name__ == '__main__':
    # 清空上次的报告数据
    report_dir = './reports'
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
    os.makedirs(report_dir)

    # 重新创建 .gitkeep，保证空目录能被 Git 追踪
    with open(os.path.join(report_dir, '.gitkeep'), 'w', encoding='utf-8') as f:
        pass

    pytest.main(['-v', '--alluredir=./reports', './test_cases/'])
    print("\n✅ 测试完成！运行以下命令查看 Allure 报告：")
    print("   allure serve ./reports")