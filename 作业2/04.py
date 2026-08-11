# 4.查看这个列表的规律：[1,4,9,16,25,36,49,64,81,100]，使用代码生成这个列表
def main():
    l=[]
    for i in range(1,11):
        l.append(i**2)
    print(l)
if __name__=="__main__":
    main()
