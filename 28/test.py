from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#跳过自动化检测提示
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.baidu.com")
#最大化窗口
driver.maximize_window()
#隐式等待
driver.implicitly_wait(10)
#点击左上角的“hao123”
driver.find_element_by_link_text("hao123").click()
#获取所有窗口的句柄
all_handles=driver.window_handles
#切换到最新的窗口句柄
driver.switch_to.window(all_handles[-1])

# 定位搜索框
search_box = driver.find_element(By.CSS_SELECTOR, "[data-hook='searchInput']")
# 在搜索框中输入文字
search_box.send_keys("国庆节")
#定位百度一下
search_btn=driver.find_element(By.XPATH, '//input[@value="百度一下"]')
#点击百度一下
search_btn.click()
#搜索结果在新窗口，切换,获取所有窗口的句柄,切换到最新的窗口句柄
sleep(2)
all_handles=driver.window_handles
driver.switch_to.window(all_handles[-1])
#获取所有搜索结果的标题,
result_titles=driver.find_elements(By.XPATH, '//h3/a')
for title in result_titles:
#判断所有标题中是否包含“国庆节”和“-百度百科”，去掉空格后判断
    if "国庆节" in title.text.replace(" ", "") and "-百度百科" in title.text.replace(" ", ""):
        print(title.text)
        break
    else:
        continue

sleep(3)
driver.quit()
