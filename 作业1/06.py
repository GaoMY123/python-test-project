'''
制作用户登录系统：已知A用户注册的用户名为 aaa，密码是 123456 。具体要求如下：

登录时需要验证用户名、密码、验证码(固定验证码为 qwer )。

提示：系统先验证验证码是否正确，正确后再验证用户名和密码。
'''
def main():
    code=input("请输入您的验证码：")
    if code=="qwer":
          username = input("请输入您的用户名：")
          password = input("请输入您的密码：")
          if username=="aaa" and password=="123456":
            print("登陆成功")
          else:
            print("用户名或者密码错误")
    else:
        print("验证码错误")
if __name__=="__main__":
    main()