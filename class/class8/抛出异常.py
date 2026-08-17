#自定义异常类
class AgeError(Exception):
    pass
class Person(object):
    def __init__(self,name,age):
        self.name=name
        #抛出异常
        if age<0:
            e=AgeError('年龄不能为负数')
            raise e
        self.age=age
p=Person('张三',12)
print(p)
