#需求：以列表的形式输出1-100之间的所有的数
li=[i for i in range(1,101)]
print(li)
#需求2：以列表的形式输出1-100之间的所有的偶数
li1=[i for i in range(1,101) if i%2==0]
print(li1)
#列表推导式的嵌套
#需求三：输出以下任意两字的名字
a=['赵','钱','孙','李']
b=['一','二','三','四']
li2=[i+j for i in a for j in b]
print(li2)
s=[]
for i in a:
    for j in b:
        s.append(i+j)
print(s)
