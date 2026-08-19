"""
打开注册A页面
使用下标选择重庆
使用value选择北京
使用文本选择上海
被封装在select标签中
select_by_index:根据下标进行选择
select_by_value:根据value属性进行选择
select_by_visible_text:根据文本进行选择
弹窗：alert弹窗，只有确定按钮
     confirm弹窗，有确定和取消
     prompt弹窗：有确定、有取消。有输入框

"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
#定位下拉框
selectA=driver.find_element_by_id('selectA')
#创建Select类对象
select=Select(selectA)
#选择重庆
select.select_by_index(3)
sleep(2)
#选择广州
select.select_by_value('gz')
sleep(3)
#选择上海
select.select_by_visible_text('A上海')
sleep(3)
driver.quit()
