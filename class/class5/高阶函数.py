#map()函数，可以将列表按照指定规则生成一个新的列表
# 需求1：将以下列表输出位["1","2","3"]
import re
from functools import reduce
li=[1,2,3]
# def demo(x):
#     return str(x)
# li1=list(map(demo,li))
# print(li1)
# li2=[]
# for i in li:
#     li2.append(str(i))
# print(li2)
demo=list(map(lambda x:str(x),li))
print(demo)
#需求二：将以下列表输出位[1,4,9]
# li3=[]
# for i in li:
#     li3.append(i**2)
# print(li3)
# def demo1(x):
#     return x**2
# li4=list(map(demo1,li))
# print(li4)
# x=[1,2,3,4,5]
# doubled=list(map(lambda x:x*2,x))
# print(doubled)
demo1=list(map(lambda x:x**2,li))
print(demo1)
#需求三：将以下列表输出为['Hello','Hi','Itfeat']
li5=['Hello','hi','Itfeat']
# def demo2(x):
#     return x.capitalize()
# li6=list(map(demo2,li5))
# print(li6)
demo2=list(map(lambda x:x.capitalize(),li5))
print(demo2)
#filter()函数，可以将列表按照指定规则筛选出符合条件的元素
#需求1：将以下列表输出为[2,6]
li=[1,2,6,7,9]
def demo(x):
    return x%2==0
li1=list(filter(demo,li))
print(li1)
demo1=list(filter(lambda x:x%2==0,li))
print(demo1)
#需求2：将以下列表输出为["Hello","Itfeat"]
# def demo2(x):
#     return re.match(r'[A-Z]',x)
# li2=list(filter(demo2,li5))
# print(li2)
# def demo2(x):
#     return x==x.capitalize()
# li2=list(filter(demo2,li5))
# print(li2)
# demo = list(filter(lambda x:x==x.capitalize(),li5))
# print(demo)
# def demo2(x):
#     return x[0].isupper()
# li2=list(filter(demo2,li5))
# print(li2)
demo2=list(filter(lambda x:x[0].isupper(),li5))
print(demo2)
# reduce()函数，将容器中的元素进行累计
li=[1,2,3,4,5]
# print(sum(li))
# def demo3(x,y):
#     return x+y
# print(reduce(demo3,li))
print(reduce(lambda x,y:x+y,li))
