#全局变量
__all__=['age','demo']
age=18


#函数
def demo():
    return 10

#类
class Person(object):
    def sing(self):
        print('要唱歌')


#测试代码
if __name__=="__main__":#快捷键main
    print(age)
    print(demo())
    p=Person()
    p.sing()

