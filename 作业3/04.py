# 4.有列表li = [1,2,3,4,5]，使用两种方式完成生成目标列表 [1,4,9,16,25] (注：列表推导式和高阶函数)
li=[1,2,3,4,5]
print([i**2 for i in li])
print(list(map(lambda x:x**2,li)))
