# 计算1000以内所有不能被7整除的整数之和
def main():
   '''
   total = 0
    for i in range(1, 1001):
        if i % 7 != 0:
            total += i
    print(total)
   '''
   sum=0
   i=1
   while i<=1000:
       if i%7!=0:
           sum=sum+i
       i=i+1
   print(sum)

if __name__ == "__main__":
    main()