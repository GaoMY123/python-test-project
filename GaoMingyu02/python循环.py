def main():
    #while循环
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")
    #for循环
    for i in range(6):
        print(i)
    else:
        print("i is no longer less than 6")
    print("i is no longer less than 6")
    #for循环不能是空的，但如果你有没有内容的for循环，请输入语pass句以避免错误。
if __name__ =="__main__":
    main()
