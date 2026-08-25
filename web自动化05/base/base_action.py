#封装元素的定位方法
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,feature,time=10,poll=0.1):
        # return self.driver.find_element(*feature)
        #使用显示等待
        # return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(feature))
        return WebDriverWait(self.driver,time,poll).until(lambda x:x.find_element(*feature))
    def click(self,feature,time=10,poll=0.1):
        self.find_element(feature,time,poll).click()
    def send_keys(self,feature,text,time=10,poll=0.1):
        self.find_element(feature,time,poll).send_keys(text)
    def clear(self,feature,time=10,poll=0.1):
        self.find_element(feature,time,poll).clear()
    #获取文本值
    def get_text(self,feature,time=10,poll=0.1):
        return self.find_element(feature,time,poll).text
    def get_attribute(self,feature,name,time=10,poll=0.1):
        return self.find_element(feature,time,poll).get_attribute(name)
