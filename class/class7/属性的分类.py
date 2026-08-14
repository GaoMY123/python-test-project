#实例属性：定义在init方法中的属性
#类属性:定义在类中方法外的属性
class Person(object):
    def __init__(self):
        self.name='张三'
    money=1000
#创建对象 对象名=类名()
p=Person()
#获取实例属性 对象名.属性名
print(p.name)
#修改实例属性 对象名.属性名=新值
p.name='李四'
print(p.name)
#获取类属性 对象名.属性名 类名.属性名
print(p.money)
print(Person.money)
#修改类属性 类名.属性名=新值
Person.money=999999
print(p.money)
print(Person.money)