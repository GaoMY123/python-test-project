# #显式等待和隐式等待
# # """
# # 元素等待分为显示等待或者是隐式等待
# # 显示等待：使用WebDriverWait类来实现，需要指定等待的时间和条件，格式为：
# # WebDriverWait(driver, 10).until(条件函数)
# # 隐式等待：在创建WebDriver对象时，指定等待的时间，所有元素都必须等待指定的时间
# # 格式为：driver.implicitly_wait(10)
# #
# # """
# # from selenium import webdriver
# # from time import sleep
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.common.by import By
# #
# # driver=webdriver.Chrome()
# # driver.get('https://www.baidu.com')
# # sleep(2)
# # #使用显示等待,单个元素生效
# # wait=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 's-top-loginbtn')))
# # wait.click()
# # # driver.find_element_by_id('s-top-loginbtn').click()
# #
# # # driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('15133714567')
# # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__userName'))).send_keys('15133711234')
# # # WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('TANGRAM__PSP_11__password')).send_keys('15133715206')
# # # driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('123456')
# # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__password'))).send_keys('123456')
# # #勾选同意协议
# # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__isAgree'))).click()
# # #点击登录按钮
# # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__submit'))).click()
# # sleep(3)
# # driver.quit()
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#
# #使用显示等待
# # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('ddddd'))
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'ddddd')))
# driver.quit()
# """
# assert断言
# """
# username_sql="zs"
# password_sql="123456"
#
# username=input("请输入账号:")
# password=input("请输入密码:")
#
# assert username_sql==username and password_sql==password,"账号或密码错误"
# print("登录成功")
# """
# 登录成功和登录失败
# """
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome()
# driver.get('http://info.ybbms.com')
# driver.maximize_window()
# #使用隐式等待，登录成功
# driver.implicitly_wait(10)
# driver.find_element_by_link_text('登录').click()
# #输入账号
# driver.find_element_by_id('mobile').send_keys('15296797153')
# #输入密码
# driver.find_element_by_id('password').send_keys('123456')
# #点击登录
# driver.find_element_by_xpath('//input[@value="登 录"]').click()
# #确认登录成功
# assert driver.find_element_by_id('nick_name').text=="123456"
# print("登录成功")
# # sleep(3)
# # driver.quit()
# #使用显式等待，登录失败
# # WebDriverWait(driver,10).until(lambda x: x.find_element_by_link_text('登录')).click()
# # #输入账号
# # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('mobile')).send_keys('15296797153')
# # #输入密码
# # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('password')).send_keys('12345')
# # #点击登录
# # WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath('//input[@value="登 录"]')).click()
# # #登录失败，切换到警告框
# # # 使用EC.alert_is_present()等待alert出现，会正确处理异常
# # # alert = WebDriverWait(driver,10).until(EC.alert_is_present())
# # # alert.accept()
# # #会出现异常，所以要捕获或者抛出异常
# # try:
# #     wait=WebDriverWait(driver,10).until(lambda x: x.switch_to.alert())
# #     wait.accept()
# # except:
# #     print("登录失败")
# sleep(3)
# driver.quit()
# #方式一：使用open()函数
# # f=open('./a.txt',"w",encoding="utf-8")
# # f.write("hello world")
# # f.close()
# #方式二:使用with语句
# with open('./a.txt',"w",encoding="utf-8") as f:
#     f.write("hello world")
# """
# 隐式等待：driver.implicitly_wait(10)
# """
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
#
# driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#
# #添加隐式等待，在十秒内不会报错，如果十秒内元素没有加载完成，会报错，十秒内加载出来停止等待继续执行
# driver.implicitly_wait(10)
#
# #定位元素
# driver.find_element_by_id('ddddd')
#
# driver.quit()
# import unittest
#
# class TestLogout(unittest.TestCase):
#     def test_case1(self):
#         """
#
#         :return:
#         """
#         print('w我是退出成功')
#     def test_case2(self):
#         print('w我是退出失败')
# if __name__ == '__main__':
#     unittest.main()
# import unittest
# from selenium import webdriver
# from time import sleep
#
#
#
# class TestLogin(unittest.TestCase):
#     def setUp(self):
#         """
#         初始化
#         连接驱动
#         打开浏览器
#         将页面最大化
#         隐式等待
#         :return:
#         """
#         self.driver=webdriver.Chrome()
#         self.driver.get('http://info.ybbms.com/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#     def tearDown(self):
#         """
#         结束
#         关闭
#         :return:
#         """
#         sleep(3)
#         self.driver.quit()
#     def test_case1(self):
#         """
#         登陆成功后的用例
#         :return:
#         """
#         self.driver.find_element_by_link_text('登录').click()
#         self.driver.find_element_by_id('mobile').send_keys('15296797153')
#         self.driver.find_element_by_id('password').send_keys('123456')
#         self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
#         assert self.driver.find_element_by_id('nick_name').text=='123456'
#         print("登录成功")
#     def test_case2(self):
#         """
#         登录失败的用例
#         :return:
#         """
#         self.driver.find_element_by_link_text('登录').click()
#         self.driver.find_element_by_id('mobile').send_keys('15296797153')
#         self.driver.find_element_by_id('password').send_keys('12345')
#         self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
#
#         try:
#             self.driver.switch_to.alert().accept()
#         except:
#             print("登录失败")
#         # raise Exception#会产生一个异常E
#         # assert False#断言失败，会产生F
#
# if __name__ == '__main__':
#     unittest.main()
# """
# 1.收集用例
# 2.打开html文件
# 3.运行用例
# 4.收集结果
# 5.将结果写入html文件
# """
# import unittest
# from HTMLTestRunner import HTMLTestRunner
#
# if __name__ == '__main__':
#     suite=unittest.defaultTestLoader.discover('./', 'test_*.py')
#
#     with open('./report/test.html',"wb") as f:
#         # HTMLTestRunner(f).run(suite)
#         HTMLTestRunner(f,2,'测试报告','测试用例执行结果').run(suite)
#         """
#         1.创建test开头的测试文件
#         2.导入unittest模块
#         3.新建 TestLogin 类，并继承 unittest.TestCase
#         4.编写test_login_success 方法，打印 success
#         5.编写test_login_failed 方法，打印 failed
#         6.编写 main 入口，并将 “unittest.main()” 添加到程序入口中
#         """
#
#         import unittest
#         from test_login import TestLogin
#         from test_logout import TestLogout
#
#         if __name__ == '__main__':
#             # 收集用例
#             # 创建TestSuite对象
#             # 运行指定用例
#             # suite=unittest.TestSuite()
#             # #添加用例
#             # suite.addTest(TestLogin('test_case1'))
#             # suite.addTest(TestLogout('test_case1'))
#             # #创建TextTestRunner对象
#             # runner=unittest.TextTestRunner()
#             # #运行用例
#             # runner.run(suite)
#             # 运行所有用例
#             suite = unittest.defaultTestLoader.discover('./', 'test_*.py')
#             # 创建TextTestRunner对象
#             runner = unittest.TextTestRunner()
#             # 运行用例
#             runner.run(suite)
#
#             # 显式等待和隐式等待
#             # """
#             # 元素等待分为显示等待或者是隐式等待
#             # 显示等待：使用WebDriverWait类来实现，需要指定等待的时间和条件，格式为：
#             # WebDriverWait(driver, 10).until(条件函数)
#             # 隐式等待：在创建WebDriver对象时，指定等待的时间，所有元素都必须等待指定的时间
#             # 格式为：driver.implicitly_wait(10)
#             #
#             # """
#             # from selenium import webdriver
#             # from time import sleep
#             # from selenium.webdriver.support import expected_conditions as EC
#             # from selenium.webdriver.support.ui import WebDriverWait
#             # from selenium.webdriver.common.by import By
#             #
#             # driver=webdriver.Chrome()
#             # driver.get('https://www.baidu.com')
#             # sleep(2)
#             # #使用显示等待,单个元素生效
#             # wait=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 's-top-loginbtn')))
#             # wait.click()
#             # # driver.find_element_by_id('s-top-loginbtn').click()
#             #
#             # # driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('15133714567')
#             # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__userName'))).send_keys('15133711234')
#             # # WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('TANGRAM__PSP_11__password')).send_keys('15133715206')
#             # # driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('123456')
#             # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__password'))).send_keys('123456')
#             # #勾选同意协议
#             # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__isAgree'))).click()
#             # #点击登录按钮
#             # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__submit'))).click()
#             # sleep(3)
#             # driver.quit()
#             from selenium import webdriver
#             from time import sleep
#             from selenium.webdriver.common.by import By
#             from selenium.webdriver.support.wait import WebDriverWait
#             from selenium.webdriver.support import expected_conditions as EC
#
#             driver = webdriver.Chrome()
#             driver.get(
#                 'file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#
#             # 使用显示等待
#             # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('ddddd'))
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ddddd')))
#             driver.quit()
#             """
#             assert断言
#             """
#             username_sql = "zs"
#             password_sql = "123456"
#
#             username = input("请输入账号:")
#             password = input("请输入密码:")
#
#             assert username_sql == username and password_sql == password, "账号或密码错误"
#             print("登录成功")
#             """
#             登录成功和登录失败
#             """
#             from selenium import webdriver
#             from time import sleep
#
#             from selenium.webdriver.support.wait import WebDriverWait
#             from selenium.webdriver.support import expected_conditions as EC
#
#             driver = webdriver.Chrome()
#             driver.get('http://info.ybbms.com')
#             driver.maximize_window()
#             # 使用隐式等待，登录成功
#             driver.implicitly_wait(10)
#             driver.find_element_by_link_text('登录').click()
#             # 输入账号
#             driver.find_element_by_id('mobile').send_keys('15296797153')
#             # 输入密码
#             driver.find_element_by_id('password').send_keys('123456')
#             # 点击登录
#             driver.find_element_by_xpath('//input[@value="登 录"]').click()
#             # 确认登录成功
#             assert driver.find_element_by_id('nick_name').text == "123456"
#             print("登录成功")
#             # sleep(3)
#             # driver.quit()
#             # 使用显式等待，登录失败
#             # WebDriverWait(driver,10).until(lambda x: x.find_element_by_link_text('登录')).click()
#             # #输入账号
#             # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('mobile')).send_keys('15296797153')
#             # #输入密码
#             # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('password')).send_keys('12345')
#             # #点击登录
#             # WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath('//input[@value="登 录"]')).click()
#             # #登录失败，切换到警告框
#             # # 使用EC.alert_is_present()等待alert出现，会正确处理异常
#             # # alert = WebDriverWait(driver,10).until(EC.alert_is_present())
#             # # alert.accept()
#             # #会出现异常，所以要捕获或者抛出异常
#             # try:
#             #     wait=WebDriverWait(driver,10).until(lambda x: x.switch_to.alert())
#             #     wait.accept()
#             # except:
#             #     print("登录失败")
#             sleep(3)
#             driver.quit()
#             # 方式一：使用open()函数
#             # f=open('./a.txt',"w",encoding="utf-8")
#             # f.write("hello world")
#             # f.close()
#             # 方式二:使用with语句
#             with open('./a.txt', "w", encoding="utf-8") as f:
#                 f.write("hello world")
#             """
#             隐式等待：driver.implicitly_wait(10)
#             """
#             from selenium import webdriver
#             from time import sleep
#
#             driver = webdriver.Chrome()
#
#             driver.get(
#                 'file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#
#             # 添加隐式等待，在十秒内不会报错，如果十秒内元素没有加载完成，会报错，十秒内加载出来停止等待继续执行
#             driver.implicitly_wait(10)
#
#             # 定位元素
#             driver.find_element_by_id('ddddd')
#
#             driver.quit()
#             import unittest
#
#
#             class TestLogout(unittest.TestCase):
#                 def test_case1(self):
#                     """
#
#                     :return:
#                     """
#                     print('w我是退出成功')
#
#                 def test_case2(self):
#                     print('w我是退出失败')
#
#
#             if __name__ == '__main__':
#                 unittest.main()
#             import unittest
#             from selenium import webdriver
#             from time import sleep
#
#
#             class TestLogin(unittest.TestCase):
#                 def setUp(self):
#                     """
#                     初始化
#                     连接驱动
#                     打开浏览器
#                     将页面最大化
#                     隐式等待
#                     :return:
#                     """
#                     self.driver = webdriver.Chrome()
#                     self.driver.get('http://info.ybbms.com/')
#                     self.driver.maximize_window()
#                     self.driver.implicitly_wait(10)
#
#                 def tearDown(self):
#                     """
#                     结束
#                     关闭
#                     :return:
#                     """
#                     sleep(3)
#                     self.driver.quit()
#
#                 def test_case1(self):
#                     """
#                     登陆成功后的用例
#                     :return:
#                     """
#                     self.driver.find_element_by_link_text('登录').click()
#                     self.driver.find_element_by_id('mobile').send_keys('15296797153')
#                     self.driver.find_element_by_id('password').send_keys('123456')
#                     self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
#                     assert self.driver.find_element_by_id('nick_name').text == '123456'
#                     print("登录成功")
#
#                 def test_case2(self):
#                     """
#                     登录失败的用例
#                     :return:
#                     """
#                     self.driver.find_element_by_link_text('登录').click()
#                     self.driver.find_element_by_id('mobile').send_keys('15296797153')
#                     self.driver.find_element_by_id('password').send_keys('12345')
#                     self.driver.find_element_by_xpath('//input[@value="登 录"]').click()
#
#                     try:
#                         self.driver.switch_to.alert().accept()
#                     except:
#                         print("登录失败")
#                     # raise Exception#会产生一个异常E
#                     # assert False#断言失败，会产生F
#
#
#             if __name__ == '__main__':
#                 unittest.main()
#             """
#             1.收集用例
#             2.打开html文件
#             3.运行用例
#             4.收集结果
#             5.将结果写入html文件
#             """
#             import unittest
#             from HTMLTestRunner import HTMLTestRunner
#
#             if __name__ == '__main__':
#                 suite = unittest.defaultTestLoader.discover('./', 'test_*.py')
#
#                 with open('./report/test.html', "wb") as f:
#                     # HTMLTestRunner(f).run(suite)
#                     HTMLTestRunner(f, 2, '测试报告', '测试用例执行结果').run(suite)
#                     """
#                     1.创建test开头的测试文件
#                     2.导入unittest模块
#                     3.新建 TestLogin 类，并继承 unittest.TestCase
#                     4.编写test_login_success 方法，打印 success
#                     5.编写test_login_failed 方法，打印 failed
#                     6.编写 main 入口，并将 “unittest.main()” 添加到程序入口中
#                     """
#
#                     import unittest
#                     from test_login import TestLogin
#                     from test_logout import TestLogout
#
#                     if __name__ == '__main__':
#                         # 收集用例
#                         # 创建TestSuite对象
#                         # 运行指定用例
#                         # suite=unittest.TestSuite()
#                         # #添加用例
#                         # suite.addTest(TestLogin('test_case1'))
#                         # suite.addTest(TestLogout('test_case1'))
#                         # #创建TextTestRunner对象
#                         # runner=unittest.TextTestRunner()
#                         # #运行用例
#                         # runner.run(suite)
#                         # 运行所有用例
#                         suite = unittest.defaultTestLoader.discover('./', 'test_*.py')
#                         # 创建TextTestRunner对象
#                         runner = unittest.TextTestRunner()
#                         # 运行用例
#                         runner.run(suite)