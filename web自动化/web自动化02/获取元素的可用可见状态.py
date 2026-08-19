"""
打开注册A界面
获取音乐A按钮的可用状态
获取span标签的可见状态
"""

from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#获取音乐A的可用状态
print(driver.find_element_by_id('yyA').is_enabled())
#获取span标签的可见状态
print(driver.find_element_by_xpath('//span[@style="visibility: hidden;"]').is_displayed())
sleep(3)
driver.quit()
