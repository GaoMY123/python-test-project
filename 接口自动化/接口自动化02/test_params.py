import unittest

from ddt import ddt,data,unpack

@ddt
class TestParams(unittest.TestCase):
    @data("如果情绪有天气，那我困在阴天里","Start your day"," ???????? ")
    def test_case1(self,text):
        """
        评论接口
        :return:
        """
        print(f"我的评论内容是{text}")
    @data(("zs","zs123"),("ls","ls123"))
    @unpack#将元组中的数据解包，赋值给username,password变量
    def test_case2(self,username,password):
        """
        登录接口
        :return:
        """
        print("我的用户名是%s，密码是%s" % (username,password))
