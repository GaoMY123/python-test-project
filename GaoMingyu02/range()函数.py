# range()函数返回一个不可变的数字序列，通常用于循环特定次数
#语法：range(start,stop,step)
#范围对象是一种表示不可变的数字序列的数据类型，他不能直接显示，因此范围列表通常被转换为列表进行显示

def main():

    print(list(range(10)))
    print(list(range(1,10)))
    #与其他序列一样，范围可以被切片以提取子序列
    r=range(10)
    print(r[2])
    print(r[:6])
    #len()函数，in
    print(len(r))
    print(5 in r)
if __name__ =='__main__':
    main()
