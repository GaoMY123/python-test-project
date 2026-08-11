# 10. 用 filter() 函数和 lambda 表达式快速求出100以内所有4的倍数
print(list(filter(lambda x:x%4==0,range(1,101))))
