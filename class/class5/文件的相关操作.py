import os
# #打开，新建文件,有四种模式
# #w:写入，r:读取，a：追加，x：创建，b：二进制模式
# f=open('./aaa.txt',mode='w',encoding='utf-8')
# f.write("hello everyone")
# f.close()
# #读取文件,read():读取文件中所有内容,readlines():读取文件中所有行内容，返回列表的数据类型,readline():读取文件中第一行内容
# f=open('./aaa.txt',mode='r',encoding='utf-8')
# print(f.read())
# print(f.readlines())
# print(f.readline())
# f.close()
# #r模式和w模式的区别
# # r模式下只能执行读取操作，文件不存在则报错
# # w模式下只能执行写入操作，文件不存在则新建，存在则覆盖
# #文件的备份
# # 1.打开源文件
# f=open('./aaa.txt',mode='r',encoding='utf-8')
# # 2.打开新文件
# f1=open('./aaa_backup.txt',mode='w',encoding='utf-8')
# # 3.读取源文件中的全部内容
# content=f.read()
# # 4.将读取出的内容写入新文件
# f1.write(content)
# # 5.关闭源文件
# f.close()
# # 6.关闭新文件
# f1.close()
#文件及文件夹的相关操作
#文件重命名
# os.rename("./aaa.txt","./abc.txt")
#删除文件
# os.remove("./aaa_backup.txt")
#创建目录
# os.mkdir("./test")
#获取当前目录路径
# print(os.getcwd())
# #切换目录
# print(os.chdir("./test"))
# print(os.getcwd())
# # 获取当前目录列表
# print(os.listdir())
# 删除目录
# os.rmdir("./test")
# 批量创建文件
# for i in range(1,11):
#     f=open(r'C:\Users\高明宇\Desktop\AAA\abc%s.txt' % i,mode='w',encoding='utf-8')
#     f.write("yes")
#     f.close()
# 批量修改文件名
#切换目录
os.chdir(r'C:\Users\高明宇\Desktop\AAA')
res=os.listdir()
# print(res)
#文件重命名
for i in res:
    new_name="it"+i
    os.rename(i,new_name)
