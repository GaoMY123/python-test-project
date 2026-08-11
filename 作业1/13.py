'''
# 1. 电脑产生一个（1-100）的随机数，用户进行猜测(通过 input 输入)，直到猜中为止。
# 2. 如果猜对了，输出：恭喜你猜对了，数字是 xx。
# 3. 如果猜的数字比随机数大，输出：猜测的数字太大了，继续加油
# 4. 如果猜测的数字比随机数小，输出：猜测的数字有点小，再来一次
'''
import random
def main():
    num=random.randint(1,100)
    person=int(input("请输入你要猜的数字："))
    while person!=num:
        if person>num:
            print("猜测的数字太大了，继续加油")
        elif person<num:
            print("猜测的数字有点小，再来一次")
        person=int(input("请输入你要猜的数字："))
    else:
        print("恭喜你猜对了，数字是",num)

if __name__ == "__main__":
    main()

