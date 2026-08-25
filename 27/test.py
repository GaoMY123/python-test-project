# 27.需求:对《注册实例.html》进行信息注册账号:admin，密码:123456，电话:18600000000，
# 电子邮件:123@qq.com要求:1.对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
# 2.定位方式不限3.暂停3秒钟关闭浏览器4.可以不使用PO模式
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#打开注册实例页面
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
#主界面注册信息填写
driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('tel').send_keys('18600000000')
driver.find_element_by_id('email').send_keys('123@qq.com')
#切换到注册A的iframe
driver.switch_to.frame('myframe1')
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
driver.find_element_by_id('telA').send_keys('18600000000')
driver.find_element_by_id('emailA').send_keys('123@qq.com')
driver.switch_to.default_content()
#切换到注册B的iframe
driver.switch_to.frame('myframe2')
driver.find_element_by_id('userB').send_keys('admin')
driver.find_element_by_id('passwordB').send_keys('123456')
driver.find_element_by_id('telB').send_keys('18600000000')
driver.find_element_by_id('emailB').send_keys('123@qq.com')
driver.switch_to.default_content()
#暂停3秒钟关闭浏览器
sleep(3)
driver.quit()
