#先导包
from selenium import webdriver
from time import sleep

#设置实例化对象
driver=webdriver.Chrome()
#打开runoob.com网址
driver.get('https://www.runoob.com/')
sleep(2)
#最大化窗口
driver.maximize_window()
#获取页面标题和URL
print(driver.title)
print(driver.current_url)
#导航到另一个页面
sleep(2)
driver.get('https://www.baidu.com/')
sleep(2)
#返回上一个页面
driver.back()
#刷新页面
sleep(2)
driver.refresh()
sleep(2)
#关闭浏览器
driver.quit()
