import unittest
from selenium import webdriver
from time import sleep
from page.login_page import LoginPage
from page.home_page import HomePage
from base.base_action import BaseAction
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://info.ybbms.com/')
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        #创建实例化对象
        self.login_page=LoginPage(self.driver)
        self.home_page=HomePage(self.driver)


    def tearDown(self):
        sleep(3)
        self.driver.quit()


    def test_case1(self):
        """
        登陆成功
        :return:
        """
        #定位元素
        #点击登录
        # self.driver.find_element_by_link_text('登录').click()
        self.home_page.click_login()
        #输入账号
        # self.driver.find_element_by_id('mobile').send_keys('15296797153')
        self.login_page.input_mobile('15296797153')
        #输入密码
        # self.driver.find_element_by_id('password').send_keys('123456')
        self.login_page.input_password('123456')
        #点击登录
        # self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
        self.login_page.click_login()
        #断言
        # assert self.driver.find_element_by_id('nick_name').text=='123456'
        # print("登录成功")
        assert self.home_page.get_username()=='123456'
    def test_case2(self):
        """
        登录失败
        :return:
        """
        # self.driver.find_element_by_link_text('登录').click()
        self.home_page.click_login()
        # 输入账号
        # self.driver.find_element_by_id('mobile').send_keys('15296797153')
        self.login_page.input_mobile('15296797153')
        # 输入密码
        # self.driver.find_element_by_id('password').send_keys('12345')
        self.login_page.input_password('12345')
        # 点击登录
        # self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
        self.login_page.click_login()
        # 断言
        # try:
        #     self.driver.switch_to.alert.accept()
        # except:
        #     print("登录失败")
        assert self.login_page.get_alert()=='用户名或者密码错误'
if __name__ == '__main__':
    unittest.main()