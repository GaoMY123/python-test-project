class Master(object):
    def __init__(self):
        self.skill='古法煎饼果子配方'
    def make_jbgz(self):
        print('老师傅做的煎饼果子')
# 徒弟类
class BigCat(Master):
    def __init__(self):
        super().__init__()
        self.skill1='徒弟的煎饼果子配方'
    def make_jbgz(self):
        super().make_jbgz()
        print('徒弟做的煎饼果子')
dalong=BigCat()
print(dalong.skill1)
print(dalong.skill)
dalong.make_jbgz()
