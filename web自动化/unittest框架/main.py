"""
1.创建test开头的测试文件
2.导入unittest模块
3.新建 TestLogin 类，并继承 unittest.TestCase
4.编写test_login_success 方法，打印 success
5.编写test_login_failed 方法，打印 failed
6.编写 main 入口，并将 “unittest.main()” 添加到程序入口中
"""

import unittest
from test_login import TestLogin
from test_logout import TestLogout

if __name__ == '__main__':
    #收集用例
    #创建TestSuite对象
    #运行指定用例
    # suite=unittest.TestSuite()
    # #添加用例
    # suite.addTest(TestLogin('test_case1'))
    # suite.addTest(TestLogout('test_case1'))
    # #创建TextTestRunner对象
    # runner=unittest.TextTestRunner()
    # #运行用例
    # runner.run(suite)
    #运行所有用例
    suite = unittest.defaultTestLoader.discover('./', 'test_*.py')
    #创建TextTestRunner对象
    runner=unittest.TextTestRunner()
    #运行用例
    runner.run(suite)