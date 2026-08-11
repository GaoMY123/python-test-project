# 编写程序，求 1 - 3 + 5 - 7 + 9 -11 + 13 - 15 ... - 99 + 101 的值    答案51
def main():
    sum = 0
    sign = 1
    for i in range(1, 102, 2):
        sum += sign * i# 从1开始，每次增加2，直到101
        sign = -sign# 每次循环，符号取反
        print(sum)

if __name__ == "__main__":
    main()