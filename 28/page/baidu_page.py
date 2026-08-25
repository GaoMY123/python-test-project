from base.base_action import BaseAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BaiduPage(BaseAction):
    hao123_link = (By.LINK_TEXT, 'hao123')

    def click_hao123(self):
        self.click(self.hao123_link)


class Hao123Page(BaseAction):
    search_box = (By.CSS_SELECTOR, "[data-hook='searchInput']")
    search_btn = (By.XPATH, '//input[@value="百度一下"]')

    def input_search(self, keyword):
        self.send_keys(self.search_box, keyword)

    def click_search(self):
        self.click(self.search_btn)


class BaiduResultPage(BaseAction):
    result_links = (By.XPATH, '//h3/a')

    def get_all_result_titles(self):
        # 没有搜索结果时返回空列表，不直接报错
        try:
            elements = self.find_elements(self.result_links)
        except TimeoutException:
            return []
        return [el.text for el in elements]

    def get_check_result(self, *keywords):
        titles = self.get_all_result_titles()
        if not titles:
            return titles, None
        for title in titles:
            # 去掉空格后判断，兼容“国庆节 - 百度百科”和“国庆节-百度百科”
            normalized = ''.join(title.split())
            if all(keyword in normalized for keyword in keywords):
                return titles, title
        return titles, None

    def is_title_contains(self, *keywords):
        return self.get_check_result(*keywords)[1] is not None
