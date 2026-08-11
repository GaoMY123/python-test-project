

#
def main():
    print("hello world")
    test()
def test():
    print("test")
#信息可以作为参数传递到函数当中
#可以添加任意多个函数，参数在函数名称确认之后、括号内指定，可以添加任意多个参数，用逗号分隔即可
def test2(s):
    print(s+"Refsnes")
test2("张三")
def test3(fname,lname):
    print(fname," ",lname)
test3("张珊珊","爱丽丝")
#默认参数
def test4(name,id=18):
    print(name,id)
test4('张三',20)
test4('李四')
#关键词参数,可以使用=值发送参数
def test5(animal,name):
    print(f"I have a {animal}")
    print(f"My {animal}'s name is {name}")
test5(animal="dog",name='Buddy')
test5(name='wangcai',animal="dog")
#位置参数,顺序关键
test5("dog","wangcai")
#混合位置参数和关键字参数,位置参数必须在关键字参数之前
test5("dog",name="goudan")
#传递不同的数据类型
#可以传递字符串、数字、列表、元组、字典、集合等
def my_function(fruits):
    for fruits in fruits:
        print(fruits)
my_fruits=["apple","orange","banana","peach"]#列表
my_function(my_fruits)
#发送字典作为参数
def my_function2(person):
    print("name",person["name"])
    print("age",person["age"])
    print("city",person["city"])
my_person={"name":"张三","age":18,"city":"北京"}
my_function2(my_person)
#可以使用return语句返回值
def my_function3(x,y):
    return x*y
result=my_function3(10,20)
print(result)
#返回列表的函数
def my_function4(x,y):
    return[x,y]
result=my_function4(10,20)
print(result)
#返回元组的函数
def my_function5(x,y):
    return x,y
result=my_function5(10,20)
print(result)
print(type(result))
#任意参数，不知道有多少参数传递到函数当中，可以使用*号表示
def my_function6(*kids):
    print("The youngest child is " + kids[2])
my_function6("张三","王四","李五")
def my_function7(*args):
    print("Type:",type(args))
    print("First argument:",args[0])
    print("Second argument:",args[1])
    print("All arguments:",args)
my_function7("zhangsan","lisi","wangwu")
#使用*args与常规参数混合,常规参数必须在*args之前
def my_function8(greeting,*name):
    for x in name:
        print(greeting,x)
my_function8("hello","张三","李四","王五",18)
#计算任意数量之和
def my_function9(*nums):
    sum=0
    for x in nums:
        sum=sum+x
    return sum
print(my_function9(1, 2, 3, 4, 5))
print(my_function9(1.3,25,36))
#找出任意参数值中的最大值
def my_function10(*nums):
    if len(nums)==0:
        return None
    max=nums[0]
    for x in nums:
        if x>max:
            max=x
    return max
print(my_function10(5,3,98,456,22,4566.23))
#添加两个关键字参数,**kwargs,函数返回一个参数字典并访问相应的项目
#**kwargs参数和*args参数的区别：*args参数用于传递任意数量的非关键字参数，**kwargs参数用于传递任意数量的关键字参数
def my_function11(**kids):
    print("His last name is"+kids["lname"])
my_function11(fname="张三",lname="爱丽丝")
#**kwargs参数允许一个函数接受任意数量的关键字参数，参数名和参数值之间用=号分隔
def my_function12(**kwargs):
    print("type:",type(kwargs))
    print("Name:",kwargs["name"])
    print("Age:",kwargs["age"])
    print("All data:",kwargs)
my_function12(name="Tobias",age=18,city="北京")
#组合*args和**kwargs,必须按照常规参数、*args、**kwargs顺序
def my_function13(title,*args,**kwargs):
    print("Title:",title)
    print("First argument:",args[0])
    print("Second argument:",args[1])
    print("Third argument:",kwargs["age"])
    print("All arguments:",kwargs)
my_function13("Hello","张三","李四","王五",age=18,city="北京")
#解包参数和解压字典
def my_function14(a,b,c):
    return a+b+c
numbers=[1,2,3]
print(my_function14(*numbers))#和 my_function14(1,2,3)效果一样
def my_function15(fname,lname):
    print("Hello",fname,lname)
person={"fname":"张三","lname":"李四"}
my_function15(**person)
#全局参数和局部参数，局部参数只能在函数内部使用，全局参数可以在函数内部和外部使用
def myfunc():
    a=10#局部变量
    def myinnerfunc():
        print(a)
    myinnerfunc()#等于print(a)
myfunc()
#print(a)会报错，因为a是局部变量，只能在函数内部使用，不能在函数外部使用
# 全局变量
x=45
def myfunc2():
    print(x)
    def myinnerfunc2():
        print(x)
    myinnerfunc2()
myfunc2()
#如果在函数内部要创建一个全局关键字，需要再函数内部使用global关键字
def myfunc3():
    global x
    x=100
    print(x)
myfunc3()
print(x)
#非局部关键字,nonlocal关键字:用于在嵌套函数中修改外部函数的变量
#在嵌套函数中使用nonlocal关键字，可以修改外部函数的变量
def myfunc4():
    x="Jane"
    def myfunc5():
        nonlocal x
        x="hello"
        print(x)
    myfunc5()
    print(x)
print(myfunc4())
#在查找变量名称是遵循legb规则，并按照以下顺序搜索：
#1.本地 2.封装 3.全局 4.内置
# python的装饰器：可以为函数添加额外的功能，而不改变函数的代码，他是一个函数，接收另一个函数作为输入并返回一个新的函数
#生成一个具有大写功能的装饰器
def mydecorator(func):
    def myinner(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return myinner
@mydecorator#装饰器
def myfunc6():#被调用的函数
    return "hello"
@mydecorator#装饰器
def myfunc7():#被调用的函数
    return "world"
@mydecorator#装饰器
def myfunc8():
    return "python"
print(myfunc6())
print(myfunc7())
print(myfunc8())
#函数需要参数的也可以被装饰，只需确保将参数传递给包装函数即可
@mydecorator
def hefunc(nam):
    return "hello"+nam
print(hefunc("John"))
#有时候装饰器函数无法控制被装饰函数传入的参数，为了解决这个问题，在包装函数中添加（*args，**kwargs）
#这样包装函数就可以接受任意数量和类型的参数，并将他们传递给被装饰函数
#装饰器可以通过添加另一个包装层来接受自己的参数
#装饰器工厂，接受一个参数并根据参数值转换大小写
def changecase(n):
  def changecase(func):
    def myinner(*args,**kwargs):
        if n==1:
            return func(*args,**kwargs).upper()
        else:
            return func(*args,**kwargs).lower()
    return myinner
  return changecase
@changecase(1)
def myfuncc(nam):
    return "Hello John"+nam
print(myfuncc("John"))
#多重装饰器
@changecase(1)
@changecase(2)
def myfuncc2(nam):
    return "lisa "+nam
print(myfuncc2("John"))
#保留功能元数据_name_,_doc_,当一个函数被装饰器装饰后，它的元数据会丢失，为了保留元数据，需要在装饰器中添加以下代码：
#functools.wraps,导入该函数保留原始函数名的文档字符串
#lambda()函数，可以创建小的匿名函数，但是只能有一个表达式，不能有多个语句，语法：lambda 参数1:表达式
x=lambda x:x+2#Lambda函数可以接受任意数量的参数，但是只能有一个表达式，不能有多个语句
print(x(5))
x=lambda a,b,c:a+b*c
print(x(1,2,3))
#为什么使用lambda函数？
#lambda在使用他们作为另一个函数中的匿名函数时表现更为明显
def myfunc9(n):
    return lambda a:a*n
x=myfunc9(2)
print(x(11))
#Lambda函数通常与内置函数map()、filter()和sorted()结合使用
#定义一个排序函数,倒序排序
def myfunc10(numbers):
    return sorted(numbers,reverse=True)
print(myfunc10([3,1,2]))
#map()函数将一个函数应用于可迭代对象中的每一个元素
x=[1,2,3,4,5]
doubled=list(map(lambda x:x*2,x))
print(doubled)
#filter()函数创建一个列表，其中包含一个函数返回True的类型
number=[1,2,3,4,5,6,7,8,9,10]
#过滤出列表中的奇数
odd_numbers=list(filter(lambda x:x%2!=0,number))
print(odd_numbers)
#函数的递归,递归是函数调用自身的一种用法，可以通过循环遍历数据的到结果
#从5开始倒计时
def myfunc11(n):
    if n<=0:
        print("none")
    else:
        print(n)
        myfunc11(n-1)
myfunc11(5)
#不用函数实现，用循环实现倒计时
for i in range(5,0,-1):
    print(i)
#每个递归函数都有两个部分，基本情况和递归情况，没有基本情况，递归函数将无限循环，导致栈溢出
#识别基本情况和基本情况
def factorial(n):
    #基本情况
    if n==0 or n==1:
        return 1
    #递归情况
    else:
        return n*factorial(n-1)
print(factorial(5))
#斐波那契数列
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))#找到第五个变量
#不用函数完成斐波那契数列
a=[0,1]
for i in range(2,10):#将i的取值从2开始到9结束
    s=a[i-1]+a[i-2]
    a.append(s)
    print(a)
#递归可用于通过逐个处理元素来处理列表
#计算列表中元素的总和
def myfunc12(n):
    if len(n)==0:
        return 0
    else:
        return n[0]+myfunc12(n[1:])
my_list=[1,2,3,4,5]
print(myfunc12(my_list))
#找到列表中的最大值
#max()函数返回可迭代对象中的最大值
def myfunc13(n):
    if len(n)==0:
        return False
    else:
        # return max(n[0],myfunc13(n[1:]))
        return n[0] if n[0]>myfunc13(n[1:]) else myfunc13(n[1:])
my_list1=[1,2,3,45,68,9*8,56]
print(myfunc13(my_list1))
#递归的深度限制，默认限制是1000，可以使用sys.setrecursionlimit()函数来增加限制，但是可能导致崩溃
# import sys
# sys.setrecursionlimit(2000)
#生成器函数：生成器函数是一种特殊的函数，返回一个迭代器对象，可以用于遍历一个序列，如列表、元组、字符串、字典等
#生成器函数的语法与普通函数类似，但是使用yield语句而不是return语句
#生成器函数的返回值是一个迭代器对象，而不是一个具体的值
#生成器函数的内存占用小，因为它们只在需要时才计算下一个值，而不是在函数调用时就计算所有值
def my_generator():
    yield 1
    yield 2
    yield 3
#调用生成器函数
for i in my_generator():
    print(i)
#生成器允许遍历数据，而无需将所有的数据加载到内存当中
#yield与return不同，return会终止函数，而yield会暂停它，可以多次调用
def count_up_to(n):#生成器，产生数字
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
#生成器内存效率高，因为他们在需要时动态生成值，而不是将所有内容都存储在内存中
#大型序列生成器
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
#next()函数可以用于获取生成器的下一个值，如果生成器没有更多值了，会抛出StopIteration异常
# 使用next()函数手动遍历生成器
def simple_gen():
    yield "Email"
    yield "Phone"
    yield "Address"
z=simple_gen()#创建一个生成器对象
print(next(z))
print(next(z))
print(next(z))
try:
    print(next(z))
except StopIteration:
    print("生成器没有更多值了")
z.close()#关闭生成器
#生成器表达式
#列表推导式与生成器表达式
list_comp=[i *i for i in range(1,10)]
print(list_comp)
gen_comp=(i*i for i in range(1,10))
print(gen_comp)
#send()和close()方法，send()方法可以向生成器发送数据，close()方法可以关闭生成器

if __name__ =='__main__':
    main()

