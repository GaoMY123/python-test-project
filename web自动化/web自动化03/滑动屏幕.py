"""
打开注册A页面
滑动到最下面
"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(3)
#编写js脚本
js="window.scrollTo(0,2000)"
#执行js脚本
driver.execute_script(js)

sleep(3)
driver.quit()
