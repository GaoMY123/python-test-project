#返回值作用：
#1.将函数的执行结果返回给调用者
#2.结束函数的调用
import copy
def main():
    def demo(a,b):
    #return a+b
    #return a+b,a*b
        return {"和为":a+b,"积为":a*b}
    print(demo(1,2))
    print(type(demo(1,2)))
    # 函数的返回值作用：
    # 1.将函数的执行结果返回给调用者
    # 2.结束函数的调用
    def demo1(a,b):
        #return a+b
        # return a=b,a*b
        return a+b,a*b
    print(demo1(1,2))
    print(type(demo1(1,2)))
    #可变与不可变的数据类型
    #可变：列表、元组、字典
    #不可变：字符串、整数、浮点数、布尔值
    #is 关键字：判断两个变量是否指向同一个对象
    #is:判断的是内存地址是否相等，是否是同一个对象
    #==：判断的是值是否相等
    a=1
    b=1
    print(a==b)
    print(a is b)
    print(id(a))
    print(id(b))
    #可变与不可变函数的数据类型
    #可变：列表、元组、字典
    #不可变：字符串、整数、浮点数、布尔值
    #is 和 == 的区别
    #is：判断的是内存地址是否相等，==判断的是值是否相等
    a=1
    b=1
    print(a==b)
    print(a is b)
    print(id(a))
    print(id(b))
    #深拷贝和浅拷贝
    #深拷贝：完完全全的拷贝，拷贝之后的数据和元数据没有任何关系，关键字事copy.deepcopy()
    #浅拷贝：只拷贝了数据，没有复制内部子对象copy.copy()
    #内部子对象：元数据修改之后，会影响拷贝后的数据
    data={"name":"张三","age":18}
    date1=copy.deepcopy(data)
    print(data)
    print(date1)
    #浅拷贝
    data2=copy.copy(data)
    data['class']=3
    data['name']='张三'
    print(data)
    print(data2)
    #深拷贝和浅拷贝
    # 深拷贝：完完全全的拷贝，拷贝之后的数据和元数据没有任何关系，关键字是copy.deepcopy()
    #浅拷贝：只拷贝了数据，没有复制内部子对象copy.copy()
    #内部子对象：元数据修改的话，会影响拷贝后的数据
    data = {"name": "张三", "age": 18}
    date1 = copy.deepcopy(data)
    print(data)
    print(date1)
    # 浅拷贝
    data2 = copy.copy(data)
    data['class'] = 3
    data['name'] = '张三'
    print(data)
    print(data2)


if __name__=='__main__':
    main()

