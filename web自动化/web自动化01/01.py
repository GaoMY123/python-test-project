#test
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# sleep(3)
# driver.quit()

# #注册
#
# from selenium import webdriver
# from time import sleep
#
# #id 定位
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# userA=driver.find_element_by_id('userA').send_keys('admin')
# driver.find_element_by_id('passwordA').send_keys('123456')
# sleep(3)
# driver.quit()
#name定位
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_name('userA').send_keys('admin')
# driver.find_element_by_name('passwordA').send_keys('123456')
# sleep(3)
# driver.quit()
#class定位
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_class_name('telA').send_keys('18611111111')
# driver.find_element_by_class_name('emailA').send_keys('123@qq.com')
# sleep(3)
# driver.quit()
#tag_name定位
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_tag_name('input').send_keys('admin')
# sleep(3)
# driver.quit()
#test
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# sleep(3)
# driver.quit()

# #注册
#
# from selenium import webdriver
# from time import sleep
#
# #id 定位
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# userA=driver.find_element_by_id('userA').send_keys('admin')
# driver.find_element_by_id('passwordA').send_keys('123456')
# sleep(3)
# driver.quit()
#name定位
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_name('userA').send_keys('admin')
# driver.find_element_by_name('passwordA').send_keys('123456')
# sleep(3)
# driver.quit()
#class定位
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_class_name('telA').send_keys('18611111111')
# driver.find_element_by_class_name('emailA').send_keys('123@qq.com')
# sleep(3)
# driver.quit()
#tag_name定位
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
driver.find_element_by_tag_name('input').send_keys('admin')
sleep(3)
driver.quit()
