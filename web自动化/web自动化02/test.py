from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.find_element_by_xpath('div[@class="chat-input-tool"]').send_keys('今天的天气怎么样')
# driver.find_element_by_xpath('button[@id="chat-submit-button"]').click()
sleep(3)
driver.quit()

