# 1.有列表li = ["1", "13", "11", "6", "8"]，请将列表进行排序，生成：["1", "6", "8", "11", "13"]
li=["1", "13", "11", "6", "8"]
li2=[]
for i in li:
     li2.append(int(i))
     li2.sort()
print([str(i) for i in li2])
print([str(i) for i in sorted([int(x) for x in li])])

