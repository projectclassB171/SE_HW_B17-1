"""
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，直到有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
"""
import random  as  rn
class hero:
    def __init__(self, name, lv, race, maxblood ):
        self.name = name
        self.lv = lv # max_lv = 3
        self.race = race
        self.maxblood = maxblood
        self.blood = maxblood
        if self.race == 'humanity':
            self.flexibility = 0.2
        else :
            self.flexibility = 0.4
        if self.lv == 1:
            self.att = rn.randint(0, 10)
        elif self.lv == 2:
            self.att = rn.randint(0, 20)
        elif self.lv == 3:
            self.att = rn.randint(0, 30)
    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = rn.randint(0, 10)
            elif self.lv == 2:
                self.att = rn.randint(0, 20)
            elif self.lv == 3:
                self.att = rn.randint(0, 30)
            print(self.att)
            beattacked.minus_blood(self.att)
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name+ '的护盾被击碎了')
        print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) + "\n")
        print('------战斗结束-------')
        # 输出剩余血量
    def minus_blood(self, num):
        self.blood -= num

    def has_living(self):  # 判断是否还有血量
        if self.blood > 0:
            return True
        return False
class monster:
    def __init__(self, name, lv, maxblood ):
        self.name = name
        self.lv = lv # max_lv = 3
        self.maxblood = maxblood
        self.blood = maxblood
        self.blood = self.maxblood + 10
        if self.lv == 1:
            self.att = rn.randint(0, 10)
        elif self.lv == 2:
            self.att = rn.randint(0, 20)
        elif self.lv == 3:
            self.att = rn.randint(0, 30)
    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = rn.randint(0, 10)
            elif self.lv == 2:
                self.att = rn.randint(0, 20)
            elif self.lv == 3:
                self.att = rn.randint(0, 30)
            print(self.att)
            if beattacked.flexibility < rn.random():
                beattacked.minus_blood(self.att)
            else:
                beattacked.minus_blood(0)
                print('但是' + beattacked.name + '闪避了攻击！')
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) +
                  '剩余护盾：' + str(beattacked.maxblood + 10 - beattacked.blood) + "\n")
        else:
            print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) + "\n")
        print('------战斗结束-------')
        # 输出剩余血量
    def minus_blood(self, num):
        self.blood -= num

    def has_living(self):  # 判断是否还有血量
        if self.blood > 0:
            return True
        return False
#############################################
m1 = monster(name='【1级小怪兽】' , lv=1 , maxblood=20)  # 创建1级小怪兽
m2 = monster(name='【2级小怪兽】' , lv=2 , maxblood=30)  # 创建2级小怪兽
m3 = monster(name='【3级小怪兽】' , lv=3 , maxblood=50)  # 创建3级小怪兽
mo = [m1,m2,m3]
h = hero(name='【莫方】' , lv=3 , race='精灵',maxblood=100)  # 创建英雄
print(h.name + '的初始血量为:' + str(h.maxblood) + '他是一个' + h.race)
for m in mo:
    print(h.name + '的现有血量为：' + str(h.blood))
    if m.lv == 3:
        print(m.name + '的等级达到了三级，获得了10点护盾')
        print(m.name + '的初始血量:' + str(m.maxblood) + '  护盾：' + str(10))
    else:
        print(m.name + '的初始血量为:' + str(m.maxblood))
    print('------------战斗结束-------------')
    while m.has_living() and h.has_living():
        print(m.name + ' 对 ' + h.name + ' 造成伤害:')
        m.attack(h)
        print(h.name + ' 对 ' + m.name + ' 造成伤害:')
        h.attack(m)
    if m.has_living():
        print(m.name + ' win!')
    elif h.has_living():
        print(h.name + ' win~!')
    else:
        print(m.name + ' 和 ' + h.name + 'lose!')