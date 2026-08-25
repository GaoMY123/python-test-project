# 脚本1：打开qq邮箱，https://mail.qq.com/，用qq进行登录,输入用户名，密码点击登录后即可
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
driver.maximize_window()

# 等页面JS完全初始化（页面先显示密码登录→JS切换为快捷登录）
sleep(5)
#切换到父级的iframe
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='QQ登录']"))
)
print("已切换到外层 iframe (title='QQ登录')")
#然后切换到子级的iframe
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "ptlogin_iframe"))
)
# 等待"密码登录"链接变为可点击状态（此时JS已切换完毕）
wait = WebDriverWait(driver, 15)
password_login = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '密码登录')))
password_login.click()

# 输入用户名
username = wait.until(EC.presence_of_element_located((By.ID, 'u')))
username.send_keys("2879677705")

# 输入密码
password = wait.until(EC.presence_of_element_located((By.ID, 'p')))
password.send_keys("123456")

# 点击登录
login_btn = wait.until(EC.element_to_be_clickable((By.ID, 'login_button')))
login_btn.click()

# 等待登录完成
sleep(3)
driver.quit()