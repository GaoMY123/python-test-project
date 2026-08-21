"""
隐式等待：driver.implicitly_wait(10)
"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')

#添加隐式等待，在十秒内不会报错，如果十秒内元素没有加载完成，会报错，十秒内加载出来停止等待继续执行
driver.implicitly_wait(10)

#定位元素
driver.find_element_by_id('ddddd')

driver.quit()