#老师傅类
class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
    def make_jbgz(self):
        print('老师傅做的煎饼果子')
#学校类
class School(object):
    def make_cxlm(self):
        print('学会了朝鲜冷面')
    def make_klm(self):
        print('学会了烤冷面')
#徒弟类
class BigCat(Master,School):
    pass
dalong=BigCat()
print(dalong.skill)
dalong.make_jbgz()
dalong.make_klm()
dalong.make_cxlm()
#多个父类有同名方法时，子类对象调用该方法，会先从自身找
#如果没有按照继承的先后顺序
#也就是子类类名后的小括号中写入的父类类名的先后顺序
#__mro__:魔法属性，查看某个类调用的先后顺序
#获取多个父类的属性时，按照调用init方法的顺序进行获取
