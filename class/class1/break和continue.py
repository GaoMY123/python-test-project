#break语句：用于跳出循环
#continue语句：用于跳过当前循环，继续下一次循环
def main():
    #打印1-5之间的数，遇到3则停止
    for i in range(1,6):
        if i==3:
            break
        print(i)
    i=1
    while i<=5:
        if i==3:
            break
        print(i)
        i=i+1

    #打印1-5之间的数，遇到3则跳过
    for i in range(1,6):
        if i==3:
            continue
        print(i)
    i=0
    while i<=4:
        i = i + 1
        if i==3:
            continue
        print(i)





if __name__ == '__main__':
    main()
