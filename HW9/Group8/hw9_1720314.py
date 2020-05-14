
'''
编写一个打怪兽的小游戏。
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
'''
from random import randint #导入函数


class hero():
    def __init__(self, name, hp, lever):
        self._name = name
        self._hp = hp
        self._lever = lever

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    def attack(self, monster):
        if self.avoid(monster._lever):
            print("{} 发起攻击".format(self.name))
        else:
            if self._lever == 1:
                harm = randint(1, 10)
            elif self._lever == 2:
                harm = randint(10, 20)
            else:
                harm = randint(20, 30)
            monster.hp -= harm
            print("{} 发起攻击：{}".format(self.name, harm))

    def upgrade(self):
        self._lever += 1 
        self.hp +=100 
        print("英雄血量+100".format(self.name))

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def avoid(self, m_lever):
        k = randint(0, 50)
        if m_lever == 1:
            if k < 10:
                return True
        elif m_lever== 2:
            if k < 15:
                return True
        else:
            if k < 20:
                return True
        return False

    def __str__(self):
        return '英雄:%s\n' % self._name + \
               '等级：%d\n' % self._lever + \
               '生命值：%d\n' % self._hp


class Monster(hero):

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def shanbi(self, hero):
        k = randint(0, 50)
        if hero._lever == 1:
            if k < 10:
                return True
        elif hero._lever == 1:
            if k < 20:
                return True
        else:
            if k < 30:
                return True
        return False

    def attack(self, hero):
        if self.avoid(hero):
            print("躲避")
        else:
            if self._lever == 1:
                harm = randint(10, 20)
            elif self._lever ==2:
                harm = randint(20, 30)
            else:
                harm = randint(30, 40)
            hero.hp -= harm
            print("{}发起攻击 {}".format(self.name,harm))

    def __str__(self):
        return '生命值：%d\n' % self.hp


def main():
    u = hero('精灵', 400, 1)
    m1 = Monster('怪兽1', 110, 1)
    m2 = Monster('怪兽2', 180, 2)
    m3 = Monster('大怪兽', 250, 3)
    ms = [m1, m2, m3]
    at_round = 1
    for i in ms:
        while u.hp > 0 and i.hp > 0:
            print('======第%d回合======' % at_round)
            u.attack(i)
            print(i)
            if i.hp > 0:
                i.attack(u)
            print(u)
            at_round += 1
    if u.hp > 0:
        print('英雄Win！')
    else:
        print('英雄Lose！')

if __name__ == '__main__':
    main()
