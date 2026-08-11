#__str__:是一个魔法方法，不需要手动调用，在对象被打印是会自动调用该方法
#必须返回一个字符串的数据类型，记得要返回
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'姓名是{self.name}，年龄是{self.age}'
p=Person('张三',18)
print(p)
p1=Person('李四',20)
print(p1)
