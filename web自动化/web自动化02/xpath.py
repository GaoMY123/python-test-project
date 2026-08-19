'''
xpath定位元素
案例：
打开注册A页面
使用xpath定位click for confirm按钮，并进行点击
等待三秒。进行关闭
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#定位click for confirm按钮
# confirm=driver.find_element_by_xpath('//input[@value="Click For Confirm"]')
# confirm.click()


driver.find_element_by_xpath('//input[@value="Click For Confirm"]').click()


sleep(3)
driver.quit()