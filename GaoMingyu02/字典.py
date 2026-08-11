#字典
def main():
    #字典是一个无序、可变的集合，每个元素都有一个键和一个值
    #键必须是唯一的，值可以是任何数据类型
    #键和值之间用冒号隔开，每个键值对之间用逗号隔开
    #字典的类型是dict
    #字典的创建
    thisdict={
        "apple":"red",
        "banana":"yellow",
        "cherry":"green"
    }
    print(thisdict)
    #可以对方括号引用键名来访问字典的值
    print(thisdict["apple"])
    #使用get（）方法也会产生相同的结果
    print(thisdict.get("apple"))
    #如果键名不存在，get（）方法会返回None
    print(thisdict.get("orange"))
    #可以通过引用键名来更改特定项的值
    thisdict["apple"]="black"
    print(thisdict)
    #可以使用for循环来遍历字典的所有键名和值
    for x in thisdict:
        print(x)
        print(thisdict[x])
    for x,y in thisdict.items():
        print(x,y)
    #返回字典中的值还可以用values（）方法
    print(thisdict.values())
    #还可以使用items（）函数来遍历键和值
    print(thisdict.items())
    #确定字典中是否存在指定的键，可以使用in关键字
    print("apple" in thisdict)
    #确定字典中是否存在指定的值，可以使用values（）方法
    print("red" in thisdict.values())
    #查看字典中有多少键值对，可以使用len()函数
    print(len(thisdict))
    #添加项目
    thisdict["orange"]="blue"
    print(thisdict)
    #删除项目，使用pop（）方法删除具有指定键名的项，使用popitem()方法删除最后一个项（如果是在python3.7之前版本，会随机删除一个键值对，现在会删除最后一个键值对）
    thisdict.pop("orange")
    print(thisdict)
    thisdict.popitem()
    print(thisdict)
    #del关键字可以删除具有指定键名的项，也可以完全删除字典
    del thisdict["apple"]
    print(thisdict)
    # del thisdict
    # 清空字典
    thisdict.clear()
    print(thisdict)
    #复制字典，使用copy（）方法
    mydict=thisdict.copy()
    print(mydict)
    #另一种方式，使用dict（）函数
    mydict=dict(thisdict)
    print(mydict)
    #嵌套字典
    myfamily = {
        "child1": {
            "name": "Phoebe Adele",
            "year": 2002
        },
        "child2": {
            "name": "Jennifer Katharine",
            "year": 1996
        },
        "child3": {
            "name": "Rory John",
            "year": 1999
        }
    }
    print(myfamily)
    #使用update()方法更新字典
    myfamily.update({"child4": {"name": "Lily John", "year": 2000}})
    print(myfamily)
    #打印嵌套字典中的某个项加值
    print(myfamily["child1"]["name"])
    print(myfamily.items())
    for x,obj in myfamily.items():
        print(x)
        # for y in obj:
        #     print(y)
    #找字典中的具体某个键
    




if __name__ =='__main__':
    main()
