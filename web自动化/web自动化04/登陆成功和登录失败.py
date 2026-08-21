"""
登录成功和登录失败
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('http://info.ybbms.com')
driver.maximize_window()
#使用隐式等待，登录成功
driver.implicitly_wait(10)
driver.find_element_by_link_text('登录').click()
#输入账号
driver.find_element_by_id('mobile').send_keys('15296797153')
#输入密码
driver.find_element_by_id('password').send_keys('123456')
#点击登录
driver.find_element_by_xpath('//input[@value="登 录"]').click()
#确认登录成功
assert driver.find_element_by_id('nick_name').text=="123456"
print("登录成功")
# sleep(3)
# driver.quit()
#使用显式等待，登录失败
# WebDriverWait(driver,10).until(lambda x: x.find_element_by_link_text('登录')).click()
# #输入账号
# WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('mobile')).send_keys('15296797153')
# #输入密码
# WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('password')).send_keys('12345')
# #点击登录
# WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath('//input[@value="登 录"]')).click()
# #登录失败，切换到警告框
# # 使用EC.alert_is_present()等待alert出现，会正确处理异常
# # alert = WebDriverWait(driver,10).until(EC.alert_is_present())
# # alert.accept()
# #会出现异常，所以要捕获或者抛出异常
# try:
#     wait=WebDriverWait(driver,10).until(lambda x: x.switch_to.alert())
#     wait.accept()
# except:
#     print("登录失败")
sleep(3)
driver.quit()