class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
    def make_jbgz(self):
        print('老师傅做的煎饼果子')
class BigCat(Master):
    def __init__(self):
        Master.__init__(self)#在类中调用父类的init方法
        self.skill1='徒弟的煎饼果子配方'
    def make_jbgz(self):
        Master.make_jbgz(self)#在类中：父类类名.同名方法名（self）
        print('徒弟做的煎饼果子')
dalong=BigCat()
dalong.make_jbgz()#调用自身得到属性和方法
#获取老师傅的属性和方法 在类外：父类类名.同名方法名（子类对象）,父类类名.__init__(子类对象名)
# Master.make_jbgz(dalong)
Master.__init__(dalong)
print(dalong.skill1)
print(dalong.skill)
