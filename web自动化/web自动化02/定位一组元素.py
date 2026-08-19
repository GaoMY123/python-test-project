"""
打开注册A界面
使用tag_name定位密码框
定位一组元素和单个元素的区别
定位一组元素：
语法driver.find_elements_by_xxx()
如果有多个符合条件的元素通过列表返回所有的元素
如果没有找到元素则返回空列表
定位单个元素：
语法:driver.find_element_by_xxx()
如果有多个符合条件的元素只会返回第一个元素
如果没有找到元素则会报错NoSuchElementException
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
inputs=driver.find_elements(By.TAG_NAME,'input')
# print(inputs)
inputs[1].send_keys('123456')
sleep(3)
driver.quit()
