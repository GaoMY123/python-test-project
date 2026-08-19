"""
关闭浏览器quit和close
quit：关闭所有浏览器窗口
close：关闭当前浏览器窗口
"""
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#点击打开新窗口
driver.find_element_by_link_text('打开新窗口').click()
sleep(2)
#关闭当前浏览器的窗口
# driver.close()
#关闭所有浏览器的窗口
driver.quit()
