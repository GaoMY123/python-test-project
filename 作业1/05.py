'''
用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，并提示：您的年龄是xx: 青少年/青年/中年/老年。

年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。
'''
def main():
    age=int(input("请输入用户的年龄："))
    if 0<=age<=17:
        print(f'您的年龄是{age}，青少年')
    elif 18<=age<=35:
        print(f'您的年龄是{age}，青年')
    elif 36<=age<=59:
        print(f'您的年龄是{age}，中年')
    elif 60<=age<=99:
        print(f'您的年龄是{age}，老年')
    else:
        print("输入错误")
if __name__=="__main__":
    main()