#class 类
# 新
class Person(object):
    pass
# 旧
class Person1():
    pass
#旧（经典）
class Person2:
    pass
#创建对象，对象名=类名（）
p=Person()
print(p)
# 给类添加方法
class Person3(object):
    def sing(self):
        print('唱歌')
p1=Person3()
p1.sing()#调用类中的方法，对象名，方法名（）
#如何给对象添加属性
p1.name='张三'
print(p1.name)
#修改
p1.name='李四'
print(p1.name)
#魔法方法,__init__
class Person4(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person4('张三',18)
print(p.name)
print(p.age)
p1=Person4('李四',20)
print(p1.name)
print(p1.age)
#self是一个万能词，哪个对象调用该方法，self就是那个对象的对象名，类中方法的第一个参数必须是self
#可以使用self访问类的任何属性
class Person5(object):
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def sing(self):
        print('唱歌'+self.name)
p=Person5('张三',18)
p.sing()
print(p.age)
print(p.name)
p1=Person5('李四',20)
p1.sing()
print(p1.age)
print(p1.name)
#带参数的init方法
class Person6(object):
    def __init__(self,color,model,horsepower):
        self.color=color
        self.model=model
        self.horsepower=horsepower
Bmw=Person6('银白色','宝马X5','1500')
Benz=Person6('黑色','奔驰S180','1800')
print(f"颜色是{Bmw.color}，型号是{Bmw.model}，马力是{Bmw.horsepower}")
print(f"颜色是{Benz.color}，型号是{Benz.model}，马力是{Benz.horsepower}")
print(Bmw)
print(Benz)
#__str__魔法方法，不需要手动调用，在对象被打印是会自动调用
#必须返回一个字符串的数据类型，记得返回
class Person7(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'姓名是{self.name}，年龄是{self.age}'
p=Person7('张三',18)
print(p)
p1=Person7('李四',20)
print(p1)
#__del__魔法方法，不需要手动调用，在对象被销毁时会自动调用
class Person8(object):
    def sing(self):
        print('唱歌')
    def __del__(self):
        print('对象被销毁了')
p=Person8()
print('好好学习 天天向上')
p.sing()
print('好好学习 天天向上')
#冒泡排序
li=[5,6,9,2,68,23]
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            print(li)
