#
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




if __name__=="__main__":
    main()