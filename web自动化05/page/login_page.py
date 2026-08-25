
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_action import BaseAction
class LoginPage(BaseAction):
    #提取元素的特征,是为了省略掉索引，使代码更简洁易读
    mobile_feature =By.ID,'mobile'
    password_feature=By.ID,'password'
    login_feature=By.XPATH,'//input[@value="登 录"]'
    # def __init__(self,driver):
    #     self.driver=driver
    #输入账号
    def input_mobile(self,mobile):
        # self.driver.find_element(*self.mobile_feature).send_keys(mobile)
        # self.find_element(self.mobile_feature).send_keys(mobile)
        self.send_keys(self.mobile_feature,mobile)
    #输入密码
    def input_password(self,password):
        # self.driver.find_element(*self.password_feature).send_keys(password)
        # self.find_element(self.password_feature).send_keys(password)
        self.send_keys(self.password_feature,password)
    #点击登录
    def click_login(self):
        # self.driver.find_element(*self.login_feature).click()
        # self.find_element(self.login_feature).click()
        self.click(self.login_feature)
    #获取警告框
    def get_alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        return alert.text