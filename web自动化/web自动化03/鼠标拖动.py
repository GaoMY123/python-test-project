"""
鼠标拖动操作
打开drag页面
将红色中方形拖动到蓝色正方形上面
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/drag.html')
#创建ActionChains类对象
action=ActionChains(driver)
#定位红色正方形
red_square=driver.find_element_by_id("div1")
#定位蓝色正方形
blue_square=driver.find_element_by_id("div2")
#将红色正方形移动到蓝色正方形上方
action.drag_and_drop(red_square,blue_square).perform()

sleep(3)
driver.quit()