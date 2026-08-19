"""
打开注册A页面
点击click for prompt按钮
输入123456
"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(3)
#点击click for prompt按钮
driver.find_element_by_xpath('//input[@value="Click For Prompt"]').click()
#切换警告框
sleep(1)
prompt=driver.switch_to.alert
#输入123546
sleep(2)
prompt.send_keys('123546')
#点击确定
prompt.accept()

sleep(3)
driver.quit()

