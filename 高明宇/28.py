# 通过循环创建十个文件，命名为1.txt，2.txt，3.txt....然后将文件名修改为:副本1.txt，副本2.txt，副本3.txt...[备注:将代码使用txt文件上传】
import os

# 1. 循环创建十个文件：1.txt、2.txt...10.txt
for i in range(1, 11):
    f = open('%d.txt' % i, mode='w', encoding='utf-8')
    f.write(str(i))
    f.close()

# 2. 将文件名修改为：副本1.txt、副本2.txt...副本10.txt
for i in range(1, 11):
    os.rename('%d.txt' % i, '副本%d.txt' % i)