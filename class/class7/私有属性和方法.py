#如何定义私有属性和方法
# 在属性名或者方法名前加两个下划线，私有后再类外无法直接获取
#老师傅类
class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
        #私有属性
        self.__money=1000

    def make_jbgz(self):

        print('老师傅做的煎饼果子')
    def __make_klm(self):
        print('老师傅做的烤冷面')
#徒弟类
class BigCat(Master):
    pass
dalong=BigCat()
dalong.make_jbgz()
# dalong.__make_klm()#私有方法无法被调用
print(dalong.skill)
# print(dalong.__money)#私有属性无法被调用
#如何获取私有属性的值
#方式一：Python中的私有是假私有，虽然无法直接在类外获取，但在类中定义一个公有方法，获取私有属性的值
#在类外调用该公有方法即可

