# """
# 元素等待分为显示等待或者是隐式等待
# 显示等待：使用WebDriverWait类来实现，需要指定等待的时间和条件，格式为：
# WebDriverWait(driver, 10).until(条件函数)
# 隐式等待：在创建WebDriver对象时，指定等待的时间，所有元素都必须等待指定的时间
# 格式为：driver.implicitly_wait(10)
#
# """
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# sleep(2)
# #使用显示等待,单个元素生效
# wait=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 's-top-loginbtn')))
# wait.click()
# # driver.find_element_by_id('s-top-loginbtn').click()
#
# # driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('15133714567')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__userName'))).send_keys('15133711234')
# # WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('TANGRAM__PSP_11__password')).send_keys('15133715206')
# # driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('123456')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__password'))).send_keys('123456')
# #勾选同意协议
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__isAgree'))).click()
# #点击登录按钮
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__submit'))).click()
# sleep(3)
# driver.quit()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')

#使用显示等待
# WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('ddddd'))
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'ddddd')))
driver.quit()
