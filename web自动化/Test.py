#导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#打开浏览器
driver = webdriver.Chrome()

#进入百度网站
driver.get('https://www.baidu.com/')
sleep(3)
#查找搜索框元素
search = driver.find_element(By.NAME, 'wd')
sleep(3)
#输入搜索内容
search.send_keys("Runoob")
sleep(3)
#模拟回车
search.send_keys(Keys.RETURN)

#等待3秒
sleep(3)

#关闭 quit()
driver.quit()