def main():

 '''
  强制类型转换：将一个数据类型转换为另一个数据类型，通常用于数据类型的转换。
  例如：将整数转换为浮点数，将字符串转换为整数等。
  注意：强制类型转换可能会导致数据丢失或精度损失，因此在使用时需要谨慎。
  格式为：变量名=类型(表达式)
  eval()函数：将字符串转换为表达式，通常用于动态执行用户输入的表达式。
  例如：eval('18')返回18，eval('18+2')返回20等。
  '''
 num=18
 s=float(num)
 print(s)
 print(type(s))
 l=float(num)
 print(l)
 print(type(l))
 s=str(num)
 print(type(s))
 print(s)
 a=48
 b=45
 s='a+b'
 print(eval(s))#注意：eval()函数只能用于执行简单的表达式，不能用于执行复杂的语句或函数
 #append()方法：将一个字符串追加到另外一个字符串的末尾
 h=["apple","banana","orange"]
 h.append("peach")
 print(h)
 #insert()方法：在指定位置插入一个字符串
 h.insert(2,"watermelon")
 print(h)
 #extend方法：将一个列表中的元素追加到另外一个列表的末尾
 h2=["grape","apple"]
 h.extend(h2)
 print(h)
 #remove()方法，删除指定元素,如果有相同的元素，优先删除第一个元素
 h.remove("apple")
 print(h)
 #pop()方法，删除指定位置的元素，默认删除最后一个元素
 h.pop(2)
 print(h)
 #del()方法，删除指定位置的元素,同时也可以删除整个列表
 del h[1:3]#删除索引为1和2的元素
 print(h)
 #del h#删除整个列表
 #clear()方法，清空列表中的所有元素
 #h.clear()
 print(h)
 #遍历链表中的所有元素，使用for循环
 for i in h:
    print(i)
 #range()函数：生成一个整数序列，从0开始，每次增加1，直到达到指定的上限。
 #例如：range(10)生成0到9的整数序列
 #range(1,10)生成1到9的整数序列
 #range(1,10,2)生成1到9的偶数序列
 for i in range(10):
    print(i)
 #range()函数的其他参数
 #range(start,stop,step)
 #start：起始值，默认为0
 #stop：结束值，不包含在序列中
 #step：步长，默认为1
 #例如：range(1,10,2)生成1到9的偶数序列
 for i in range(1,10,2):
    print(i)
 #遍历链表中的所有元素，可以使用range()函数和len()函数，生成一个从0到链表长度-1的整数序列
 for i in range(len(h)):
    print(h[i])
 #while循环：在满足指定条件时，重复执行代码块。
 #例如：while i<10: print(i)
 #     i=i+1
 #     print(i)
 i=0
 while i<len(h):
    print(h[i])
    i=i+1
#使用列表推导来遍历链表中的所有元素
 [print(i) for i in h]
 '''
 列表推导：使用列表推导式来创建一个新的列表，通常用于在一行代码中完成多个操作。
 格式为：[表达式 for 变量 in 可迭代对象 if 条件]
 举例：
 [i for i in range(10)]生成0到9的整数序列
 
 '''
 #将fruits = ["apple", "banana", "cherry", "kiwi", "mango"]中的数据传输到一个空的链表当中
 fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
 h3=[]
 for i in fruits:
  if "a" in i:
   h3.append(i)
 print(h3)
#采用列表推导的形式来完成
 h3=[i for i in fruits if 'a' in i]
 print(h3)
 h3=[i for i in fruits if i!='apple' ]
 print(h3)
 #可以采用列表推导的方式将链表中的值换成新的值或者将值转换为大写或者小写或者其他操作
 #title()方法：将字符串中的每个单词的首字母转换为大写，其他字母转换为小写
 h3=[i.upper() for i in fruits]
 print(h3)
 h3=[i.lower() for i in fruits]
 print(h3)
 h3=[i.title() for i in fruits]
 print(h3)
 #升序和降序排列，升序的关键字为sort(),降序的关键字为sort(reverse=True)
 h3.sort()
 print(h3)
 h3.sort(reverse=True)
 print(h3)
 #自定义排序函数，关键字参数：key=function
 h3.sort(key=len)
 print(h3)
 #不区分大小写的排序，可以使用关键字参数：key=str.lower
 h3.sort(key=str.lower)
 print(h3)
 #反转排序，关键字使用reverse()
 h3.reverse()
 print(h3)
 #列表的复制，可以使用copy（）方法，也可以使用切片操作，也可以使用内置函数list（）
 h4=h3.copy()
 print(h4)
 h4=list(h3)
 print(h4)
 h4=h3[:]
 print(h4)
 #join list：将列表中的元素使用指定的分隔符连接起来，最简单的方法就是使用+号，也可以使用join()方法，或者使用extend()方法,可以使用for循环，将每个元素都插入到新的列表中的指定位置
 list1 = ["a", "b", "c"]
 list2 = [1, 2, 3]

 for x in list2:
  list1.append(x)#将list2中的每个元素都插入到list1的末尾

 print(list1)
 h2.extend(h3)
 print(h2)
 '''
 append()	Adds an element at the end of the list
 clear()	Removes all the elements from the list
 copy()	Returns a copy of the list
 count()	Returns the number of elements with the specified value
 extend()	Add the elements of a list (or any iterable), to the end of the current list
 index()	Returns the index of the first element with the specified value
 insert()	Adds an element at the specified position
 pop()	Removes the element at the specified position
 remove()	Removes the item with the specified value
 reverse()	Reverses the order of the list
 sort()	Sorts the list
 可以在列表中使用的内置方法
 '''

if __name__ == '__main__':
 main()












