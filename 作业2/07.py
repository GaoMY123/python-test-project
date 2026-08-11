# 有列表 li = [1, 2, 1, 5, 2, 7, 19, 14, 4]，写代码统计出列表中每个元素出现的次数，结果格式不限
def main():
    li=[1,2,1,5,2,7,19,14,4]
    d={}
    for i in li:
        d[i]=li.count(i)
    print(d)
if __name__=="__main__":
    main()
