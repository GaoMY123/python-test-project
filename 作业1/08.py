'''
闰年判断程序(闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)

输入一个有效的年份，判断是不是闰年

如果是闰年，则打印“xxxx年是闰年”；否则打印“xxxx年不是闰年”

如输入"2018"，将打印“2018年不是闰年”
'''
def main():
   i=0
   for i in range(5):
    year=int(input("请输入一个年份："))
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"{year}是闰年")
    else:
        print(f"{year}不是闰年")
if __name__=="__main__":
    main()
