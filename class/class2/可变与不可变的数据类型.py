#不可变的数据类型：元组、字符串、布尔值
#可变的数据类型：列表、字典、集合
def main():
    #不可变得数据类型
    tuple1=("张三","李四","王五","赵六","郑十","张三")
    print(tuple1)
    print(type(tuple1))
    #元组的修改
    #tuple1[0]="王二"
    print(tuple1)
    #元组的查看
    print("张三" in tuple1)
    print("王二" not in tuple1)
    #index()返回元素第一次出现的索引位置
    print(tuple1.index("张三"))
    print(tuple1.index("王五"))
    #count()统计元素出现的次数
    print(tuple1.count("张三"))
    #可变的数据类型
    list1=["张三","李四","王五",18]
    print(list1)
    print(type(list1))
    print(list1.append("赵六"))
    print(list1)
if __name__=="__main__":
    main()
