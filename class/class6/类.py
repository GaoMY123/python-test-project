#类
# class Person(object):
#     pass#新式类
# # 旧式类
# class Person2():
#     pass
# #旧式类（经典类）
# class Person3:
#     pass
# # 创建对象 对象名=类名()
# p=Person()
# p2=Person2()
# p3=Person3()
#给类添加方法
# class Person(object):
#     def sing(self):
#         print("我会唱歌")
# p=Person()#创建对象
# p.sing()#调用类中的方法 对象名.方法名()
# #如何给对象添加属性
# p.name='张三'#对象名.属性名=属性值
# print(p.name)
# #修改
# p.name='李四'
# print(p.name)
# #魔法方法
# # __init__:是一个魔法方法，不需要手动调用，在对象被创建是会自动调用该方法
# class Person1(object):
#     def __init__(self,name,age):
#         print("对象被创建了")
#         # 在类中给对象添加属性
#         self.name=name
#         self.age=age
# p=Person1('张三',18)
# print(p.name)
# print(p.age)
# p1=Person1('李四',20)
# print(p1.name)
# print(p1.age)
#self:是一个万能词，那个对象调用该方法，self就是那个对象的对象名，类中方法的第一个参数必须是self
# 可以使用self访问类的任何属性
#调用另一个方法中的方法使用self

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self):
        print(self.name+'在唱歌')
p=Person('张三',18)
print(p.name)
p.sing()
print(p.age)
p1=Person('李四',20)
print(p1.name)
print(p1.age)
p1.sing()