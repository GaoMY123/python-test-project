from selenium import webdriver
from time  import sleep
#连接驱动
driver=webdriver.Chrome()
#打开注册
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
userA=driver.find_element_by_name('userA')
userA.send_keys('admin')
passwordA=driver.find_element_by_name('passwordA')
passwordA.send_keys('123456')
sleep(5)
driver.quit()