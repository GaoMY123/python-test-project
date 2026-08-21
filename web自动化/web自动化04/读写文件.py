#方式一：使用open()函数
# f=open('./a.txt',"w",encoding="utf-8")
# f.write("hello world")
# f.close()
#方式二:使用with语句
with open('./a.txt',"w",encoding="utf-8") as f:
    f.write("hello world")
