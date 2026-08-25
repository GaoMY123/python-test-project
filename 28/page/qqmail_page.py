from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class QQMailPage(BaseAction):
    password_login_btn = (By.ID, 'switcher_plogin')
    username_input = (By.ID, 'u')
    password_input = (By.ID, 'p')
    login_btn = (By.ID, 'login_button')

    def click_password_login(self):
        self.click(self.password_login_btn)

    def input_username(self, username):
        self.send_keys(self.username_input, username)

    def input_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_btn)