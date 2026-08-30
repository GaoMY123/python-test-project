import unittest

if __name__ == '__main__':
    #执行测试用例
    suite = unittest.defaultTestLoader.discover('./', 'test_*.py')
    # 创建TextTestRunner对象
    runner = unittest.TextTestRunner()
    # 运行用例
    runner.run(suite)
