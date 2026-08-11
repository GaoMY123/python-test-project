#__del__:是一个魔法方法，不需要手动调用，在对象被销毁时会自动调用该方法

class Person(object):
    def sing(self):
        print('我会唱歌')
    def __del__(self):
        print('对象被销毁了')
p=Person()
print('好好学习 天天向上')

p.sing()
print('好好学习 天天向上')