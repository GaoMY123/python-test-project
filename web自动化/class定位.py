from selenium import webdriver
from time import sleep
#打开页面
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#定位电话
telA=driver.find_element_by_class_name('telA')

#输入电话
telA.send_keys('18611111111')

#点击邮件
emailA=driver.find_element_by_class_name('emailA')

#输入邮件
emailA.send_keys('123@qq.com')

sleep(3)
driver.quit()

