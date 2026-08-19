"""

"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#点击打开新窗口
driver.find_element_by_link_text("打开新窗口").click()

#获取当前窗口的句柄
current=driver.current_window_handle
print(current)

#获取所有窗口句柄

handles=driver.window_handles
#切换窗口 窗口的id(句柄)
driver.switch_to.window(handles[-1])
#输入账号adminB
sleep(3)
driver.find_element_by_id("userB").send_keys("adminB")
sleep(3)
driver.quit()
