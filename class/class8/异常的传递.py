def demo1(x,y):
    print(x/y)
def demo2(a,b):
    demo1(a,b)
try:
    demo2(2,0)
except ZeroDivisionError :
    print('除数不能为0')
#在开发中，可以在主函数中增加异常捕获而在主函数中调用的其他函数，
# 因为Python中的异常是可以传递的，所有只要出现异常，
# 都会传递到主函数的异常捕获中这样就不需要在代码中，增加大量的异常捕获，能够保证代码的整洁。