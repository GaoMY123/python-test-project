#返回值作用：
#1 ：将函数的执行结果返回给调用者
#2 结束函数的调用
def main():
    def demo(a,b):
        # return a+b
        # return a+b,a*b
        return {"和为":a+b,"积为":a*b}
    print(demo(1,2))
    print(type(demo(1,2)))
if __name__ == "__main__":
    main()
