#代码的语法格式本身没有问题，但是在某些情况下运行还是会报错
#语法错误：代码的语法格式本身就有问题，运行一定会报错
li=['a','b','c']
print(li[10])#IndexError
#KeyError
data={'name':'张三','age':18}
print(data['age'])
print(data['age1'])
#ZeroDivisionError
def demo(x,y):
    print(x/y)
demo(2,0)
#FileNotFoundError
f=open('./aaa.txt',mode='r',encoding='utf-8')
