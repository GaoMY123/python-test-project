# 匿名函数
# lambda 参数列表：表达式
#无参数无返回值
from functools import reduce
import os
def demo():
    print(10)
demo()
demo1=lambda :10
#无参数有返回值
# def demo2():
    # return 10
# demo2()
demo2=lambda :10
demo2()
#有参数无返回值
demo3=lambda a,b:a+b
demo3(1,2)
#有参数有返回值
demo4=lambda a,b:a+b
print(demo4(1,2))
#列表推导式
#需求1：以列表的形式输出1-100之间的所有的数
li=[i for i in range(1,101)]
print(li)
#需求2：以列表的形式输出1-100之间的所有的偶数
li2=[i for i in range(1,101) if i%2==0]
print(li2)
#列表嵌套式
a=['赵','钱','孙','李']
b=['一','二','三','四']
for i in a:
    for j in b:
        print(i+j)
li3=[i+j for i in a for j in b]
print(li3)
#高阶函数：map()函数，filter()函数，reduce()函数
# 需求一：将以下列表输出为['1','2','3']
li=[1,2,3]
demo=list(map(lambda x:str(x),li))
# 需求二：将以下列表输出为[1,4,9]
demo3=list(map(lambda x:x**2,li))
#需求三：将以下列表为输出['Hello','Hi','Itfeat']
li4=['hello','hi','itfeat']
demo4=list(map(lambda x:x.capitalize(),li4))
print(demo4)
#需求一：将以下列表输出为[2,6]
li5=[1,2,6,7,9]
demo5=list(filter(lambda x: x%2==0,li5))
print(demo5)
#需求二：将以下列表输出为["Hello","Itfeat"]
li6=['Hello','hi','Itfeat']
demo6=list(filter(lambda x: x[0].isupper(),li6))
print(demo6)
#reduce()函数，将容器中的元素进行累计
li7=[1,2,3,4,5]
demo7=reduce(lambda a,b: a+b,li7)
print(demo7)
#文件的相关操作
# 打开文件，新建文件，有四种模式
# w,r,a,x
f=open('/aac.txt',mode="w",encoding='utf-8')
f.write("hi")
f.close()
#r
f=open('/aac.txt',mode='r',encoding='utf-8')
f.read()
print(f.readline())
print(f.readlines())
f.close()
#文件的备份
# 1.打开源文件
f=open('./aac.txt',mode='r',encoding='utf-8')
# 2.打开新文件
f1=open('./aac_copy.txt',mode='w',encoding='utf-8')
# 3.读取源文件中的全部内容
res=f.read()
# 4.将读取到的内容写入新文件
f1.write(res)

# 5.关闭源文件
f.close()
# 6.关闭新文件
f1.close()
# 文件及文件夹的相关操作
#文件重命名
os.rename("./aac.txt",'./aax.txt')
#删除文件
os.remove('aac_copy.txt')
#创建目录
os.mkdir("./test")
#获取当前目录路径
print(os.getcwd())
#切换目录
os.chdir('./aac')
#获取当前目录的列表
print(os.listdir())
#删除目录
os.remove('./aac')
#批量创建文件
for i in range(1,11):
    f=open('./aac.txt%s' % i,mode='w',encoding='utf-8')
    f.write("hi")
    f.close()
#切换目录
os.chdir("./test")
res=os.listdir()
#文件重命名
for i in res:
    new='It'+i
    os.rename(i,new)
