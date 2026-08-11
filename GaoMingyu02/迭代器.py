#迭代器是一个可以迭代的对象，意味着可以遍历所有值
#迭代器的实现需要实现__iter__和__next__方法
#迭代器vs可迭代对象，列表、元组、字符串、字典等都是可迭代对象，但是它们可以从中获取迭代器的可迭代容器
#iter()函数用于获取迭代器
#从元组中返回一个迭代器，并打印每一个值
def main():

    t=(1,2,3,4,5)
    myit=iter(t)
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))

if __name__=="__main__":
    main()