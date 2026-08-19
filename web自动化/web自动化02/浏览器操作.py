"""
打开注册A界面
将浏览器最大化
设置大小600，600
设置位置300,300
"""
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#最大化
driver.maximize_window()
sleep(3)
#设置大小
driver.set_window_size(600,600)
sleep(3)
#设置位置
driver.set_window_position(600,300)
sleep(3)
driver.quit()