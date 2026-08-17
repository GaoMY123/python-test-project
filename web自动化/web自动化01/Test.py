#导包
from selenium import webdriver
from time import sleep
#打开浏览器
driver=webdriver.Chrome()

#进入百度网站
driver.get('https://www.baidu.com/')
#等待3秒
sleep(10)

#关闭 quit()
driver.quit()