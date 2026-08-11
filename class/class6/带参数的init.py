# 创建一个英雄游戏，英雄有姓名，职业，技能，血量，蓝量，护盾值
# class Hero(object):
#      def __init__(self,name,occupation,skill,hp,mp,shield):
#             self.name=name
#             self.occupation=occupation
#             self.skill=skill
#             self.hp=hp
#             self.mp=mp
#             self.shield=shield
#      def move(self):
#             print(self.name+'在移动')
#      def attack(self):
#             print(self.name+'在攻击')
#      def skill(self):
#             print(self.name+'正在使用技能'+self.skill)
#      def hp(self):
#             print(self.name+'的血量是'+str(self.hp))
#      def mp(self):
#             print(self.name+'的蓝量是'+str(self.mp))
#      def shield(self):
#             print(self.name+'的护盾值是'+str(self.shield))
# d=Hero('德玛西亚','战士','旋风斩',100,100,100)
# d.move()
# d.attack()
# d.skill()
# d.hp()
# d.mp()
# d.shield()
class Car(object):
     def __init__(self,color,model,horsepower):
         self.color=color
         self.model=model
         self.horsepower=horsepower
     def __str__(self):
         return f'颜色是{self.color}，型号是{self.model}，马力是{self.horsepower}'
Bmw=Car('银白色','宝马x5','1500')
Benz=Car('黑色','奔驰s180','1800')
print(f'颜色是{Bmw.color},型号是{Bmw.model},马力是{Bmw.horsepower}')
print(f'颜色是{Benz.color},型号是{Benz.model},马力是{Benz.horsepower}')
print(Bmw)
print(Benz)
