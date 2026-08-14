#不同的子类对象，调用相同的父类方法，产生了不同的执行结果
#员工
class Staff(object):
    def work(self):
        print('员工工作')
class ItBoy(Staff):
    def work(self):
        print('在敲代码')
class UiGirl(Staff):
    def work(self):
        print('在画图')
class Boss(object):
    def arrange_work(self,x):
        print('安排工作')
        x.work()
b=Boss()
i=ItBoy()
u=UiGirl()
b.arrange_work(i)
b.arrange_work(u)
