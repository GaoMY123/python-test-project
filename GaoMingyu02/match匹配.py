#match匹配，版本3.10以上

def main():
    match 1:
        case 1:
            print("x is 1")
        case 2:
            print("x is 2")
        #在没有其他匹配时执行代码块，会使用下划线字符_作为最后的案例值
        case _:
            print("x is not 1 or 2")



if __name__ =="__main__":
    main()
