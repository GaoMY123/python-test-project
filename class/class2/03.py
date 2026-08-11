def main():
    #列表的定义
    list1=["张三","李四","王五",18]
    print(list1)
    print(type(list1))
    print(list1[0])
    print(list1[2])
    #切片
    print(list1[0:3])
    #快速反转
    print(list1[::-1])
    print(list1[-3])
    #只取三这一个元素
    print(list1[0][1])
    #列表的循环遍历
    for i in list1:
        print(i)
    i=0
    while i<len(list1):
        print(list1[i])
        i=i+1
    #len()查看容器中元素的个数
    print(len(list1))
    #append()在列表末尾添加一个元素
    list1.append("赵六")
    #extend()在列表末尾添加多个元素
    list1.extend('20')
    list1.extend([" ","狗剩"])
    print(list1)
    #insert()在列表指定位置插入一个元素
    list1.insert(1,"狗蛋")
    print(list1)
    #列表的修改
    list1[0]="王二"
    #列表的查看
    print("k" in list1)
    print("王二" in list1)
    print("20" not in list1)
    #count()统计元素出现的次数
    print(list1.count("20"))
    #index()返回元素第一次出现的索引位置
    print(list1.index("0"))
    print(list1.index(18))
    #列表去重
    list2=["张三","李四","王五","张三","王二"]
    li=[]
    for i in list2:
        if i not in li:
            li.append(i)
    print(li)
    #另一种方法
    li2=list(set(list2))#set()将列表转换为集合，去重后转换为列表
    print(li2)
    print(type(li2))
    #列表的删除
    # li2.remove("王二")
    print(li2)
    #pop()删除列表最后一个元素
    # li2.pop()
    # li2.pop(0)
    print(li2)
    #del 删除指定索引位置的元素
    # del li2[0]
    print(li2)
    del list2
    #排序，降序和升序,如果是字符串
    li2.sort()
    print(li2)
    li2.sort(reverse=True)
    print(li2)
    #倒序
    li2.reverse()
    print(li2)
    print(li2[::-1])
    li3=[]
    for i in li2:
        li3.insert(0,i)
    print(li3)
    #列表的嵌套
    li4=[["刘一","陈二","张三","李四"],["王五","赵六","孙七"],["周八","吴九","郑十"]]
    print(li4[0][1],li4[1][2],li4[2][2][1])
    '''
       列表和元素的区别
       列表是用[]定义的，元组是用()定义的
       列表支持增删改查等相关操作，元组只支持查看操作
       :return:
       '''
    # 元组的定义
    tuple = ("张三", "李四", "王五", "赵六", "郑十", "张三")
    s = ("Jane",)
    print(tuple)
    print(type(tuple))
    print(type(s))
    # 支持索引和切片操作
    print(tuple[0])
    print(tuple[-1])
    print(tuple[1:3])
    print(tuple[::-1])
    print(tuple[-3])
    # 查看元素在元组中的位置，in，not in
    print("张三" in tuple)
    print("王二" not in tuple)
    # index()返回元素第一次出现的索引位置
    print(tuple.index("张三"))
    print(tuple.index("王五"))
    # count()统计元素出现的次数
    print(tuple.count("张三"))
    # 不可变得数据类型
    tuple1 = ("张三", "李四", "王五", "赵六", "郑十", "张三")
    print(tuple1)
    print(type(tuple1))
    # 元组的修改
    # tuple1[0]="王二"
    print(tuple1)
    # 元组的查看
    print("张三" in tuple1)
    print("王二" not in tuple1)
    # index()返回元素第一次出现的索引位置
    print(tuple1.index("张三"))
    print(tuple1.index("王五"))
    # count()统计元素出现的次数
    print(tuple1.count("张三"))
    # 可变的数据类型
    list1 = ["张三", "李四", "王五", 18]
    print(list1)
    print(type(list1))
    print(list1.append("赵六"))
    print(list1)
    # 字典的定义
    dict = {
        "name": "张三",
        "age": "18",
        "city": "北京"
    }
    print(dict)
    # 查看键、值
    print(dict.keys())
    print(dict.values())
    print(dict["name"])
    # 查看键值对
    print(dict.items())
    # 字典的相关操作，取值，字典名[]键名 键不存在则报错，字典名.get(键名) 键不存在则返回None
    print(dict["age"])
    # print(dict["nihao"])
    print(dict.get("city"))
    print(dict.get("data"))
    # 字典的添加与修改，键不存在则添加，键存在则修改
    dict["data"] = "12"
    print(dict.keys())
    dict["name"] = "李四"
    print(dict)
    # 字典的删除
    # pop,del,clear()
    # dict.pop("name")
    # print(dict)
    # del dict["age"]
    # print(dict)
    # dict.clear()#清空字典
    # print(dict)
    # 字典的遍历，遍历键
    for i in dict.keys():
        print(i)
    for i in dict:
        print(i)
    # 遍历值
    for i in dict.values():
        print(i)
    for i in dict:
        print(dict[i])
    # 遍历键值对
    # items()返回的是元组类型，元组中的每一个元素都是键值对
    for i in dict.items():
        print(i)
        print(f"键为{i}，值为{dict[i[0]]}")
    for i in dict:
        print(i, dict[i])
        print(f"键为{i}，值为{dict[i]}")
    # join()拼接字符串
    str1 = "-"
    li = ['张三', "李四", "王五"]
    z = str1.join(li)
    print(z)
    print(type(z))
    # 列表的定义
    list1 = ["张三", "李四", "王五", 18]
    print(list1)
    print(type(list1))
    print(list1[0])
    print(list1[2])
    # 切片
    print(list1[0:3])
    # 快速反转
    print(list1[::-1])
    print(list1[-3])
    # 只取三这一个元素
    print(list1[0][1])
    # 列表的循环遍历
    for i in list1:
        print(i)
    i = 0
    while i < len(list1):
        print(list1[i])
        i = i + 1
    # len()查看容器中元素的个数
    print(len(list1))
    # append()在列表末尾添加一个元素
    list1.append("赵六")
    # extend()在列表末尾添加多个元素
    list1.extend('20')
    list1.extend([" ", "狗剩"])
    print(list1)
    # insert()在列表指定位置插入一个元素
    list1.insert(1, "狗蛋")
    print(list1)
    # 列表的修改
    list1[0] = "王二"
    # 列表的查看
    print("k" in list1)
    print("王二" in list1)
    print("20" not in list1)
    # count()统计元素出现的次数
    print(list1.count("20"))
    # index()返回元素第一次出现的索引位置
    print(list1.index("0"))
    print(list1.index(18))
    # 列表去重
    list2 = ["张三", "李四", "王五", "张三", "王二"]
    li = []
    for i in list2:
        if i not in li:
            li.append(i)
    print(li)
    # 另一种方法
    li2 = list(set(list2))  # set()将列表转换为集合，去重后转换为列表
    print(li2)
    print(type(li2))
    # 列表的删除
    # li2.remove("王二")
    print(li2)
    # pop()删除列表最后一个元素
    # li2.pop()
    # li2.pop(0)
    print(li2)
    # del 删除指定索引位置的元素
    # del li2[0]
    print(li2)
    del list2
    # 排序，降序和升序,如果是字符串
    li2.sort()
    print(li2)
    li2.sort(reverse=True)
    print(li2)
    # 倒序
    li2.reverse()
    print(li2)
    print(li2[::-1])
    li3 = []
    for i in li2:
        li3.insert(0, i)
    print(li3)
    # 列表的嵌套
    li4 = [["刘一", "陈二", "张三", "李四"], ["王五", "赵六", "孙七"], ["周八", "吴九", "郑十"]]
    print(li4[0][1], li4[1][2], li4[2][2][1])
    '''
       列表和元素的区别
       列表是用[]定义的，元组是用()定义的
       列表支持增删改查等相关操作，元组只支持查看操作
       :return:
       '''
    # 元组的定义
    tuple = ("张三", "李四", "王五", "赵六", "郑十", "张三")
    s = ("Jane",)
    print(tuple)
    print(type(tuple))
    print(type(s))
    # 支持索引和切片操作
    print(tuple[0])
    print(tuple[-1])
    print(tuple[1:3])
    print(tuple[::-1])
    print(tuple[-3])
    # 查看元素在元组中的位置，in，not in
    print("张三" in tuple)
    print("王二" not in tuple)
    # index()返回元素第一次出现的索引位置
    print(tuple.index("张三"))
    print(tuple.index("王五"))
    # count()统计元素出现的次数
    print(tuple.count("张三"))
    # 不可变得数据类型
    tuple1 = ("张三", "李四", "王五", "赵六", "郑十", "张三")
    print(tuple1)
    print(type(tuple1))
    # 元组的修改
    # tuple1[0]="王二"
    print(tuple1)
    # 元组的查看
    print("张三" in tuple1)
    print("王二" not in tuple1)
    # index()返回元素第一次出现的索引位置
    print(tuple1.index("张三"))
    print(tuple1.index("王五"))
    # count()统计元素出现的次数
    print(tuple1.count("张三"))
    # 可变的数据类型
    list1 = ["张三", "李四", "王五", 18]
    print(list1)
    print(type(list1))
    print(list1.append("赵六"))
    print(list1)
    # 字典的定义
    dict = {
        "name": "张三",
        "age": "18",
        "city": "北京"
    }
    print(dict)
    # 查看键、值
    print(dict.keys())
    print(dict.values())
    print(dict["name"])
    # 查看键值对
    print(dict.items())
    # 字典的相关操作，取值，字典名[]键名 键不存在则报错，字典名.get(键名) 键不存在则返回None
    print(dict["age"])
    # print(dict["nihao"])
    print(dict.get("city"))
    print(dict.get("data"))
    # 字典的添加与修改，键不存在则添加，键存在则修改
    dict["data"] = "12"
    print(dict.keys())
    dict["name"] = "李四"
    print(dict)
    # 字典的删除
    # pop,del,clear()
    # dict.pop("name")
    # print(dict)
    # del dict["age"]
    # print(dict)
    # dict.clear()#清空字典
    # print(dict)
    # 字典的遍历，遍历键
    for i in dict.keys():
        print(i)
    for i in dict:
        print(i)
    # 遍历值
    for i in dict.values():
        print(i)
    for i in dict:
        print(dict[i])
    # 遍历键值对
    # items()返回的是元组类型，元组中的每一个元素都是键值对
    for i in dict.items():
        print(i)
        print(f"键为{i}，值为{dict[i[0]]}")
    for i in dict:
        print(i, dict[i])
        print(f"键为{i}，值为{dict[i]}")
    # join()拼接字符串
    str1 = "-"
    li = ['张三', "李四", "王五"]
    z = str1.join(li)
    print(z)
    print(type(z))

if __name__=="__main__":
    main()