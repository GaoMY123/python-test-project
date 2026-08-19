"""
鼠标的操作：点击、悬停，双击
打开注册A页面
点击账号框，输入账号admin
双击账号框，右击账号框
"""
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
#
# #创建ActionChains类对象
# action=ActionChains(driver)
# #定位账号框
# userA=driver.find_element_by_id("userA")
# action.click(userA).perform()
# userA.send_keys('admin')
# #右击账号框
# action.context_click(userA).perform()
# #双击账号框
# action.double_click(userA).perform()
# sleep(3)
# driver.quit()
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#创建ActionChains类对象
action=ActionChains(driver)
#定位账号框
userA=driver.find_element_by_id("userA")
#点击账号框
action.click(userA).perform()
#输入账号
userA.send_keys('admin')
#右击账号框
action.context_click(userA).perform()
#双击账号框
action.double_click(userA).perform()

sleep(3)
driver.quit()