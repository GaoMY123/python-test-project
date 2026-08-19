from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#输入账号
driver.find_element_by_id('userA').send_keys('admin')
#输入密码
driver.find_element_by_id('passwordA').send_keys('123456')
#输入电话号码
telA=driver.find_element_by_id('telA')
telA.send_keys('186111111111')
#输入邮箱
driver.find_element_by_id('emailA').send_keys('123@qq.com')
#清空电话号码
sleep(2)
telA.clear()
#重新输入电话号码
sleep(2)
telA.send_keys('15133715260')
#点击注册按钮
driver.find_element_by_xpath('//button[@type="submitA"]').click()

sleep(3)
driver.quit()
