def main():
  age=input("请输入你的年龄：")
  if int(age) >=18:
    print("可以进入网吧")
    print("欢迎光临")
  else:
    print("不能进入网吧")
    print("回家吧，你还是太小了")
  score=input("请输入你的成绩：")
  if int(score) >=90:
    print("你是一个好学生")
  elif int(score)>=80 and int(score)<90:
      print("一般")
  elif int(score) >=60 and int(score)<80:
      print("很一般")
  elif  int(score)<=60 and int(score)>=0:
      print("差")
  else:
      print("输入错误")




if __name__ == '__main__':
    main()

