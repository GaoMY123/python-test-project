import unittest
from selenium import webdriver
from time import sleep
from page.qqmail_page import QQMailPage
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
        self.driver.maximize_window()
        self.qqmail_page = QQMailPage(self.driver)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_login(self):
        #登录在iframe中，需要切换
        #先切换为父级iframe
        self.qqmail_page.switch_to_frame((By.CSS_SELECTOR, "iframe[title='QQ登录']"))
        #再切换为自己iframe
        self.qqmail_page.switch_to_frame((By.ID, "ptlogin_iframe"))
        #点击密码登录
        self.qqmail_page.click_password_login()
        #输入用户名
        self.qqmail_page.input_username('1911802840')
        #输入密码
        self.qqmail_page.input_password('123456')
        #点击登录
        self.qqmail_page.click_login()


if __name__ == '__main__':
    unittest.main()