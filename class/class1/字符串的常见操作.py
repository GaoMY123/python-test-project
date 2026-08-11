
def main():
    #find()方法:返回子字符串第一次出现的索引位置，如果子字符串不存在，则返回-1
    #index()方法:返回子字符串第一次出现的索引位置，如果子字符串不存在，则抛出异常
    #rfind()方法:返回子字符串最后一次出现的索引位置，如果子字符串不存在，则返回-1
    #rindex()方法:返回子字符串最后一次出现的索引位置，如果子字符串不存在，则抛出异常
    c="Hello World"
    print(c.find("s"))
    print(c.find("d"))
    print(c.find("l"))
    print(c.find("o"))
    print(c.rfind("l"))
    print(c.rfind("o"))
    print(c.find("l",3,6))
    print(c.index("l"))
    print(c.index("o"))
    print(c.index("l",3,6))
    #count()方法：返回字符在字符串中出现的次数
    print(c.count("l"))
    print(c.count("o"))
    #replace()方法，替换字符串
    print(c.replace("l","L"))
    #split()方法，将字符串按指定的分隔符进行分割
    s=c.split("l")
    print(s)
    print(type(s))
    print(c.split("l"))
    print(c.split("o"))
    #元组
    # c=(1,)
    # print(type(c))
    z={"ds","fd"}#集合
    print(type(z))
    v=["ds","fs"]#列表
    print(type(v))
    #字典
    # c={
    #     "name":"张三",
    #     "age":118
    # }
    print(type(c))
    #capitalize()方法:将字符串的第一个字符转换为大写，其他字符转换为小写
    print(c.capitalize())
    #title()方法:将字符串中的每个单词的第一个字符转换为大写，其他字符转换为小写
    print(c.title())
    #startswith()方法:判断字符串是否以指定的子字符串开头
    print(c.startswith("Hello"))
    print(c.startswith("World"))
    print(c.startswith("w"))
    print(c.startswith("l"))
    #endswith():判断字符串否以指定子字符串结尾
    print(c.endswith("World"))
    print(c.endswith("s"))
    #upper()将字符串中的所有字符转换为大写
    print(c.upper())
    #lower()将字符串中的所有字符转换为小写
    print(c.lower())
    #ljust()方法：将字符串左对齐，用指定的字符填充到指定的宽度
    print(c.ljust(20))
    #rjust()方法：将字符串右对齐，用指定的字符填充到指定的宽度
    print(c.rjust(20))
    #center()方法：将字符串居中对齐，用指定的字符填充到指定的宽度
    print(c.center(20))
    #lstrip()方法：删除字符串左侧的空格
    print(c.lstrip())
    #rstrip()方法：删除字符串右侧的空格
    print(c.rstrip())
    #strip()方法：删除字符串左侧和右侧的空格
    print(c.strip())
    #partition()方法：将字符串按指定的分隔符进行分割，返回一个三元组，包含子字符串、分隔符、子字符串
    print(c.partition("l"))
    #rpartition()方法：将字符串按指定的分隔符进行分割从右往左，返回一个三元组，包含子字符串、分隔符、子字符串
    print(c.rpartition("l"))
    #splitlines()方法：将字符串按换行符进行分割，返回一个列表，每个元素为一行\
    s="Hello world\nhello python"
    print(s.splitlines())
    #join()方法：将字符串列表中的元素用指定的分隔符进行连接接成一个字符串
    print("!".join(s.splitlines()))
    #isalpha()方法：判断字符串是否只包含字母
    print(c.isalpha())
    #isdigit()方法：判断字符串是否只包含数字
    print(c.isdigit())
    #isalnum()方法：判断字符串是否只包含字母和数字
    print(c.isalnum())
    #isspace()方法：判断字符串是否只包含空格
    print(c.isspace())



if __name__ == '__main__':
    main()
