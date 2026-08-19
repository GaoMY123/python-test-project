"""
css定位元素

"""



from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get('file:///F:/%E5%9F%B9%E8%AE%AD/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(2)
#定位click for prompt按钮
# driver.find_element_by_css_selector('[value="Click For Prompt"]').click()
driver.find_element(By.CSS_SELECTOR,'[value="Click For Prompt"]').click()
sleep(3)
driver.quit()
