#super()只能用在类中，典型的应用场景是在父类的基础上添加自己的想法
class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
    def make_jbgz(self):
        print('老师傅做的煎饼果子')
class School(object):
    def __init__(self):
        self.skill2='学校的煎饼果子配方'
    def make_jbgz(self):
        print('学校的煎饼果子')
# 徒弟类
class BigCat(Master,School):
    def __init__(self):
        super(BigCat,self).__init__()
        super(Master,self).__init__()
        self.skill1='徒弟的煎饼果子配方'
    def make_jbgz(self):
        super(BigCat,self).make_jbgz()
        super(Master,self).make_jbgz()
        print('徒弟做的煎饼果子')
dalong=BigCat()
print(dalong.skill2)
print(dalong.skill1)
print(dalong.skill)
dalong.make_jbgz()
