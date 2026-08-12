#继承：子类可以继承父类的属性和方法
class Master(object):
    def __init__(self):
        self.skill='能做出好吃的煎饼果子'
    def jbgz(self):
        print('老师傅做的煎饼果子')
#单继承：子类只继承一个父类
class BigCat(Master):
    pass
#调用子类的方法
dalong=BigCat()
print(dalong.skill)
dalong.jbgz()
