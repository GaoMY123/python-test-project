import unittest
from selenium import webdriver
from time import sleep
from page.baidu_page import BaiduPage, Hao123Page, BaiduResultPage


class TestBaidu(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.baidu_page = BaiduPage(self.driver)

    def tearDown(self):
        sleep(3)
        self.driver.quit()
    #
    def test_search_guoqing(self):
        # 点击左上角的“hao123”
        self.baidu_page.click_hao123()
        # 切换到 hao123 新窗口
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

        hao123_page = Hao123Page(self.driver)
        hao123_page.input_search('国庆节')
        hao123_page.click_search()

        # 搜索结果页在新窗口打开，再次切换窗口
        sleep(2)
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

        result_page = BaiduResultPage(self.driver)
        titles, matched_title = result_page.get_check_result('国庆节', '-百度百科')
        passed = matched_title is not None
        if not titles:
            print('没有获取到任何搜索结果')
        elif matched_title:
            print(matched_title)
        else:
            print('未找到同时包含"国庆节"和"-百度百科"的标题')
        self.assertTrue(passed, '搜索结果标题中未同时包含"国庆节"和"-百度百科"')


if __name__ == '__main__':
    unittest.main()
