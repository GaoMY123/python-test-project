"""
元素定位的最佳实践
1：优先使用id，name等唯一属性定位元素
2.避免使用动态属性：如果元素的属性是动态生成的（如随机Id），避免直接使用这些属性定位
3.使用相对定位:使用xpath或者css选择器结合元素的层级关系定位
4.添加等待机制：使用隐式等待或者显示等待确保元素加载完成后再进行操作

"""
#find_element_by_id()

#find_element_by_name()

#find_element_by_class_name()

#find_element_by_tag_name()

#find_element_by_css_selector()

#find_element_by_xpath()

#find_element_by_link_text()

#find_element_by_partial_link_text()

#定位多个元素
#find_elements
# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
sleep(2)
driver.get('https://www.example.com')
sleep(2)
#通过ID定位输入框并输入文本
username=driver.find_element(By.ID,'username')
username.send_keys('testuser')

#通过Name定位并输入文本
password=driver.find_element(By.NAME,'password')
password.send_keys('password123')

#通过CSS选择器定位按钮并点击
driver.find_element(By.CSS_SELECTOR,'button.submit-btn').click()
#通过xpath定位按钮并点击
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
#关闭浏览器
driver.quit()