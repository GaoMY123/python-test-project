#实例方法：小括号中为self的方法，需要用对象名进行调用
#类方法：小括号中为cls的方法，需要再定义方法的上一行添加@classmethod
#静态方法：小括号中什么方法都没有，需要再定义方法的上一行添加@staticmethod
class Person(object):
    #实例方法
    def sing(self):
        print('在唱歌')
    # 类方法
    @classmethod
    def dance(cls):
        print('在跳舞')
    # 静态方法
    @staticmethod
    def sleep():
        print('在睡觉')
p=Person()
#调用实例方法 对象名.方法名（）
p.sing()
#调用类方法 类名.方法名()
Person.dance()
#调用静态方法 对象名.方法名（）  类名.方法名（）
Person.sleep()
p.sleep()