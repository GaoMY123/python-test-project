'''
案例：
打开注册A界面
点击访问新浪网站
等待三秒进行关闭
'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
driver_link=driver.find_element_by_link_text('访问 新浪 网站')
driver_link.click()
time.sleep(3)
driver.quit()
