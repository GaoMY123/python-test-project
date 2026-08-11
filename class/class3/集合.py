def main():
    s={1,2,3,4,5}
    print(s)
    print(type(s))
    #带下标索引的遍历
    z=['a','b','c','d','e']
    for i in enumerate(z):
        print(i)
    for i in enumerate(z):
        print(f"索引为：{i[0]},元素为：{i[1]}")
    #集合的特点：无序、不重复、无索引、无元素类型限制
    #对列表进行去重
    l=[1,2,3,4,5,1,2,3,4,5]
    z=list(set(l))
    print(z)
    #集合的添加操作，add()，update(),union()
    s.add(6)
    s.update([7,8,9])
    s.union([10,11])
    print(s)
    #集合的删除操作，remove()，discard().pop()
    #remove()：删除指定的元素，如果元素不存在，会报错
    #discard()：删除指定的元素，如果元素不存在，不会报错
    #pop()：随机删除一个元素，返回该元素
    #clear()：清空集合
    s.remove(6)
    s.discard(8)
    # s.pop()
    # s.clear()
    print(s)
    #集合的交集、并集、差集、对称差集
    #什么叫差集：两个集合的差集，是指在第一个集合中，而不在第二个集合中的元素
    s1={1,2,3,4,5}
    s2={4,5,6,7,8}
    print("交集",s1&s2)
    print("并集",s1|s2)
    print("差集",s1-s2)
    print("对称差集",s1^s2)
    # 公共内置方法：+，*，in,not in,min(),max(),len()
    print("+",s1+s2)
    print("*",s1*s2)
    print("最大值",max(s1))
    print("最小值",min(s1))
    print("求和",sum(s1))



if __name__=="__main__":
    main()
