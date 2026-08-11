#打印一行*代码， 这份代码用五次
#end='' 表示不换行
def main():
    #使用for循环嵌套打印*代码
    for i in range(5):
        for x in range(5):
            print('*',end='  ')
#换行
        print()
#使用while循环嵌套打印*代码
    i=1
    while i<=5:
        j=1
        while j<=5:
            print('*',end='  ')
            j=j+1
        i=i+1
        print()
#打印三角形
    i=1
    while i<=5:
        j=1
        while j<=i:
            print('*',end=' ')
            j=j+1
        i=i+1
        print()
#打印倒三角形
    i=5
    while i>=1:
        j=1
        while j<=i:
            print("*",end="  ")
            j=j+1
        print()
        i=i-1
#打印乘法表
    i=1
    while i<=9:
        j=1
        while j<=i:
            print(f"{i}*{j}={i*j}",end="  ")
            j=j+1
        print()
        i=i+1
#打印等腰三角形
    for i in range(5):
        for j in range(5-i+1):
            print(' ',end='')
        for j in range(i+1):
            print('*',end=' ')
        print()
    i=1
    while i<=5:
        #打印空格
        j=1
        while j<=5-i:
            print(' ',end='')
            j=j+1
        #打印*
        k=1
        while k<=i:
            print('*',end=' ')
            k=k+1
        print()
        i=i+1
#如何打印一个
if __name__ == '__main__':
    main()
