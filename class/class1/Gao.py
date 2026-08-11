def main():
    #使用for循环嵌套打印*代码
    for i in range(5):
        for j in range(i+1):
            print("*",end="")
        print()
    #使用while循环嵌套打印*代码
    i=0
    while i<5:
        j=0
        while j<=i:
            print("*",end="")
            j=j+1
        print()
        i=i+1
    #打印三角形
    i=1
    while i<=5:
        j=1
        while j<=i:
            print('*',end=' ')
            j=j+1
        print()
        i=i+1
    #打印倒三角形
    i=5
    while i>=1:
        j=1
        while j<=i:
            print('*',end=' ')
            j=j+1
        print()
        i=i-1
    #打印乘法表
    i=1
    while i<=9:
        j=1
        while j<=i:
            print(f"{i}*{j}={i*j}",end=' ')
            j=j+1
        print()
        i=i+1
    #打印等腰三角形
    i=1
    while i<=5:
        j=1
        while j<=5-i:
            print(' ',end='')
            j=j+1
        k=1
        while k<=i:
            print("*",end=' ')
            k=k+1
        print()
        i=i+1
    #for循环
    #生成1-10之间的所有数
    for i in range(1,11):
        print(i)
    #生成1-100之间的偶数
    for i in range(2,101,2):
        print(i)
    #生成1-100之间的所有数
    for i in range(1,101):
        print(i)
    #生成1-100之间的奇数
    for i in range(1,101,2):
        print(i)
    #生成1-100之间所有数的和
    sum=0
    for i in range(1,101):
        sum=sum+i
    print(sum)
    #生成1-100之间所有偶数的和
    sum=0
    for i in range(2,101,2):
        sum=sum+i
    print(sum)
    # 生成一个斐波那契数列
    a=[1,1]
    for i in range(2,10):
        a.append(a[i-1]+a[i-2])
        print(a)
        print(a[i])
    #打印100-1之间的所有数
    for i in range(100,0,-1):
        print(i)
    #break和continue
    #打印1-5之间的数，遇到3就停止
    for i in range(1,6):
        if i==3:
            break
        print(i)
    i=1
    while i<=5:
        if i==3:
            break
        print(i)
        i=i+1
    #打印1-5之间的数，遇到3就跳过
    for i in range(1,6):
        if i==3:
            continue
        print(i)
    i=1
    while i<=5:
        i=i+1
        if i==3:
            continue
        print(i)
    #字符串
    a="hello world"
    print(a)
    print(a[0])
    print(a[0])
    print(a[-1])
    print(a[1:5])
    print(a[1:9:4])
    print(a[1:9:2])
    result=a[1:3]+a[5]
    print(result)
    print(a.find("world"))
    print(a.find("l"))
    print(a.find("o"))
    print(a.index("l"))
    print(a.index("o"))
    print(a.rfind("l"))
    print(a.rindex("l"))
    print(a[::-1])
    #find()方法:返回子字符串第一次出现的索引位置，如果子字符串不存在，则返回-1
    print(a.find("s",3,5))
    #index()方法:返回子字符串第一次出现的索引位置，如果子字符串不存在，则抛出异常
    print(a.index("l",1,9))
    #rfind()方法:返回子字符串最后一次出现的索引位置，如果子字符串不存在，则返回-1
    print(a.rfind("l"))
    print(a.rfind("o"))
    #rindex()方法:返回子字符串最后一次出现的索引位置，如果子字符串不存在，则抛出异常
    print(a.rindex("l"))
    print(a.rindex("o"))
    #count()方法：返回字符在字符串中出现的次数
    print(a.count("l"))
    print(a.count("o"))
    #replace()方法，替换字符串
    print(a.replace("l","L"))
    #split()方法，将字符串按指定的分隔符进行分割
    s=a.split("l")
    print(s)
    print(type(s))
    print(a.split("l"))
    print(a.split("o"))
    #capitalize()方法:将字符串的第一个字符转换为大写，其他字符转换为小写
    print(a.capitalize())
    #title()方法:将字符串中的每个单词的第一个字符转换为大写，其他字符转换为小写
    print(a.title())
    #startswith()方法:判断字符串是否以指定的子字符串开头
    print(a.startswith("hello"))
    print(a.startswith("w"))
    print(a.startswith("l"))
    #endswith()方法：判断字符串是否以指定的字符串结尾
    print(a.endswith("World"))
    print(a.endswith("s"))
    print(a.endswith("d"))
    #upper()将字符串中的所有字符转换为大写
    print(a.upper)
    #lower()将字符串中的所有字符转换为小写
    print(a.lower)
    #ljust()方法，将字符串左对齐，用指定的字符填充到最右侧
    print(a.ljust(20))
    #rjust()方法，将字符串对齐，用指定的字符填充到最右侧
    print(a.rjust(20))
    #center()方法，将字符串居中对齐
    print(a.center(20))
    #lstrip()方法，将字符串左侧的空格去掉
    print(a.lstrip())
    #rstrip()方法，将字符串右侧的空格去掉
    print(a.rstrip())
    #strip()方法，将字符串左右两侧的空格去掉
    print(a.strip)
    #partition()方法，将字符串按指定的分隔符进行分割，返回一个三元数组，包含子字符串、分隔符、子字符串
    print(a.partition("l"))
    print(a.partition("o"))
    #rpartition()方法，将字符串按指定的分隔符进行分割，返回一个三元数组，包含子字符串、分隔符、子字符串
    print(a.rpartition("l"))
    #splitlines()方法，将字符串按行进行分割，返回一个列表，每个元素为一行
    s="hello world\nhello world\nhello world"
    print(s.splitlines())
    #使用for循环嵌套打印*代码
    for i in range(5):
        for j in range(i+1):
            print("*",end="")
        print()
    #使用while循环嵌套打印*代码
    i=0
    while i<5:
        j=0
        while j<=i:
            print("*",end="")
            j=j+1
        print()
        i=i+1
    #打印三角形
    i=1
    while i<=5:
        j=1
        while j<=i:
            print('*',end=' ')
            j=j+1
        print()
        i=i+1
    #打印倒三角形
    i=5
    while i>=1:
        j=1
        while j<=i:
            print('*',end=' ')
            j=j+1
        print()
        i=i-1
    #打印乘法表
    i=1
    while i<=9:
        j=1
        while j<=i:
            print(f"{i}*{j}={i*j}",end=' ')
            j=j+1
        print()
        i=i+1
    #打印等腰三角形
    i=1
    while i<=5:
        j=1
        while j<=5-i:
            print(' ',end='')
            j=j+1
        k=1
        while k<=i:
            print("*",end=' ')
            k=k+1
        print()
        i=i+1
    #for循环
    #生成1-10之间的所有数
    for i in range(1,11):
        print(i)
    #生成1-100之间的偶数
    for i in range(2,101,2):
        print(i)
    #生成1-100之间的所有数
    for i in range(1,101):
        print(i)
    #生成1-100之间的奇数
    for i in range(1,101,2):
        print(i)
    #生成1-100之间所有数的和
    sum=0
    for i in range(1,101):
        sum=sum+i
    print(sum)
    #生成1-100之间所有偶数的和
    sum=0
    for i in range(2,101,2):
        sum=sum+i
    print(sum)
    # 生成一个斐波那契数列
    a=[1,1]
    for i in range(2,10):
        a.append(a[i-1]+a[i-2])
        print(a)
        print(a[i])
    #打印100-1之间的所有数
    for i in range(100,0,-1):
        print(i)
    #break和continue
    #打印1-5之间的数，遇到3就停止
    for i in range(1,6):
        if i==3:
            break
        print(i)
    i=1
    while i<=5:
        if i==3:
            break
        print(i)
        i=i+1
    #打印1-5之间的数，遇到3就跳过
    for i in range(1,6):
        if i==3:
            continue
        print(i)
    i=1
    while i<=5:
        i=i+1
        if i==3:
            continue
        print(i)
    #字符串
    a="hello world"
    print(a)
    print(a[0])
    print(a[0])
    print(a[-1])
    print(a[1:5])
    print(a[1:9:4])
    print(a[1:9:2])
    result=a[1:3]+a[5]
    print(result)
    print(a.find("world"))
    print(a.find("l"))
    print(a.find("o"))
    print(a.index("l"))
    print(a.index("o"))
    print(a.rfind("l"))
    print(a.rindex("l"))
    print(a[::-1])
    #find()方法:返回子字符串第一次出现的索引位置，如果子字符串不存在，则返回-1
    print(a.find("s",3,5))
    #index()方法:返回子字符串第一次出现的索引位置，如果子字符串不存在，则抛出异常
    print(a.index("l",1,9))
    #rfind()方法:返回子字符串最后一次出现的索引位置，如果子字符串不存在，则返回-1
    print(a.rfind("l"))
    print(a.rfind("o"))
    #rindex()方法:返回子字符串最后一次出现的索引位置，如果子字符串不存在，则抛出异常
    print(a.rindex("l"))
    print(a.rindex("o"))
    #count()方法：返回字符在字符串中出现的次数
    print(a.count("l"))
    print(a.count("o"))
    #replace()方法，替换字符串
    print(a.replace("l","L"))
    #split()方法，将字符串按指定的分隔符进行分割
    s=a.split("l")
    print(s)
    print(type(s))
    print(a.split("l"))
    print(a.split("o"))
    #capitalize()方法:将字符串的第一个字符转换为大写，其他字符转换为小写
    print(a.capitalize())
    #title()方法:将字符串中的每个单词的第一个字符转换为大写，其他字符转换为小写
    print(a.title())
    #startswith()方法:判断字符串是否以指定的子字符串开头
    print(a.startswith("hello"))
    print(a.startswith("w"))
    print(a.startswith("l"))
    #endswith()方法：判断字符串是否以指定的字符串结尾
    print(a.endswith("World"))
    print(a.endswith("s"))
    print(a.endswith("d"))
    #upper()将字符串中的所有字符转换为大写
    print(a.upper)
    #lower()将字符串中的所有字符转换为小写
    print(a.lower)
    #ljust()方法，将字符串左对齐，用指定的字符填充到最右侧
    print(a.ljust(20))
    #rjust()方法，将字符串对齐，用指定的字符填充到最右侧
    print(a.rjust(20))
    #center()方法，将字符串居中对齐
    print(a.center(20))
    #lstrip()方法，将字符串左侧的空格去掉
    print(a.lstrip())
    #rstrip()方法，将字符串右侧的空格去掉
    print(a.rstrip())
    #strip()方法，将字符串左右两侧的空格去掉
    print(a.strip)
    #partition()方法，将字符串按指定的分隔符进行分割，返回一个三元数组，包含子字符串、分隔符、子字符串
    print(a.partition("l"))
    print(a.partition("o"))
    #rpartition()方法，将字符串按指定的分隔符进行分割，返回一个三元数组，包含子字符串、分隔符、子字符串
    print(a.rpartition("l"))
    #splitlines()方法，将字符串按行进行分割，返回一个列表，每个元素为一行
    s="hello world\nhello world\nhello world"
    print(s.splitlines())
if  __name__ == '__main__':
    main()
