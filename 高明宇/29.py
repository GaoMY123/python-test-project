# 导入random模块,生成1-100间所有的随机列表(列表中的数字不重复,长度为100)
import random
li = []
while len(li) < 100:
    num = random.randint(1, 100)
    if num not in li:
        li.append(num)
print(li)