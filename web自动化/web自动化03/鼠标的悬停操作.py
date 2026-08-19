"""
鼠标悬停操作：加载被隐藏元素
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(2)
#创建ActionChains类对象
action=ActionChains(driver)
#将鼠标悬停在设置上
action.move_to_element(driver.find_element_by_id("s-usersetting-top")).perform()
#点击搜索设置
action.click(driver.find_element_by_link_text("搜索设置")).perform()

sleep(3)
driver.quit()