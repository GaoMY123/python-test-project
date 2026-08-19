"""
浏览器的操作：回退、前进、刷新
输入账号admin，然后再点击刷新
"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)


#输入账号admin
driver.find_element_by_id("userA").send_keys("admin")
#刷新
sleep(2)
driver.refresh()

#点击打开注册B界面
driver.find_element_by_link_text('打开B页面').click()

#回退
sleep(2)
driver.back()

#前进
sleep(2)
driver.forward()

sleep(3)
driver.quit()