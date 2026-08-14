class Person(object):
    def __init__(self,name,sex,age,country):
        self.name=name
        self.sex=sex
        self.age=age
        self.country=country
    def eat(self):
        print(f'{self.name}要吃饭')
    def sleep(self):
        print(f'{self.name}要睡觉')
    def work(self):
        print(f'{self.name}要工作')
    def __str__(self):
        return f'姓名是{self.name}，性别是{self.sex}，年龄是{self.age}，国家是{self.country}'
p=Person("李四",'男','18','中国')
print(p)
class Student(Person):
    def __init__(self,name,sex,age,country,school_name,no):
        super().__init__(name,sex,age,country)
        self.school_name=school_name
        self.no=no
    def eat(self):
        super().eat()
        print(f'{self.name}要吃饭')
    def sleep(self):
        super().sleep()
        print(f'{self.name}要睡觉')
    def work(self):
        super().work()
        print(f'{self.name}要学习')
    def __str__(self):
        return f'{super().__str__()}，学校是{self.school_name}，学号是{self.no}'
p1=Student('张三','男',18,'中国','清华大学','1001')
p1.eat()
p1.sleep()
p1.work()
print(p1)

