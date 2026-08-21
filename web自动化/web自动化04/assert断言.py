"""
assert断言
"""
username_sql="zs"
password_sql="123456"

username=input("请输入账号:")
password=input("请输入密码:")

assert username_sql==username and password_sql==password,"账号或密码错误"
print("登录成功")
