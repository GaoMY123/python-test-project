from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, time=10, poll=0.1):
        return WebDriverWait(self.driver, time, poll).until(
            lambda x: x.find_element(*feature)
        )

    def find_elements(self, feature, time=10, poll=0.1):
        WebDriverWait(self.driver, time, poll).until(
            EC.presence_of_element_located(feature)
        )
        return self.driver.find_elements(*feature)

    def click(self, feature, time=10, poll=0.1):
        self.find_element(feature, time, poll).click()

    def send_keys(self, feature, text, time=10, poll=0.1):
        self.find_element(feature, time, poll).send_keys(text)

    def clear(self, feature, time=10, poll=0.1):
        self.find_element(feature, time, poll).clear()

    def get_text(self, feature, time=10, poll=0.1):
        return self.find_element(feature, time, poll).text

    def get_attribute(self, feature, name, time=10, poll=0.1):
        return self.find_element(feature, time, poll).get_attribute(name)

    def switch_to_frame(self, feature, time=10, poll=0.1):
        frame = self.find_element(feature, time, poll)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()