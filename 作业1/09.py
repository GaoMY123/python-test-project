'''
请输入第一个数字:
请输入第二个数字:
请输入要进行的操作(+ - * /):
计算的结果为:
举例如下:
请输入第一个数字: 10
请输入第二个数字: 20
请输入要进行的操作(+ - * /): +
计算的结果为: 10 + 20 = 30

'''
def main():
    num1=float(input("请输入第一个数字："))
    num2=float(input("请输入第二个数字："))
    operator=input("请输入接下来要进行的操作（+ - * /）:")
    if operator=='+':
        print("计算的结果为",num1+num2)
        print(f"计算的结果为：{num1+num2}")
    elif operator=='-':
        print("计算的结果为",num1-num2)
        print(f"计算的结果为：{num1-num2}")
    elif operator=='*':
        print("计算的结果为",num1*num2)
        print(f"计算的结果为：{num1*num2}")
    elif operator=='/':
        print("计算的结果为",num1/num2)
        print(f"计算的结果为：{num1/num2}")
    else:
        print("输入错误")
if __name__=="__main__":
    main()

