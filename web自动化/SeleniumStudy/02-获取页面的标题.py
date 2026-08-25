

from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()

#使用显示等待，等待页面加载完场后再操作
# wait=WebDriverWait(driver, 10).until(
#     EC.title_is('百度一下，你就知道')
# )


driver.get('https://www.baidu.com/')
sleep(2)
#将页面最大化
driver.maximize_window()
sleep(2)
#强制停止页面加载:有时候一个网页加载时间比较长会导致异常的出现，为了能够顺利抓取数据
#可以让页面加载几秒后再通过执行JavaScript代码window.stop()来强制停止页面加载。
# driver.execute_script('window.stop()')
# sleep(2)
#获取页面的标题
print(driver.title)

#
sleep(3)
driver.quit()
