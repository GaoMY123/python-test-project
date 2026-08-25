# # #浏览器操作
# # from selenium import webdriver
# # from time import sleep
# # driver=webdriver.Chrome()
# # driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# # sleep(3)
# # # 输入账号admin
# # driver.find_element_by_id('userA').send_keys('admin')
# # #刷新
# # sleep(2)
# # driver.refresh()
# # #点击打开注册B界面
# # driver.find_element_by_link_text('打开B页面').click()
# # #回退
# # sleep(2)
# # driver.back()
# # #前进
# # sleep(2)
# # driver.foward()
# # sleep(3)
# # driver.quit()
# #截图与验证码处理
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #截图
# driver.save_screenshot('screenshot.png')
#
# sleep(3)
# driver.quit()
#滑动屏幕
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #编写js脚本
# js='window.scrollTo(0,5000)'
# #执行js脚本
# driver.execute_script(js)
# sleep(3)
# driver.quit()
#自动登录
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# sleep(3)
#
# #使浏览器最大化
# driver.maximize_window()
# sleep(3)
#
# #点击登录
# driver.add_cookie({"name":"BDUSS","value":"lTQUtzZkZvcWFFTktTWlh4cTQxNVRYdFR3TUw0Q1ItVzU2Y0pPc0xmN1JlSUpxRVFBQUFBJCQAAAAAAQAAAAEAAABGbYWGc2pqamRkZNauuOgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANHrWmrR61pqYX",})
# sleep(3)
# #刷新界面
# driver.refresh()
#
# sleep(5)
# driver.quit()
#多窗口
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
#
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #点击打开新窗口
# driver.find_element_by_link_text('打开新窗口').click()
# #获取当前窗口的句柄
# print(driver.current_window_handle)
# #获取所有窗口的句柄
# handles=driver.window_handles
# #切换窗口 窗口的id(句柄)
# driver.switch_to.window(handles[1])
# #输入账号adminB
# driver.find_element_by_id('userB').send_keys('adminB')
# sleep(3)
# driver.quit()
#获取标题和地址
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #获取标题
# print(driver.title)
# #获取地址
# print(driver.current_url)
# sleep(3)
# driver.quit()
#警告框操作
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
# #将浏览器最大化
# driver.maximize_window()
# sleep(2)
# #定位click for confirm按钮
# driver.find_element_by_link_text('click for confirm').click()
# sleep(2)
# #切换警告框
# confirm=driver.switch_to.alert
# sleep(3)
# #获取文本
# print(confirm.text)
# #点击确认
# confirm.accept()
# sleep(3)
# #点击取消
# confirm.dismiss()
# sleep(3)
# driver.quit()
#警告框输入
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
#
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #点击click for prompt按钮
# driver.find_element_by_xpath('//input[@value="click for prompt"]').click()
# #切换警告框
# sleep(1)
# prompt=driver.switch_to.alert
# #输入123456
# prompt.send_keys('123456')
# #点击确定
# prompt.accept()
# sleep(3)
# driver.quit()
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
# #点击打开新窗口
# driver.find_element_by_link_text('打开新窗口').click()
# sleep(2)
# #关闭当前浏览器的窗口
# driver.close()
# #关闭所有浏览器的窗口
# driver.quit()
#下拉框
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# #定位下拉框
# selectA=driver.find_element_by_id('selectA')
# #创建Select类对象
# select=Select(selectA)
# #选择重庆
# select.select_by_index(3)
# sleep(3)
# #选择广州
# select.select_by_value('gz')
# #选择上海
# select.select_by_visible_text('A上海')
# sleep(3)
# driver.quit()
#frame
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
# sleep(3)
# #输入注册用户账号admin
# driver.find_element_by_id("user").send_keys("admin")
# #切换到注册用户A
# driver.switch_to.frame('myframe1')
# # 输入注册用户A账号adminA
# driver.find_element_by_id('userA').send_keys("adminA")
# #返回默认框架
# driver.switch_to.default_content()
# #切换注册用户B
# driver.switch_to.frame('myframe2')
# #输入注册用户b账号adminB
# driver.find_element_by_id('userB').send_keys("adminB")
#
# sleep(3)
# driver.quit()
#键盘操作
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #输入账号admin
# userA=driver.find_element_by_id("userA")
# userA.send_keys('admin')
# sleep(3)
# userA.send_keys(Keys.BACKSPACE)
# # driver.quit()
# #全选账号
# userA.send_keys(Keys.CONTROL,'a')
# #复制账号
# userA.send_keys(Keys.CONTROL,'c')
# #粘贴到密码框
# passwordA=driver.find_element_by_id("passwordA")
# passwordA.send_keys(Keys.CONTROL,'v')
#
# sleep(3)
# driver.quit()
#鼠标拖动
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# #创建ActionChains类对象
# action=ActionChains(driver)
# #定位红色正方形
# red=driver.find_element_by_id('div1')
# #定位蓝色正方形
# blue=driver.find_element_by_id('div2')
# #将红色正方形拖到蓝色正方形上方
# action.drag_and_drop(red,blue).perform()
#
# sleep(3)
# driver.quit()
#鼠标的悬停操作
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# sleep(2)
# #创建ActionChains类对象
# action=ActionChains(driver)
# #将鼠标悬停在设置上
# action.move_to_element(driver.find_element_by_id("s-usersetting-top")).perform()
# #点击搜索设置
# action.click(driver.find_element_by_link_text("搜索设置")).perform()
#
# sleep(3)
# driver.quit()
#鼠标的操作
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
# #创建ActionChains类对象
# action=ActionChains(driver)
# #定位账号框
# userA=driver.find_element_by_id("userA")
# #点击账号框
# action.click(userA).perform()
# #输入账号
# userA.send_keys('admin')
# #右击账号框
# action.context_click(userA).perform()
# #双击账号框
# action.double_click(userA).perform()
#
# sleep(3)
# driver.quit()
# # #浏览器操作
# # from selenium import webdriver
# # from time import sleep
# # driver=webdriver.Chrome()
# # driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# # sleep(3)
# # # 输入账号admin
# # driver.find_element_by_id('userA').send_keys('admin')
# # #刷新
# # sleep(2)
# # driver.refresh()
# # #点击打开注册B界面
# # driver.find_element_by_link_text('打开B页面').click()
# # #回退
# # sleep(2)
# # driver.back()
# # #前进
# # sleep(2)
# # driver.foward()
# # sleep(3)
# # driver.quit()
# #截图与验证码处理
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #截图
# driver.save_screenshot('screenshot.png')
#
# sleep(3)
# driver.quit()
#滑动屏幕
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #编写js脚本
# js='window.scrollTo(0,5000)'
# #执行js脚本
# driver.execute_script(js)
# sleep(3)
# driver.quit()
#自动登录
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# sleep(3)
#
# #使浏览器最大化
# driver.maximize_window()
# sleep(3)
#
# #点击登录
# driver.add_cookie({"name":"BDUSS","value":"lTQUtzZkZvcWFFTktTWlh4cTQxNVRYdFR3TUw0Q1ItVzU2Y0pPc0xmN1JlSUpxRVFBQUFBJCQAAAAAAQAAAAEAAABGbYWGc2pqamRkZNauuOgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANHrWmrR61pqYX",})
# sleep(3)
# #刷新界面
# driver.refresh()
#
# sleep(5)
# driver.quit()
#多窗口
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
#
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #点击打开新窗口
# driver.find_element_by_link_text('打开新窗口').click()
# #获取当前窗口的句柄
# print(driver.current_window_handle)
# #获取所有窗口的句柄
# handles=driver.window_handles
# #切换窗口 窗口的id(句柄)
# driver.switch_to.window(handles[1])
# #输入账号adminB
# driver.find_element_by_id('userB').send_keys('adminB')
# sleep(3)
# driver.quit()
#获取标题和地址
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #获取标题
# print(driver.title)
# #获取地址
# print(driver.current_url)
# sleep(3)
# driver.quit()
#警告框操作
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
# #将浏览器最大化
# driver.maximize_window()
# sleep(2)
# #定位click for confirm按钮
# driver.find_element_by_link_text('click for confirm').click()
# sleep(2)
# #切换警告框
# confirm=driver.switch_to.alert
# sleep(3)
# #获取文本
# print(confirm.text)
# #点击确认
# confirm.accept()
# sleep(3)
# #点击取消
# confirm.dismiss()
# sleep(3)
# driver.quit()
#警告框输入
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
#
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #点击click for prompt按钮
# driver.find_element_by_xpath('//input[@value="click for prompt"]').click()
# #切换警告框
# sleep(1)
# prompt=driver.switch_to.alert
# #输入123456
# prompt.send_keys('123456')
# #点击确定
# prompt.accept()
# sleep(3)
# driver.quit()
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(2)
# #点击打开新窗口
# driver.find_element_by_link_text('打开新窗口').click()
# sleep(2)
# #关闭当前浏览器的窗口
# driver.close()
# #关闭所有浏览器的窗口
# driver.quit()
#下拉框
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# #定位下拉框
# selectA=driver.find_element_by_id('selectA')
# #创建Select类对象
# select=Select(selectA)
# #选择重庆
# select.select_by_index(3)
# sleep(3)
# #选择广州
# select.select_by_value('gz')
# #选择上海
# select.select_by_visible_text('A上海')
# sleep(3)
# driver.quit()
#frame
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
# sleep(3)
# #输入注册用户账号admin
# driver.find_element_by_id("user").send_keys("admin")
# #切换到注册用户A
# driver.switch_to.frame('myframe1')
# # 输入注册用户A账号adminA
# driver.find_element_by_id('userA').send_keys("adminA")
# #返回默认框架
# driver.switch_to.default_content()
# #切换注册用户B
# driver.switch_to.frame('myframe2')
# #输入注册用户b账号adminB
# driver.find_element_by_id('userB').send_keys("adminB")
#
# sleep(3)
# driver.quit()
#键盘操作
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# sleep(3)
# #输入账号admin
# userA=driver.find_element_by_id("userA")
# userA.send_keys('admin')
# sleep(3)
# userA.send_keys(Keys.BACKSPACE)
# # driver.quit()
# #全选账号
# userA.send_keys(Keys.CONTROL,'a')
# #复制账号
# userA.send_keys(Keys.CONTROL,'c')
# #粘贴到密码框
# passwordA=driver.find_element_by_id("passwordA")
# passwordA.send_keys(Keys.CONTROL,'v')
#
# sleep(3)
# driver.quit()
#鼠标拖动
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# #创建ActionChains类对象
# action=ActionChains(driver)
# #定位红色正方形
# red=driver.find_element_by_id('div1')
# #定位蓝色正方形
# blue=driver.find_element_by_id('div2')
# #将红色正方形拖到蓝色正方形上方
# action.drag_and_drop(red,blue).perform()
#
# sleep(3)
# driver.quit()
#鼠标的悬停操作
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# sleep(2)
# #创建ActionChains类对象
# action=ActionChains(driver)
# #将鼠标悬停在设置上
# action.move_to_element(driver.find_element_by_id("s-usersetting-top")).perform()
# #点击搜索设置
# action.click(driver.find_element_by_link_text("搜索设置")).perform()
#
# sleep(3)
# driver.quit()
#鼠标的操作
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#创建ActionChains类对象
action=ActionChains(driver)
#定位账号框
userA=driver.find_element_by_id("userA")
#点击账号框
action.click(userA).perform()
#输入账号
userA.send_keys('admin')
#右击账号框
action.context_click(userA).perform()
#双击账号框
action.double_click(userA).perform()

sleep(3)
driver.quit()