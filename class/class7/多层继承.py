#老师傅类
#类a继承类b，类b继承类c，可以调用类b类c中所有的属性和方法
class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
    def make_jbgz(self):
        print('老师傅做的煎饼果子')
class School(Master):
    def make_cxlm(self):
        print('学会了朝鲜冷面')
    def make_klm(self):
        print('学会了烤冷面')
class BigCat(School):
    pass
dalong=BigCat()
print(dalong.skill)
dalong.make_jbgz()
dalong.make_klm()
dalong.make_cxlm()
