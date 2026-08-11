# 5.有列表li = [1,4,9,16,25]， 使用两种方式提取出大于10的数，提取结果为 [16,25] (注：列表推导式和高阶函数)
li=[1,4,9,16,25]
print([i for i in li if i>10])
print(list(filter(lambda x:x>10,li)))
