#重写:子类中的方法名和父类中一致时就叫做重写
#子类重写父类的属性和方法后能调用的永远是自身的属性和方法
#老师父类
class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
    def make_jbgz(self):
        print('老师傅做的煎饼果子')
#徒弟类
class BigCat(Master):
    def __init__(self):
        self.skill='徒弟的煎饼果子配方'
    def make_jbgz(self):
        print('徒弟做的煎饼果子')
dalong=BigCat()
print(dalong.skill)
dalong.make_jbgz()