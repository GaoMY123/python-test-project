'''
如何定义一个函数：def 函数名（）：
    函数体
    return 返回值
'''
def main():
    def demo():
        i=1
        sum=0
        while i<=100:
            if i %2==0:
                sum=sum+i
            i+=1
        print(sum)
    demo()
    #添加函数的文档说明,长摁ctrl 点击函数名，help（函数名）
    def demo1():
        '''
        这是一个函数，用于求1-100之间的偶数的和
        '''
        i=1
        sum=0
        while i<=100:
            if i %2==0:
              sum=sum+i
            i+=1
        print(sum)
    demo1()
    help(demo1)
    #函数的参数和返回值，参数分为形参和实参
    #形参：在函数定义时，定义的参数，用于接收实参
    #实参：在函数调用时，传递给函数的参数，用于替换形参
    #返回值：在函数执行完成后，将结果返回给调用者
    def demo2(a,b):
        return a+b
    print(demo2(1,2))
    #函数的嵌套调用
    #需求1：定义一个函数可以打印一行横线
    #需求2：定义一个函数可以打印自定义行数的横线
    def test1():
        print("----------")
    def test2():
        n=input("请输入要打印的行数:")
        for i in range(int(n)):
            test1()
    test2()
    #局部变量,定义在函数内部的变量，只能在函数内部使用
    def test3():
        a=10
        print(a)
    test3()
    #全局变量：定义在函数外部的变量,可以被多个函数调用
    a=100
    def test4():
        a=10
        print(a)
    test4()
    print(a)
    #global：在函数内部定义的变量，可以在函数外部使用
    #nonlocal：在函数内部定义的变量，可以在函数外部使用，在函数嵌套时使用
    def test5():
        nonlocal a
        a=1000
        print(a)
    print(a)
    test5()
    print(a)
    #拆包：将一个列表或者元组中的元素，分别赋值给多个变量
    l=[1,2,3,4,5]
    a,b,c,d,e=l
    print(a,b,c,d,e)
    #方式一：容器中有几个元素就找几个变量来接收
    #方式二：可以使用*号将容器中的元素接收
    a,b,*c=l
    print(a,b,c)
    #应用：将一个字典中的元素，分别赋值给多个变量
    data={"name":"张三","age":18,"sex":1}
    for l,v in data.items():
        print(l,v)
    #交换两个变量的值,方式一：
    a=1
    b=2
    c=a
    a=b
    b=c
    print(a,b)
    #方式二：
    a,b=b,a
    print(a,b)
    #方式三：两数相减
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
    #九九乘法表
    i=1
    while i<=9:
        j=1
        while j<=i:
            print(f"{j}*{i}={i*j}",end=" ")
            j+=1
        print()
        i+=1
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}*{i}={i*j}",end=' ')
        print()
    #位置参数：形参和实参的位置及顺序必须一致
    #关键字参数：调用函数时指定形参的名字进行传参
    #缺省值参数：在定义函数时给形参设置一个默认值，当调用函数时，如果没有传递实参，会使用默认值，如果有传递实参，会使用实参
    #不定长位置参数：调用函数传入位置参数的个数不确定，一般用*args表示，默认返回元组的数据类型
    #不定长关键字参数：调用函数传入关键字参数的个数不确定，一般用**kwargs表示，默认返回字典的数据类型
    def demo6(*args,**kwargs):
        print(args)
        print(kwargs)
    demo6(1,2,3,4,5,a=1,b=2,c=3)
    #函数的的引用某个变量在内存中的指向
    #id(变量名)：查看某个变量的内存地址值
    # 赋值操作:将一个变量的内存地址赋值给另外一个变量
    a=[1]
    b=a
    a.append(5)
    print(a)
    print(id(a))
    print(b)
    print(id(b))

if __name__=="__main__":
    main()




