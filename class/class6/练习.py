# 创建一个英雄游戏，英雄有姓名，职业，技能，血量，蓝量，护盾值
class Hero(object):
     def __init__(self,name,occupation,skill,hp,mp,shield):
            self.name=name
            self.occupation=occupation
            self.skill=skill
            self.hp=hp
            self.mp=mp
            self.shield=shield
     def move(self):
            print(self.name+'在移动')
     def attack(self):
            print(self.name+'在攻击')
     def use_skill(self):
            print(self.name+'正在使用技能'+self.skill)
     def show_hp(self):
            print(self.name+'的血量是'+str(self.hp))
     def show_mp(self):
            print(self.name+'的蓝量是'+str(self.mp))
     def show_shield(self):
            print(self.name+'的护盾值是'+str(self.shield))
d=Hero('德玛西亚','战士','旋风斩','100','100','100')
d.move()
d.attack()
d.use_skill()
d.show_hp()
d.show_mp()
d.show_shield()
