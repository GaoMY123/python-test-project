from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#定位注册用户A按钮
button=driver.find_element_by_xpath('//button')
#获取文本 注册用户A
print(button.text)
#获取大小
print(button.size)
#获取title属性值 加入会员A
print(button.get_attribute('title'))
#获取位置
print(button.location)
sleep(2)
driver.quit()