from itertools import count


def main():
    i=2
    while i<101:
        print("当前循环的次数为：",i)
        i+=2
    print("循环结束")
    z=2
    s=2
    while s%z==0 and s<=100:
        print(s)
        s = s + 2

    i=1
    sum=0
    while i<=100:
        sum=sum+i
        i+=1
    print("1到100的和为:",sum)
    #打印1到100之间所有偶数的和
    i=2
    sum=0
    while i<=100:
        sum=sum+i
        i=i+2
    print("1到100之间所有偶数的和为:",sum)
    z = 2
    s = 2
    sum=0
    while s % z == 0 and s <= 100:
        sum=sum+s
        s = s + 2
    print("1到100之间所有偶数的和为:",sum)
    #打印1到100之间所有奇数的和
    i=1
    sum=0
    while i<=100:
        sum=sum+i
        i+=2
    print("1到100之间所有奇数的和为:",sum)
    z = 2
    s = 1
    sum=0
    while s % z != 0 and s <= 100:
        sum=sum+s
        s = s + 2
    print("1到100之间所有奇数的和为:",sum)


if __name__ == '__main__':
    main()
