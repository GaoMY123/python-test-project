#集合是一个无序的、不可变且没有索引的结合，而且当中没有重复元素
def main():
    #创建一个集合，使用set（）函数
    fruits={"apple","banana","cherry"}
    print(type(fruits))
    print(fruits)
    #集合项是不可变的，这意味着在创建集合后我们无法更改项,但是可以删除并添加元素
    fruits.add("orange")
    print(fruits)
    #元素不可重复,值True和1被视为集合中的相同值，并被视为重复项,False和0被视为集合中的相同值，并被视为重复项
    fruits={"apple","banana","cherry",True,1,2,False,0}
    fruits.add("apple")
    print("fruits")
    #获取集合中的长度，使用len()函数
    print(len(fruits))
    #设置项可以是任何数据类型，包括字符串、数字、元组、列表、字典等
    set1={"abc",123,True,False}
    print(set1)
    #集合的类型是set
    print(type(set1))
    #使用set函数创建一个集合
    set2=set(set1)
    print(set2)
    '''
    Python 编程语言中有四种集合数据类型：

    列 list 列表是一个有序且可变的集合。允许重复的成员。
    tuple 元组是一个有序且不可更改的集合。允许重复的成员。
    Set Set是一个无序、不可更改*且无索引的集合。没有重复的成员。
    dict 字典 Dictionary是一个有序的、可变的集合。没有重复的成员。
    '''
    #集合的循环,因为是无序的，所以循环的顺序是随机的
    for x in fruits:
        print(x)
    #检查某个元素是否在集合中
    print("apple" in fruits)
    #检查某个元素是否不在集合中
    print("orange" not in fruits)
    #可以使用add（）方法添加元素到集合中
    fruits.add("lemon")
    print(fruits)
    #使用update()方法添加多个元素到集合中
    s={"apple","watermelon","pineapple","mango","papaya"}
    fruits.update(s)
    print(fruits)
    #使用remove()方法删除除集合中的元素
    fruits.remove("lemon")
    print(fruits)
    #使用discard()方法删除除集合中的元素
    fruits.discard("apple")
    print(fruits)
    #使用pop方法删除项目，但是此方法会删除最后一项，set（）是无序的，因此不知道被删除的是什么项目
    fruits.pop()
    print(fruits)
    #使用clear（）方法清空集合中的所有元素
    #fruits.clear()
    print(fruits)
    #使用del（）方法彻底删除一个集合
    del s
    #使用union（）方法返回一个新集合，包含两个集合中的所有项目，还可以使用|运算符来表示
    #union()方法同时也允许合并集合、元组、列表、字典等
    a={"vegtables","fruits"}
    c=fruits.union(a)
    d=fruits | a
    print(c)
    print(d)
    #使用intersection（）方法返回一个新集合，包含两个集合中都存在的项目,也可以使用&运算符来表示
    e=fruits.intersection(a)
    print(e)
    f=fruits & a
    print(f)
    #intersection_update()方法会从集合中移除所有不在指定集合中的元素
    fruits.intersection_update(a)
    print(fruits)
    #使用difference（）方法返回一个新集合，包含两个集合中存在一个但不存在另一个集合中的项目
    g=fruits.difference(a)
    print(g)
    #使用difference_update()方法会从集合中移除所有在指定集合中的元素，像这样类似的还有symmetric_difference_update()方法，以及^运算符
    #symmetric_difference_update()方法会从集合中移除所有在指定集合中的元素，以及在指定集合中不存在的元素
    #^运算符会返回一个新集合，包含两个集合中存在一个但不存在另一个集合中的项目
    fruits.difference_update(a)
    print(fruits)
    #frozenset()函数会返回一个冻结的集合，冻结的集合是不可变的，不能被修改
    h=frozenset(fruits)
    print(h)
    #冻结的集合的类型是frozenset
    print(type(h))
    #冻结的集合的循环
    for x in h:
        print(x)
    #冻结的集合的循环遍历索引数字
    for i in range(len(h)):
        print(i)
        print(h[i])
    #冻结的集合的循环while循环
    i=0
    while i<len(h):
        print(i)
        print(h[i])
        i+=1








if __name__ =='__main__':
    main()
