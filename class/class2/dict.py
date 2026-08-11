#字典
def main():
    #字典的定义
    dict={
        "name":"张三",
        "age":"18",
        "city":"北京"
    }
    print(dict)
    #查看键、值
    print(dict.keys())
    print(dict.values())
    print(dict["name"])
    #查看键值对
    print(dict.items())
    #字典的相关操作，取值，字典名[]键名 键不存在则报错，字典名.get(键名) 键不存在则返回None
    print(dict["age"])
    # print(dict["nihao"])
    print(dict.get("city"))
    print(dict.get("data"))
    #字典的添加与修改，键不存在则添加，键存在则修改
    dict["data"]="12"
    print(dict.keys())
    dict["name"]="李四"
    print(dict)
    #字典的删除
    # pop,del,clear()
    # dict.pop("name")
    # print(dict)
    # del dict["age"]
    # print(dict)
    # dict.clear()#清空字典
    # print(dict)
    #字典的遍历，遍历键
    for i in dict.keys():
        print(i)
    for i in dict:
        print(i)
    #遍历值
    for i in dict.values():
        print(i)
    for i in dict:
        print(dict[i])
    #遍历键值对
    #items()返回的是元组类型，元组中的每一个元素都是键值对
    for i in dict.items():
        print(i)
        print(f"键为{i}，值为{dict[i[0]]}")
    for i in dict:
        print(i,dict[i])
        print(f"键为{i}，值为{dict[i]}")
    #join()拼接字符串
    str1="-"
    li=['张三',"李四","王五"]
    z=str1.join(li)
    print(z)
    print(type(z))



if __name__=="__main__":
    main()