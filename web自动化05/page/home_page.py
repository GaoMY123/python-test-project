from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class HomePage(BaseAction):
    #提取元素的特征
    login_feature=By.LINK_TEXT,'登录'
    username_feature=By.ID,'nick_name'
    # def __init__(self,driver):
    #     self.driver=driver
    #点击登录
    def click_login(self):
        # self.driver.find_element(*self.login_feature).click()
        # self.find_element(self.login_feature).click()
        self.click(self.login_feature)
    #获取用户名
    def get_username(self):
        # return self.driver.find_element(*self.username_feature).text
        # return self.find_element(self.username_feature).text
        return self.get_text(self.username_feature)
