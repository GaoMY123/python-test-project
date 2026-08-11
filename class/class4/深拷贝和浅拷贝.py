# 深拷贝和浅拷贝
#深拷贝：完完全全的拷贝，拷贝之后的数据和元数据没有任何关系copy.deepcopy()
#浅拷贝：只拷贝了数据，没有复制内部子对象copy.copy()
#表层数据：只拷贝了数据，没有复制内部子对象
#内部子对象：原数据修改的话，会影响拷贝后的数据
import copy
data={"name":"张三","age":18}
data1=copy.deepcopy(data)
data["height"]=180.1
print(data)
print(data1)
#浅拷贝
data2=copy.copy(data)
data["class"]=3
data["name"]='李四'
print(data)
print(data2)
