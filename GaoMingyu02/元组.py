# 元组和列表的区别：
# 元组的元素不能被修改，列表的元素可以被修改
# 元组的元素可以是任意类型，列表的元素可以是任意类型
# 元组的元素可以是元组，列表的元素可以是元组
# 元组的元素可以是列表，列表的元素可以是元组
# 元组的元素可以是字典，列表的元素可以是字典
# 元组的元素可以是集合，列表的元素可以是集合
import random
def main():
    mytuple = ("apple", "banana", "orange")  # 元组的顺序是不可变的，创建之后不能添加或者删除项，可以被索引访问
    print(mytuple[0])
    mytuple = ("apple", "banana", "orange", "apple")  # 元组的元素可以重复,因为有索引
    # 使用len函数确认元组的长度
    print(len(mytuple))
    print(mytuple[0:2])
    #创建只有一个元素的元组
    mytuple1=("apple")#如果只有一个元素，不加逗号的话会被认为是一个字符串，而不是元组
    myyuple2=("apple",)
    print(type(mytuple1))
    print(type(myyuple2))
    #元组的元素可以是任何数据类型,列表中的元素也可以是任何数据类型
    mytuple3=("apple",123,456,789,3.14,True)
    print(mytuple3)
    #还可以使用tuple()函数来创建元组
    mytuple4=tuple(("apple","banana","orange"))
    print(type(mytuple4))
    #访问元组的元素
    #第一个元素的索引依旧是0，-1指的是最后一个项目，-2指的是倒数第二个项目
    print(mytuple4[0])
    print(mytuple[-1])
    #索引的范围是0到元组的长度减1
    print(mytuple[0:2])
    #负索引的范围是从元组的末尾开始
    print(mytuple[-4:-1])
    #用in来检查元组中是否包含某个元素
    print("apple" in mytuple)
    #如何更改元组值，可以将元组转换为列表，修改列表，然后再将列表转换成元组
    mytuple5=("apple","banana","orange")
    mytuple5=list(mytuple5)
    mytuple5[0]="peach"
    mytuple5=tuple(mytuple5)
    print(mytuple5)
    #添加元组的元素，可以将元组转换为列表，添加元素，然后再将列表转换成元组，可以使用append（）方法添加元素
    mytuple5=list(mytuple5)
    mytuple5.append("peach")
    mutuple5=tuple(mytuple5)
    print(mutuple5)
    #如果想要添加多个元素，可以创建一个新的元组，将旧的元组和新的元素合并起来,还可以转换成列表使用extend()方法
    a=('watermelon',)
    mytuple5+=a
    print(mytuple5)
    #extend()方法可以将一个元组添加到元组的末尾，也可以转换为列表
    #移除某个项目，同样可以将元组转换成列表，移除元素，然后再将列表转换成元组，使用remove（）方法
    mytuple5=list(mytuple5)
    myluple5=mytuple5.remove("orange")
    mytuple5=tuple(mytuple5)
    print(mytuple5)
    #删除一个元组，使用del（）方法
    #del mytuple5
    #print(mytuple5)
    #解压一个元组，将元组中的元素分别赋值给多个变量
    fruits=("apple","banana","cherry")
    (red,yellow,green)=fruits
    print(red)
    print(yellow)
    print(green)
    #如果变量的数量少于值的数量，可以在变量名前添加一个*，值将被分配给变量作为一个列表
    fruits=("appple","banana","cherry","柠檬")
    (red,yellow,*green)=fruits
    print(red)
    print(yellow)
    print(green)
    # 如果*号添加到除最后一个变量名之外的变量名，python将分配值到变量，直到剩余值的数量与剩余变量的数量相匹配
    fruits=("apple","banana","peach","watermelon","orange","lemon")
    (red,*yellow,green)=fruits
    print(red)
    print(yellow)
    print(green)
    #循环元组
    for i in fruits:
        print(i)
    #循环遍历索引数字
    for i in range(len(fruits)):
        print(i)
        print(fruits[i])
    #使用while循环
    i=0
    while i<len(fruits):
        print(i)
        print(fruits[i])
        i+=1
    #连接两个元组,使用+运算符
    b=fruits+a
    print(b)
    #元组相乘，可以使用*运算符
    c=fruits*2
    print(c)
    #元组的方法：count()方法将返回元组中某个元素出现的次数
    print(fruits.count("apple"))
    #元组的方法：index()方法将返回元组中某个元素的第一个索引
    print(fruits.index("apple"))







if __name__ =='__main__':
    main()