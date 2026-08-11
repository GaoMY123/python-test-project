def main():
    age=input("请输入您的年龄：")
    if int(age)>=18:
        print("可以进入网吧")
        money=float(input("请输入您的余额："))
        if money >=10:
            print("余额充足，可以上网")
            seat()
        else:
            print("余额不足，请充值")
            recharge()
    else:
        print("您未成年，不能进入网吧")
def recharge():
    money=float(input("请输入要充值的金额："))
    if money>0:
        print("充值成功")
        print("祝您上网愉快")
        print("您的余额为：",money)
        seat()
    else:
        print("充值金额错误，请重新输入")
        recharge()
def seat():
    chair=int(input("请选择您的座位："))
    if 1<=chair<100:
        print("您选择了座位",chair)
        print("祝您上网愉快！")
    else:
        print("座位号错误，请重新输入：")
        seat()
if __name__ =='__main__':
    main()
