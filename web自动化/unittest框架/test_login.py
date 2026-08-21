import unittest
from selenium import webdriver
from time import sleep



class TestLogin(unittest.TestCase):
    def setUp(self):
        """
        初始化
        连接驱动
        打开浏览器
        将页面最大化
        隐式等待
        :return:
        """
        self.driver=webdriver.Chrome()
        self.driver.get('http://info.ybbms.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        """
        结束
        关闭
        :return:
        """
        sleep(3)
        self.driver.quit()
    def test_case1(self):
        """
        登陆成功后的用例
        :return:
        """
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('mobile').send_keys('15296797153')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
        assert self.driver.find_element_by_id('nick_name').text=='123456'
        print("登录成功")
    def test_case2(self):
        """
        登录失败的用例
        :return:
        """
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('mobile').send_keys('15296797153')
        self.driver.find_element_by_id('password').send_keys('12345')
        self.driver.find_element_by_xpath('//input[@value="登 录"]').click()

        try:
            self.driver.switch_to.alert().accept()
        except:
            print("登录失败")
        # raise Exception#会产生一个异常E
        # assert False#断言失败，会产生F

if __name__ == '__main__':
    unittest.main()
