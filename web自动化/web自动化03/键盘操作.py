"""
键盘操作
command是mac系统
control是windows系统
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#输入账号admin
userA=driver.find_element_by_id("userA")
userA.send_keys("admin")
#删除
sleep(3)
userA.send_keys(Keys.BACKSPACE)

#全选账号
userA.send_keys(Keys.CONTROL,"a")
#复制账号
userA.send_keys(Keys.CONTROL,"c")
#粘贴到密码框
passwordA=driver.find_element_by_id('passwordA')
passwordA.send_keys(Keys.CONTROL,"v")

sleep(3)
driver.quit()


