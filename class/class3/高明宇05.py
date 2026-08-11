def main():
    s={1,2,3,4,5}
    print(s)
    print(type(s))
    #带下标索引的遍历
    z=['a','b','c','d','e']
    for i in enumerate(z):
        print(i)
    for i in enumerate(z):
        print(f"索引为：{i[0]},元素为{i[1]}")
    #集合的特点：无序、不重复、无索引、无元素类型限制
    #对列表进行去重
    l=[1,2,3,4,5,1,2,3,4,5]
    z=set(list(l))
    print(z)
    #集合的添加操作：add(),update(),union()
    s.add(6)
    s.update([7,8,9])
    s.union([10,11])
    print(s)
    #集合的删除操作：remove(),discard(),pop()
    #remove():删除指定元素，如果元素不存在，会报错
    #discard():删除指定元素，如果元素不存在，不会报错
    #pop():随机删除一个元素
    #clear():清空集合
    s.remove(6)
    s.pop()
    #s.discard(8)
    #s.clear()
    print(s)
    #集合的交集、并集、差集、对称差集
    #什么叫差集:两个集合的差集，是指在第一个集合中，而不在第二个集合中的元素
    s1={1,2,3,4,5}
    s2={4,5,6,7,8}
    print("交集",s1&s2)
    print("并集",s1|s2)
    print("差集",s1-s2)
    print("对称差集",s1^s2)
    #公共内置方法：+,*,in,not in,min(),max(),sum()
    # print("+",s1+s2)#
    # print("*",s1*s2)
    print("最大值",max(s1))
    print("最小值",min(s1))
    print("求和",sum(s1))
    #函数
    def demo():
        i=1
        sum=0
        while i<=100:
            if i %2==0:
                sum+=i
            i=i+1
        print(i)
    demo()
    #添加函数的文档说明，长摁Ctrl，点击函数名，help(函数名)
    def demo1():
        '''
        这是一个函数，用于求1-100之间的和
        '''
        i = 1
        sum = 0
        while i <= 100:
            if i % 2 == 0:
                sum += i
            i = i + 1
        print(i)

    demo1()
    help(demo1)
    #函数的参数和返回值，参数分为形参和实参
    #形参：在函数定义时，定义的参数，用于接收实参
    #实参:在函数调用时，传递给函数的参数，用于替换形参
    #返回值：在函数执行完成之后，将结果返回给调用者
    def demo2(a,b):
        return a+b
    print(demo2(1,2))
    #函数的嵌套调用
    #需求1：定义一个函数可以打印一行横线
    #需求2：定义一个函数可以打印自定义行数的函数
    def demo3():
        print('-'*10)
    def demo4():
        n=int(input("请输入要打印的行数："))
        for i in range(n):
            demo3()
    demo4()
    #局部变量，定义在函数内部的变量，只能在函数内部使用
    def test3():
        a=10
        print(a)
    test3()
    #全局变量
    a=100
    def test4():
        a=10
        print(a)
    test4()
    print(a)
    #global函数：在函数内部定义的变量，可以在函数外部使用
    #nonlocal函数：在函数内部定义的变量，可以在函数外部使用，在函数嵌套时使用
    def test5():
        nonlocal a
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
    data={"name":"张三","age":18,"sex":"男"}
    for i,j in data.items():
        print(i,j)
    #交换变量的值1
    a=1
    b=2
    c=a
    a=b
    b=c
    print(a,b)
    #2
    a,b=b,a
    print(a,b)
    #3
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
    #九九乘法表
    i=1
    while i<10:
        j=1
        while j<=i:
            print(f"{j}*{i}={i*j}",end=' ')
            j+=1
        print()
        i+=1
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}*{i}={i*j}",end=' ')
        print()
    s = {1, 2, 3, 4, 5}
    print(s)
    print(type(s))
    # 带下标索引的遍历
    z = ['a', 'b', 'c', 'd', 'e']
    for i in enumerate(z):
        print(i)
    for i in enumerate(z):
        print(f"索引为：{i[0]},元素为{i[1]}")
    # 集合的特点：无序、不重复、无索引、无元素类型限制
    # 对列表进行去重
    l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    z = set(list(l))
    print(z)
    # 集合的添加操作：add(),update(),union()
    s.add(6)
    s.update([7, 8, 9])
    s.union([10, 11])
    print(s)
    # 集合的删除操作：remove(),discard(),pop()
    # remove():删除指定元素，如果元素不存在，会报错
    # discard():删除指定元素，如果元素不存在，不会报错
    # pop():随机删除一个元素
    # clear():清空集合
    s.remove(6)
    s.pop()
    # s.discard(8)
    # s.clear()
    print(s)
    # 集合的交集、并集、差集、对称差集
    # 什么叫差集:两个集合的差集，是指在第一个集合中，而不在第二个集合中的元素
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    print("交集", s1 & s2)
    print("并集", s1 | s2)
    print("差集", s1 - s2)
    print("对称差集", s1 ^ s2)
    # 公共内置方法：+,*,in,not in,min(),max(),sum()
    # print("+",s1+s2)#
    # print("*",s1*s2)
    print("最大值", max(s1))
    print("最小值", min(s1))
    print("求和", sum(s1))

    # 函数
    def demo():
        i = 1
        sum = 0
        while i <= 100:
            if i % 2 == 0:
                sum += i
            i = i + 1
        print(i)

    demo()

    # 添加函数的文档说明，长摁Ctrl，点击函数名，help(函数名)
    def demo1():
        '''
        这是一个函数，用于求1-100之间的和
        '''
        i = 1
        sum = 0
        while i <= 100:
            if i % 2 == 0:
                sum += i
            i = i + 1
        print(i)

    demo1()
    help(demo1)

    # 函数的参数和返回值，参数分为形参和实参
    # 形参：在函数定义时，定义的参数，用于接收实参
    # 实参:在函数调用时，传递给函数的参数，用于替换形参
    # 返回值：在函数执行完成之后，将结果返回给调用者
    def demo2(a, b):
        return a + b

    print(demo2(1, 2))

    # 函数的嵌套调用
    # 需求1：定义一个函数可以打印一行横线
    # 需求2：定义一个函数可以打印自定义行数的函数
    def demo3():
        print('-' * 10)

    def demo4():
        n = int(input("请输入要打印的行数："))
        for i in range(n):
            demo3()

    demo4()

    # 局部变量，定义在函数内部的变量，只能在函数内部使用
    def test3():
        a = 10
        print(a)

    test3()
    # 全局变量
    a = 100

    def test4():
        a = 10
        print(a)

    test4()
    print(a)

    # global函数：在函数内部定义的变量，可以在函数外部使用
    # nonlocal函数：在函数内部定义的变量，可以在函数外部使用，在函数嵌套时使用
    def test5():
        nonlocal a
        print(a)

    test5()
    print(a)
    # 拆包：将一个列表或者元组中的元素，分别赋值给多个变量
    l = [1, 2, 3, 4, 5]
    a, b, c, d, e = l
    print(a, b, c, d, e)
    # 方式一：容器中有几个元素就找几个变量来接收
    # 方式二：可以使用*号将容器中的元素接收
    a, b, *c = l
    print(a, b, c)
    # 应用：将一个字典中的元素，分别赋值给多个变量
    data = {"name": "张三", "age": 18, "sex": "男"}
    for i, j in data.items():
        print(i, j)
    # 交换变量的值1
    a = 1
    b = 2
    c = a
    a = b
    b = c
    print(a, b)
    # 2
    a, b = b, a
    print(a, b)
    # 3
    a = a + b
    b = a - b
    a = a - b
    print(a, b)
    # 九九乘法表
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print(f"{j}*{i}={i * j}", end=' ')
            j += 1
        print()
        i += 1
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}*{i}={i * j}", end=' ')
        print()
if __name__=="__main__":
    main()



