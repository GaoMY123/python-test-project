#如何获取私有属性的值
#方式一：Python中的私有是假私有，虽然无法直接在类外获取，但在类中定义一个公有方法，获取私有属性的值
#在类外调用该公有方法即可
class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
        #私有属性
        self.__money=1000
    def get_money(self):
        print(f'钱为{self.__money}')
    def set_money(self,x):
        self.__money=x
class BigCat(Master):
    pass
dalong=BigCat()
dalong.get_money()
dalong.set_money(5010)
dalong.get_money()
#方式二：使用dir()变量名 查看某个对象可以调用的所有属性和方法
# print(dir(dalong))
print(dalong._Master__money)
