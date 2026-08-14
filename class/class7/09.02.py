# #继承：子类可以继承父类的属性和方法
# class Master(object):
#     def __init__(self):
#         self.skill='能做出好吃的煎饼果子'
#     def jbgz(self):
#         print('老师傅做的煎饼果子')
# #单继承：子类只继承一个父类
# class BigCat(Master):
#     pass
# #调用子类的方法
# dalong=BigCat()
# dalong.jbgz()
# print(dalong.skill)
#老师傅类
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#     def make_jbgz(self):
#         print('老师傅做的煎饼果子')
# #学校类
# class School(object):
#     def make_cxlm(self):
#         print('学校做的朝鲜冷面')
#     def make_klm(self):
#         print('学校做的烤冷面')
# #徒弟类
# class BigCat(Master,School):
#     pass
# dalong=BigCat()
# dalong.make_cxlm()
# dalong.make_jbgz()
# dalong.make_klm()
# print(dalong.skill)
#重写
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#     def make_jbgz(self):
#         print('老师傅做的煎饼果子')
# class BigCat(Master):
#     def __init__(self):
#         self.skill1='徒弟的煎饼果子配方'
#     def make_jbgz(self):
#         Master.make_jbgz(self)
#         print('徒弟做的煎饼果子')
# dalong=BigCat()
# print(dalong.skill1)
# dalong.make_jbgz()
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#     def make_jbgz(self):
#         print('老师傅做的煎饼果子')
# class BigCat(Master):
#     def __init__(self):
#         Master.__init__(self)
#         self.skill1='徒弟的煎饼果子配方'
#     def make_jbgz(self):
#         Master.make_jbgz(self)
#         print('徒弟做的煎饼果子')
# dalong=BigCat()
# dalong.make_jbgz()
# Master.__init__(dalong)
# print(dalong.skill)
# print(dalong.skill1)
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#     def make_jbgz(self):
#         print('老师傅做的煎饼果子')
# class School(object):
#     def __init__(self):
#         self.skill2='学校的煎饼果子配方'
#     def make_jbgz(self):
#         print('学校的煎饼果子')
# class BigCat(Master,School):
#     def __init__(self):
#         super(Master,self).__init__()
#         super(BigCat,self).__init__()
#         self.skill1='徒弟的煎饼果子配方'
#     def make_jbgz(self):
#         super(Master,self).make_jbgz()
#         super(BigCat,self).make_jbgz()
#         print('徒弟做的煎饼果子配方')
# dalong=BigCat()
# print(dalong.skill1)
# print(dalong.skill)
# print(dalong.skill2)
# dalong.make_jbgz()
# class Person(object):
#     def __init__(self,name,sex,age,country):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         self.country=country
#     def eat(self):
#         print(f'{self.name}要吃饭')
#     def sleep(self):
#         print(f'{self.name}要睡觉')
#     def work(self):
#         print(f'{self.name}要工作')
#     def __str__(self):
#         return f'{self.name}是{self.sex}，{self.age}岁，来自{self.country}'
# p=Person('张三','男',18,'中国')
# print(p)
# class Student(Person):
#     def __init__(self,name,sex,age,country,school_name,no):
#         super().__init__(name,sex,age,country)
#         self.school_name=school_name
#         self.no=no
#     def eat(self):
#         print(f'{self.name}要吃饭')
#     def sleep(self):
#         print(f'{self.name}要睡觉')
#     def work(self):
#         print(f'{self.name}要学习')
#     def __str__(self):
#         return f'{super().__str__()}，{self.school_name}，{self.no}'
# p1=Student('李四','男',18,'中国','清华大学','1001')
# print(p1)
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#     def make_jbgz(self):
#         print('老师傅做的煎饼果子')
# class School(Master):
#     def make_cslm(self):
#         print('学会了朝鲜冷面')
#     def make_klm(self):
#         print('学会了烤冷面')
# dalong=School()
# print(dalong.skill)
# dalong.make_jbgz()
# dalong.make_cslm()
# dalong.make_klm()
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#         self.__money=1000
#     def make_jbgz(self):
#         print('老师傅做的煎饼果子')
#     def __make_klm(self):
#         print('老师傅做的烤冷面')
# class BigCat(Master):
#     pass
# dalong=BigCat()
# dalong.make_jbgz()
# print(dalong.skill)
# class Master(object):
#     def __init__(self):
#         self.skill='古法煎饼果子配方'
#         self.money=1000
#     def get_money(self):
#         print(f'钱为{self.money}')
#     def set_money(self,x):
#         self.money=x
# class BigCat(Master):
#     pass
# dalong=BigCat()
# dalong.get_money()
# dalong.set_money(5220)
# dalong.get_money()
# print(Master._Master__money)
# class Staff(object):
#     def work(self):
#         print('员工要工作')
# class ItBoy(Staff):
#     def work(self):
#         print('在敲代码')
# class UiGirl(Staff):
#     def work(self):
#         print('在画图')
# class Boss(object):
#     def arrange_work(self,x):
#         print('安排工作')
#         x.work()
# b=Boss()
# i=ItBoy()
# u=UiGirl()
# b.arrange_work(i)
# b.arrange_work(u)
# class Person(object):
#     def __init__(self):
#         self.name='张三'
#     money=100
# p=Person()
# print(p.name)
# p.name='李四'
# print(p.name)
# print(p.money)
# print(Person.money)
# Person.money=99999
# print(p.money)
# print(Person.money)
class Person(object):
    def sing(self):
        print('在唱歌')
    @classmethod
    def dance(cls):
        print('在跳舞')
    @staticmethod
    def sleep():
        print('在睡觉')
p=Person()
p.sing()
Person.dance()
Person.sleep()
p.sleep()