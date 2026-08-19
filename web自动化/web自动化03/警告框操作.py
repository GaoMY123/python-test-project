# """
# 弹窗：alert弹窗，只有确定按钮
#      confirm弹窗，有确定和取消
#      prompt弹窗：有确定、有取消。有输入框
# """
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
# #定位click for confirm按钮
#
# driver.find_element_by_xpath('//input[@value="Click For Confirm"]').click()
# sleep(2)
# #切换警告框
# confirm=driver.switch_to.alert
# #获取文本
# print(confirm.text)
# #点击确定
# sleep(2)
# confirm.accept()
# #点击取消
# # confirm.dismiss()
#
# sleep(3)
# driver.quit()

from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#将浏览器最大化
driver.maximize_window()
#定位click for confirm按钮
driver.find_element_by_xpath('//input[@value="Click For Confirm"]').click()
#切换警告框
confirm=driver.switch_to.alert
sleep(3)
#获取文本
print(confirm.text)
#点击确定
sleep(2)
# confirm.accept()
#点击取消
confirm.dismiss()
sleep(3)
driver.quit()
