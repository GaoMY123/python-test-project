"""
1.收集用例
2.打开html文件
3.运行用例
4.收集结果
5.将结果写入html文件
"""
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite=unittest.defaultTestLoader.discover('./', 'test_*.py')

    with open('./report/test.html',"wb") as f:
        # HTMLTestRunner(f).run(suite)
        HTMLTestRunner(f,2,'测试报告','测试用例执行结果').run(suite)