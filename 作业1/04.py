#用户输入年龄，如果年龄超过65岁，输出："可以退休了"， 否则，输出："小伙子，加油干！"

def main():
    age=int(input("请输入用户的年龄："))
    if age>65:
        print("可以退休了")
    else:
        print("小伙子，加油干！")
if __name__=="__main__":
     main()
