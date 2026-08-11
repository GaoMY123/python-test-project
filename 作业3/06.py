# 6.使用两种方式将列表 li = [1, 2, 3, 4, 5] 变成 ["1", "2", "3", "4", "5"] (注：列表推导式和高阶函数)
li=[1, 2, 3, 4, 5]
print([str(i) for i in li])
print(list(map(lambda x:str(x),li )))