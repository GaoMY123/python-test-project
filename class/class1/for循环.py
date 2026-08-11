def main():
    a=["ds","sd"]#列表

    for i in a:
        print(i)
    #生成1-10之间的所有数
    for i in range(1,11):
        print(i)
    #生成1-100之间的偶数
    for i in range(2,101,2):
        print(i)
    for i in range(1,101):
        if i%2==0:
            print(i)
    #生成1-100之间的所有数
    for i in range(1,101):
        print(i)
    #生成1-100之间的奇数
    for i in range(1,101,2):
        print(i)
    #生成1-100之间所有数的和：
    sum=0
    for i in range(1,101):
        sum=sum+i
    print(sum)
    #生成1-100之间所有偶数的和
    sum=0
    for i in range(2,101,2):
        sum=sum+i
    print(sum)
    #生成斐波那契数列:每一项都是前两项的和
    #append()方法:在列表末尾添加一个元素或多个元素
    a=[1,1]#初始化列表，包含前两项，第一项为1.第二项为1，第三项就为第一项加第二项。
    for i in range(2,10):
        a.append(a[i-1]+a[i-2])
        print(a)
        print(a[i])
    #打印100-1之间的所有数
    for i in range(100,0,-1):
        print(i)
    i=1
    for i in range(1,10):
        print(i)
    else:
        print(i)
i =1
for i in range(1,10):
    print(i)
if __name__ == '__main__':
    main()
