#匿名函数
#lambda 参数列表：表达式
#无参数无返回值：
# def demo():
#     print(10)
demo=lambda :print(10)
demo()
#无参数有返回值
# def demo1():
#     return 10
demo1=lambda :10
print(demo1())
#有参数无返回值
# def demo2(n):
#     print("和为:",n)
demo2=lambda n:print("和为:",n)
print(demo2(10))
#有参数有返回值
# def demo3(a,b):
#     return a+b
demo3=lambda a,b:a+b
print(demo3(1,2))
