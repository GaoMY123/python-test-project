

def main():
    a="hello world"
    print(a)
    print(type(a))
    #索引
    print(a[0])
    print(a[-1])
    print(a[1:9:4])#切片,格式为变量名[起始值：结束值：步长]
    result=a[1:3]+a[4]#拼接字符串
    print(result)
    print(a[1:])
    #取第一个l出现的位置
    print(a.find("l"))
    print(a.index("l"))
    #取最后一个l出现的位置
    print(a.rfind("l"))
    print(a.rindex("l"))
    #快速反转字符串
    print(a[::-1])

if __name__ == '__main__':
    main()

