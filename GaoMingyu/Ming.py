def main():
  #元组和列表的区别：
  #元组的元素不能被修改，列表的元素可以被修改
  #元组的元素可以是任意类型，列表的元素可以是任意类型
  #元组的元素可以是元组，列表的元素可以是元组
  #元组的元素可以是列表，列表的元素可以是元组
  #元组的元素可以是字典，列表的元素可以是字典
  #元组的元素可以是集合，列表的元素可以是集合
  #元组的元素可以是字符串，列表的元素可以是字符串
  mytuple=("apple","banana","orange")#元组的顺序是不可变的，创建之后不能添加或者删除项，可以被索引访问
  print(mytuple[0])
  mytuple = ("apple", "banana", "orange","apple")#元组的元素可以重复,因为有索引
  #使用len函数确认元组的长度
  print(len(mytuple))
  num = 18
  s = float(num)
  print(s)
  print(type(s))
  l = float(num)
  print(l)
  print(type(l))
  s = str(num)
  print(type(s))
  print(s)
  a = 48
  b = 45
  s = 'a+b'
  print(eval(s))  # 注意：eval()函数只能用于执行简单的表达式，不能用于执行复杂的语句或函数
  # 比较运算符
  a = 10
  b = 20
  print(a == b)
  print(a != b)
  print(a > b)
  print(a < b)
  print(a >= b)
  print(a <= b)
  # 逻辑运算符
  a = 10
  b = 20
  c = 30
  print(a == b and b == c)
  print(a >= b or b <= c)
  print(not a == b)
  print(not a == b and b == c)
  print(not (a == b and b == c))
  # if判断语句
  age = input("请输入你的年龄：")
  if int(age) >= 18:
    print("可以进入网吧")
    print("欢迎光临")
  else:
    print("不能进入网吧")
    print("回家吧，你还是太小了")
  score = input("请输入你的成绩：")
  if int(score) >= 90:
    print("你是一个好学生")
  elif int(score) >= 80 and int(score) < 90:
    print("一般")
  elif int(score) >= 60 and int(score) < 80:
    print("很一般")
  elif int(score) <= 60 and int(score) >= 0:
    print("差")
  else:
    print("输入错误")
  # if的三目运算符
  a = "apple"
  b = "apple"
  c = "banana"
  print(a if a == b else b)
  print(c if a != c else a)
  a = 10
  b = 20
  print(a if a > b else b)
  print(b if a > b else a)
  # if语句的嵌套
  age = input("请输入您的年龄：")
  if int(age) >= 18:
    print("可以进入网吧")
    money = float(input("请输入您的余额："))
    if money >= 10:
      print("余额充足，可以上网")
      seat()
    else:
      print("余额不足，请充值")
      recharge()
  else:
    print("您未成年，不能进入网吧")


def recharge():
  money = float(input("请输入要充值的金额："))
  if money > 0:
    print("充值成功")
    print("祝您上网愉快")
    print("您的余额为：", money)
    seat()
  else:
    print("充值金额错误，请重新输入")
    recharge()


def seat():
  chair = int(input("请选择您的座位："))
  if 1 <= chair < 100:
    print("您选择了座位", chair)
    print("祝您上网愉快！")
  else:
    print("座位号错误，请重新输入：")
    seat()
  # 猜拳游戏
  # 循环3次
  for i in range(3):
    a = int(input("请输入您的选择：1-3之间的整数（1-剪刀，2-石头，3-布）："))
    b = random.randint(1, 3)
    print("电脑选择了", b)
    if a == b:
      print("平局")
    elif a == 1 and b == 2:
      print("电脑赢了")
    elif a == 1 and b == 3:
      print("您赢了")
    elif a == 2 and b == 1:
      print("您赢了")
    elif a == 2 and b == 3:
      print("电脑赢了")
    elif a == 3 and b == 1:
      print("电脑赢了")
    elif a == 3 and b == 2:
      print("您赢了")
    else:
      print("输入错误，请重新输入")
    # while循环
    i = 2
    while i < 101:
      print("当前循环的次数为：", i)
      i += 2
    print("循环结束")
    z = 2
    s = 2
    while s % z == 0 and s <= 100:
      print(s)
      s = s + 2

    i = 1
    sum = 0
    while i <= 100:
      sum = sum + i
      i += 1
    print("1到100的和为:", sum)
    # 打印1到100之间所有偶数的和
    i = 2
    sum = 0
    while i <= 100:
      sum = sum + i
      i = i + 2
    print("1到100之间所有偶数的和为:", sum)
    z = 2
    s = 2
    sum = 0
    while s % z == 0 and s <= 100:
      sum = sum + s
      s = s + 2
    print("1到100之间所有偶数的和为:", sum)
    # 打印1到100之间所有奇数的和
    i = 1
    sum = 0
    while i <= 100:
      sum = sum + i
      i += 2
    print("1到100之间所有奇数的和为:", sum)
    z = 2
    s = 1
    sum = 0
    while s % z != 0 and s <= 100:
      sum = sum + s
      s = s + 2
    print("1到100之间所有奇数的和为:", sum)

if __name__=='__main__':
    main()
