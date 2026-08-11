def main():
    '''
    列表和元素的区别
    列表是用[]定义的，元组是用()定义的
    列表支持增删改查等相关操作，元组只支持查看操作
    :return:
    '''
    #元组的定义
    tuple=("张三","李四","王五","赵六","郑十","张三")
    s=("Jane",)
    print(tuple)
    print(type(tuple))
    print(type(s))
    #支持索引和切片操作
    print(tuple[0])
    print(tuple[-1])
    print(tuple[1:3])
    print(tuple[::-1])
    print(tuple[-3])
    #查看元素在元组中的位置，in，not in
    print("张三" in tuple)
    print("王二" not in tuple)
    #index()返回元素第一次出现的索引位置
    print(tuple.index("张三"))
    print(tuple.index("王五"))
    #count()统计元素出现的次数
    print(tuple.count("张三"))


if __name__=="__main__":
    main()
