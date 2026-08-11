
def main():
    a=100
    def test4():
        a=10
        print(a)
    test4()
    print(a)
    #global：在函数内部定义的变量，可以在函数外部使用
    #nonlocal：在函数内部定义的变量，可以在函数外部使用，在函数嵌套时使用
    def test5():
        nonlocal a
        a=1000
        print(a)
    print(a)
    test5()
    print(a)
    data={'001':{'no':'001','name':'张三','score':100},'002':{}}
if __name__=="__main__":
    main()