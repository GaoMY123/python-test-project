import random

def main():
  #循环3次
  for i in range(3):
    a=int(input("请输入您的选择：1-3之间的整数（1-剪刀，2-石头，3-布）："))
    b=random.randint(1,3)
    print("电脑选择了",b)
    if a==b:
        print("平局")
    elif a==1 and b==2:
        print("电脑赢了")
    elif a==1 and b==3:
        print("您赢了")
    elif a==2 and b==1:
        print("您赢了")
    elif a==2 and b==3:
        print("电脑赢了")
    elif a==3 and b==1:
        print("电脑赢了")
    elif a==3 and b==2:
        print("您赢了")
    else:
        print("输入错误，请重新输入")
if __name__ =='__main__':
    main()
