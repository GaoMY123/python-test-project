"""
打开注册实例界面
输入注册用户账号admin
输入注册用户A账号adminA
输入注册用户B账号adminB
"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
sleep(3)

#输入注册用户账号admin
driver.find_element_by_id("user").send_keys("admin")
#切换到注册用户A
driver.switch_to.frame('myframe1')
#输入注册用户A账号adminA   填写frame的id，name，index，webElement
driver.find_element_by_id('userA').send_keys("adminA")
#返回默认框架
driver.switch_to.default_content()
#切换注册用户B
driver.switch_to.frame('myframe2')
#输入注册用户B账号adminB
driver.find_element_by_id('userB').send_keys("adminB")

sleep(3)
driver.quit()
