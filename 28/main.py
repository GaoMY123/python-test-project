# 脚本1：1.打开qq邮箱，https://mail.qq.com/，用qq进行登录,输入用户名，密码点击登录后即可
# 脚本2：1. 打开 baidu.com 2. 点击左上角的 "hao123" 3. 在百度搜索框中输入"国庆节"并点击"百度一下" 4. 若链接标题中出现 "国庆节_百度百科"，则脚本通过
# 要求： 1. 使用PO模式编写代码
import unittest

if __name__ == '__main__':
    suit = unittest.defaultTestLoader.discover('./scripts/', 'test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suit)