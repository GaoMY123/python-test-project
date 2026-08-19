"""
自动登录
"""
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

sleep(3)

#使浏览器最大化
driver.maximize_window()
sleep(2)

#点击登录
driver.add_cookie({"name":"BDUSS","value":"lTQUtzZkZvcWFFTktTWlh4cTQxNVRYdFR3TUw0Q1ItVzU2Y0pPc0xmN1JlSUpxRVFBQUFBJCQAAAAAAQAAAAEAAABGbYWGc2pqamRkZNauuOgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANHrWmrR61pqYX"})

sleep(3)
driver.refresh()


sleep(5)
driver.quit()

