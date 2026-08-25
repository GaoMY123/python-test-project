from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建webdriver对象
driver = webdriver.Chrome()
# 打开百度
driver.get('https://www.baidu.com/')
#将页面最大化
driver.maximize_window()
sleep(2)
# 使用显式等待，等待搜索框元素可交互后再操作
# 百度搜索框的 id 是 'kw'，比 name 更稳定

search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'kw'))
)

# 在其中输入Runoob
try:
    search.send_keys("Runoob")
except Exception as e:
    #输出错误类型
    print(e)
# 模拟回车
search.send_keys(Keys.RETURN)

sleep(3)
driver.quit()